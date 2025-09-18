import pandas as pd
import numpy as np
import torch.nn as nn
import esm
import torch
import argparse
from sklearn.feature_selection import VarianceThreshold

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='esm2_t36_3B_UR50D')
#parser.add_argument('--number', type=int, default=731)
parser.add_argument('--layer', type=int, default=36)
parser.add_argument('--embedding', type=int, default=1)
parser.add_argument('--target',type=str,default=' lectin')
args = parser.parse_args()

# protein
model_path = f'esm.pretrained.{args.model}()'
model, alphabet = eval(model_path)
batch_converter = alphabet.get_batch_converter()
model.eval()
#number
protein = pd.read_csv('real_protein.csv')
non_lectin = [ 29,  40, 124, 144, 212, 213, 270, 277, 295, 319, 447, 490, 493, 500,
       506, 535, 543, 548, 573, 589, 597, 598, 611, 632, 636, 658, 659, 683,
       692, 695, 697, 702, 705, 706, 712]
protein_data = protein.drop(non_lectin, axis=0)
#data = data.reset_index(drop=True)
# random_rows = protein.sample(n=args.number, random_state=42)
# sample_protein = pd.DataFrame(random_rows)
seq = protein_data.iloc[:,0].tolist()
print(seq)
# #class
# protein = pd.read_csv('glycan_protein_716.csv',encoding='gbk')
# random_rows = protein[protein['Protein name'].str.contains(args.target)]
# print(random_rows.index)
# seq = random_rows.iloc[:,1].tolist()

chunk_size = 1
my_data =[]

for i in range(0, len(seq), chunk_size):
    sequences = seq[i:i + chunk_size]
    data_list = []
    for j in range(0,len(sequences)):
        data_list.append((1, sequences[j][:len(sequences[j])]))

    batch_labels, batch_strs, batch_tokens = batch_converter(data_list)#padding
    batch_lens = (batch_tokens != alphabet.padding_idx).sum(1)#real lens

    with torch.no_grad():
        results = model(batch_tokens, repr_layers=[args.layer], return_contacts=True)
    token_representations = results["representations"][args.layer]
    sequence_representations = []
    for i, tokens_len in enumerate(batch_lens):
        sequence_representations.append(token_representations[i, 1 : tokens_len - 1].mean(0))
    my_data.append(sequence_representations)
protein_all_data =[]
for i in my_data:
    for j in i:
        j =j.tolist()
        protein_all_data.append(j)
protein_data = np.array(protein_all_data)
protein_feature = pd.DataFrame(protein_data)

#glycan
glycan = pd.read_csv('glycan_feature_716_1.csv',header=None)
max_value = glycan.max().max()
glycan_data = glycan.values.tolist()
embedding = nn.Embedding(max_value +1,args.embedding)
input = torch.LongTensor(glycan_data)
e = embedding(input)
feature = []
for i in e:
    j = i.view(1,-1)
    feature.append(j)
my_feature =[]
for m in feature:
    n = m.tolist()
    for k in n:
        k = list(k)
        my_feature.append(k)
my_feature = np.array(my_feature)
glycan_feature = pd.DataFrame(my_feature)
# transfer = VarianceThreshold(threshold=1)
# glycan_feature = transfer.fit_transform(glycan_feature)
print(glycan_feature.shape)


#strength
zsorce_data = pd.read_csv('z_score_NA_716.csv')
non_pro = [713, 706, 634, 625, 605, 581, 560, 493, 449, 430, 313, 256, 172, 154, 149, 78, 52, 51, 0]
data = zsorce_data.drop(non_pro, axis=0)
data = data.reset_index(drop=True)
data = data.drop(non_lectin, axis=0)
data = data.reset_index(drop=True)
# x =random_rows.index
# data = data.iloc[random_rows.index]
rows_with_null = data[data.isnull().any(axis=1)]
#print(random_rows.index)
data = data.iloc[:,1:]
protein_num, saccharide_num = data.shape

relations = []
for protein_idx, row in data.iterrows():
    for sugar_idx, strength in enumerate(row):
        relations.append((f"Protein_{protein_idx + 1}", f"Sugar_{sugar_idx + 1}", strength))
relations = pd.DataFrame(relations, columns=['Protein', 'Saccharide', 'Strength'])


glycan_repeat = pd.concat([glycan] * protein_num, ignore_index=True)
protein_repeat = np.repeat(protein_feature.values, saccharide_num, axis=0)
protein_repeat = pd.DataFrame(protein_repeat, columns=protein_feature.columns)
pro_cho = pd.concat([relations, protein_repeat, glycan_repeat], axis=1)
pro_cho = pro_cho.iloc[:, 2:]
print(pro_cho.shape)
pro_cho = pro_cho.dropna()
print(pro_cho.shape)
pro_cho.to_csv('lectin_no_finger_1280.csv')

