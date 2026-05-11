import argparse
import torch
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score
from model import GlycoproteinProphet


def main():
    parser = argparse.ArgumentParser(description="Run prediction with GlycoproteinProphet")
    parser.add_argument("--model_path", type=str, default="LecglyNet.pt", help="Path to trained model")
    parser.add_argument("--csv_path", type=str, default="sample.csv", help="Path to input CSV file")
    parser.add_argument("--output_path", type=str, default="LecglyNet_result.csv", help="Path to save result CSV")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    df = pd.read_csv(args.csv_path)

    labels = df.iloc[:, 1].values
    features = df.iloc[:, 2:].values

    X = torch.tensor(features, dtype=torch.float32).to(device)

    model = GlycoproteinProphet().to(device)
    model.load_state_dict(torch.load(args.model_path, map_location=device))
    model.eval()

    with torch.no_grad():
        outputs = model(X).squeeze()
        probs = torch.sigmoid(outputs).cpu().numpy()

    auc = roc_auc_score(labels, probs)
    print(f"\nAUC: {auc:.4f}")
    df["pred_prob"] = probs



    df.to_csv(args.output_path, index=False)
    print(f"Saved results to {args.output_path}")


if __name__ == "__main__":
    main()



