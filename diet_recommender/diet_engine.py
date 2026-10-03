import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_dataset():
    df = pd.read_csv(BASE_DIR / "dataset.csv")
    return df


def filter_by_goal(df, goal):

    df = df[df["category"] != "Junk"].copy()

    if goal == "gain":

        df["score"] = (
            df["Caloric Value"] * 0.5 +
            df["Protein"] * 0.3 +
            df["Carbohydrates"] * 0.2
        )

    elif goal == "loss":

        df["score"] = (
            df["Protein"] * 0.5 +
            df["Dietary Fiber"] * 0.3 -
            df["Caloric Value"] * 0.2
        )

    else:   # maintain

        df["score"] = (
            df["Protein"] * 0.4 +
            df["Carbohydrates"] * 0.3 +
            df["Fat"] * 0.3
        )

    df = df.sort_values(by="score", ascending=False)

    return df