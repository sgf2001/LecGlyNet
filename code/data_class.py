import argparse
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


def normal_distribution(x, c, mu, sigma):
    return c / (sigma * np.sqrt(2 * np.pi)) * np.exp(
        -(x - mu) ** 2 / (2 * sigma ** 2)
    )


def fit_sigma(data):

    y_hist, bin_edges = np.histogram(data, bins=100, density=False)
    x_hist = (bin_edges[:-1] + bin_edges[1:]) / 2

    p0 = [max(y_hist), np.mean(data), np.std(data)]

    params, _ = curve_fit(
        normal_distribution,
        x_hist,
        y_hist,
        p0=p0,
        bounds=(0, np.inf),
        maxfev=100000
    )

    c, mu, sigma = params

    return sigma


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="binary_matrix.csv")
    parser.add_argument("--k", type=float, default=12,
                        help="classification coefficient")

    args = parser.parse_args()

    df = pd.read_csv(args.input, header=None)

    result_matrix = []

    for i in range(df.shape[0]):

        row = df.iloc[i, :].values

        valid_mask = ~pd.isna(row)
        valid_data = row[valid_mask]

        sigma = fit_sigma(valid_data)

        threshold = args.k * sigma  
        row_binary = np.zeros(len(row))

        row_binary[valid_mask] = (
            valid_data > threshold
        ).astype(int)

        result_matrix.append(row_binary)

    result_matrix = np.array(result_matrix)

    pd.DataFrame(result_matrix).to_csv(
        args.output,
        index=False,
        header=False
    )


if __name__ == "__main__":
    main()
