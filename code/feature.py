import argparse
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import esm

parser = argparse.ArgumentParser()
parser.add_argument("--esm_model", default="esm2_t36_3B_UR50D")
parser.add_argument("--layer", type=int, default=36)
parser.add_argument("--embedding_dim", type=int, default=1)
parser.add_argument("--protein_csv", required=True)
parser.add_argument("--glycan_csv", required=True)
parser.add_argument("--zscore_csv", required=True)
parser.add_argument("--output", default="lectin_dataset.csv")

args = parser.parse_args()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, alphabet = esm.pretrained.__dict__[args.esm_model]()
batch_converter = alphabet.get_batch_converter()

model = model.eval().to(device)
protein = pd.read_csv(args.protein_csv)
protein = protein.drop(non_lectin, axis=0)
seq = protein.iloc[:, 0].tolist()
protein_embeds = []
chunk_size = 1

for i in range(0, len(seq), chunk_size):

    batch_seqs = seq[i:i + chunk_size]

    data_list = [
        (str(j), s) for j, s in enumerate(batch_seqs)
    ]

    batch_labels, batch_strs, batch_tokens = batch_converter(data_list)

    batch_tokens = batch_tokens.to(device)

    batch_lens = (batch_tokens != alphabet.padding_idx).sum(1)

    with torch.no_grad():
        results = model(batch_tokens, repr_layers=[args.layer])

    token_reps = results["representations"][args.layer]

    for idx, l in enumerate(batch_lens):

        rep = token_reps[idx, 1:l-1].mean(0)
        protein_embeds.append(rep.cpu().numpy())

protein_feature = pd.DataFrame(protein_embeds)
glycan = pd.read_csv(args.glycan_csv, header=None)

max_value = int(glycan.max().max())

embedding = nn.Embedding(max_value + 1, args.embedding_dim)

glycan_tensor = torch.LongTensor(glycan.values)

with torch.no_grad():
    glycan_emb = embedding(glycan_tensor)

glycan_feature = glycan_emb.view(glycan_emb.shape[0], -1).numpy()

glycan_feature = pd.DataFrame(glycan_feature)
zsorce_data = pd.read_csv(args.zscore_csv)
data = zsorce_data.drop(non_pro, axis=0)
data = data.reset_index(drop=True)

data = data.drop(non_lectin, axis=0)
data = data.reset_index(drop=True)

data = data.iloc[:, 1:]

protein_num, saccharide_num = data.shape
relations = []

for p_idx, row in data.iterrows():

    for s_idx, strength in enumerate(row):

        relations.append([
            f"P_{p_idx}",
            f"S_{s_idx}",
            strength
        ])

relations = pd.DataFrame(
    relations,
    columns=["Protein", "Saccharide", "Strength"]
)
glycan_repeat = pd.concat(
    [glycan] * protein_num,
    ignore_index=True
)

protein_repeat = np.repeat(
    protein_feature.values,
    saccharide_num,
    axis=0
)

protein_repeat = pd.DataFrame(protein_repeat)
dataset = pd.concat([
    relations,
    protein_repeat,
    glycan_repeat
], axis=1)

dataset = dataset.iloc[:, 2:]  # drop id columns

dataset = dataset.dropna()

dataset.to_csv(args.output, index=False)
