import argparse
import pandas as pd


def get_type(sents: str):

    sac_list = []

    sub_sents = sents.split(",")

    for i in sub_sents:

        if ":" in i:
            sac_list.append(i.split(":")[0])

    return sac_list


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True, help="input txt file")
    parser.add_argument("--output", default="glycan.xlsx")

    args = parser.parse_args()

    with open(args.input, "r") as f:
        lines = f.readlines()

    # =========================
    # collect types
    # =========================
    single, double, trip = [], [], []

    for line in lines:

        parts = line.strip().split(";")

        if len(parts) < 2:
            continue

        if parts[0] == "single":
            single += get_type(parts[-1])

        elif parts[0] == "double":
            double += get_type(parts[-1])

        elif parts[0] == "trip":
            trip += get_type(parts[-1])

    single = sorted(list(set(single)))
    double = sorted(list(set(double)))
    trip = sorted(list(set(trip)))

    all_type = single + double + trip

    # =========================
    # build dict
    # =========================
    num_rows = len(lines) // 3 + 1

    sac_dict = {
        "id": [],
        "name": []
    }

    for t in all_type:
        sac_dict[t] = [0 for _ in range(num_rows)]

    row = -1
    j = 0

    for line in lines:

        parts = line.strip().split(";")

        if j % 3 == 0:
            row += 1

            sac_dict["id"].append(row + 1)

            sac_dict["name"].append(parts[1] if len(parts) > 1 else "")

        if len(parts) == 3 and parts[-1] != "":

            items = parts[-1].split(",")

            for n in items:

                if ":" in n:

                    key, val = n.split(":")

                    sac_dict[key][row] = int(val)

        j += 1

    df = pd.DataFrame(sac_dict)

    df.to_excel(
        args.output,
        sheet_name="count",
        index=False,
        na_rep="NULL"
    )

    print(f"Done! Saved to {args.output}")
    print(f"Shape: {df.shape}")


if __name__ == "__main__":
    main()
