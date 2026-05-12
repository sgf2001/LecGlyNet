import argparse
import os
import numpy as np
import pandas as pd

import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.metrics import roc_auc_score
from torch.utils.data import Dataset, DataLoader

# 导入模型
from model import GlycoproteinProphet

# =========================
# 参数
# =========================
parser = argparse.ArgumentParser()

parser.add_argument("--csv", type=str, default="MAD_dataset_12.csv")
parser.add_argument("--epochs", type=int, default=200)
parser.add_argument("--batch_size", type=int, default=128)
parser.add_argument("--lr", type=float, default=1e-3)
parser.add_argument("--save_dir", type=str, default="./weights")

args = parser.parse_args()

os.makedirs(args.save_dir, exist_ok=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# =========================
# 数据
# =========================
my_data = pd.read_csv(args.csv)

np.random.seed(42)

df_0 = my_data[my_data.iloc[:, 1] == 0]
df_1 = my_data[my_data.iloc[:, 1] == 1]

n_samples_per_class = round((len(df_1) / 10) * 9)

train_0 = df_0.sample(n=n_samples_per_class, random_state=42)
train_1 = df_1.sample(n=n_samples_per_class, random_state=42)

train_df = pd.concat([train_0, train_1])

test_df = my_data.drop(train_df.index)

X_train = train_df.iloc[:, 2:]
y_train = train_df.iloc[:, 1]

X_test = test_df.iloc[:, 2:]
y_test = test_df.iloc[:, 1]

# =========================
# Dataset
# =========================
class MyDataset(Dataset):

    def __init__(self, X, y):

        self.x_data = torch.tensor(
            X.values,
            dtype=torch.float32
        )

        self.y_data = torch.tensor(
            y.values,
            dtype=torch.float32
        )

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):

        return self.x_data[idx], self.y_data[idx]

train_dataset = MyDataset(X_train, y_train)
test_dataset = MyDataset(X_test, y_test)

train_loader = DataLoader(
    train_dataset,
    batch_size=args.batch_size,
    shuffle=True,
    num_workers=2
)

test_loader = DataLoader(
    test_dataset,
    batch_size=args.batch_size,
    shuffle=False,
    num_workers=2
)

# =========================
# 模型
# =========================
model = GlycoproteinProphet().to(device)

criterion = nn.BCELoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=args.lr
)

scheduler = optim.lr_scheduler.StepLR(
    optimizer,
    step_size=100,
    gamma=0.5
)

# =========================
# train
# =========================
best_auc = 0

for epoch in range(args.epochs):

    # =====================
    # train
    # =====================
    model.train()

    train_losses = []

    for inputs, labels in train_loader:

        inputs = inputs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(inputs)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        train_losses.append(loss.item())

    scheduler.step()

    # =====================
    # validation
    # =====================
    model.eval()

    val_probs = []
    val_labels = []

    with torch.no_grad():

        for inputs, labels in test_loader:

            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)

            val_probs.extend(outputs.cpu().numpy())
            val_labels.extend(labels.cpu().numpy())

    auc = roc_auc_score(
        val_labels,
        val_probs
    )

    # =====================
    # save best
    # =====================
    if auc > best_auc:

        best_auc = auc

        save_path = os.path.join(
            args.save_dir,
            "best_auc_model.pth"
        )

        torch.save(
            model.state_dict(),
            save_path
        )

        print(
            f"==> Save Best Model | "
            f"AUC={auc:.4f}"
        )

    print(
        f"Epoch [{epoch+1}/{args.epochs}] "
        f"Loss={np.mean(train_losses):.4f} "
        f"AUC={auc:.4f}"
    )

print(f"\nBest AUC: {best_auc:.4f}")
