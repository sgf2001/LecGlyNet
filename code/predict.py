import torch
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve, accuracy_score
from model import GlycoproteinProphet

# ================= 配置 ===============
model_path = "final_model_199.pt"     # 你的模型
csv_path = "datase_Cona.csv"       # 输入数据（第一列label）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ================= 1. 读取数据 =================
df = pd.read_csv(csv_path)
print(df.shape)

labels = df.iloc[:, 1].values
features = df.iloc[:, 2:].values

X = torch.tensor(features, dtype=torch.float32).to(device)

# ================= 2. 加载模型 =================
model = GlycoproteinProphet().to(device)
model.load_state_dict(torch.load(model_path, map_location=device))
model.eval()

# ================= 3. 推理 =================
with torch.no_grad():
    outputs = model(X).squeeze()
    probs = torch.sigmoid(outputs).cpu().numpy()

# ================= 4. 用 0.5 cutoff =================
preds_05 = (probs > 0.51).astype(int)

cm_05 = confusion_matrix(labels, preds_05)
tn, fp, fn, tp = cm_05.ravel()

print("====== 使用 0.5 cutoff ======")
print("Confusion Matrix:")
print(cm_05)

accuracy = (tp + tn) / (tp + tn + fp + fn)
sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
precision = tp / (tp + fp) if (tp + fp) > 0 else 0

print("\nMetrics:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Sensitivity (Recall): {sensitivity:.4f}")
print(f"Specificity: {specificity:.4f}")
print(f"Precision: {precision:.4f}")

# ================= 5. AUC =================
auc = roc_auc_score(labels, probs)
print(f"\nAUC: {auc:.4f}")

# ================= 6. 可选：1% FPR 阈值 =================
fpr, tpr, thresholds = roc_curve(labels, probs)
idx = np.argmin(np.abs(fpr - 0.01))
best_threshold = thresholds[idx]

preds_fpr = (probs > best_threshold).astype(int)
cm_fpr = confusion_matrix(labels, preds_fpr)

print("\n====== 使用 1% FPR threshold ======")
print(f"Threshold: {best_threshold:.6f}")
print("Confusion Matrix:")
print(cm_fpr)

# ================= 7. 保存结果 =================
df["pred_prob"] = probs
df["pred_label_0.5"] = preds_05
df["pred_label_fpr1%"] = preds_fpr

df.to_csv("pred_result.csv", index=False)

print("\n结果已保存到 pred_result.csv")
