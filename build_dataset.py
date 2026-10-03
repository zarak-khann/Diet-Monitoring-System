import pandas as pd
import os

# Path to raw folder
raw_path = "data/raw"

# Columns we care about
required_columns = [
    "food",
    "Caloric Value",
    "Fat",
    "Saturated Fats",
    "Carbohydrates",
    "Sugars",
    "Protein",
    "Dietary Fiber",
    "Sodium"
]

all_dataframes = []

# Loop through all CSV files
for file in os.listdir(raw_path):
    if file.endswith(".csv"):
        print("Processing:", file)
        df = pd.read_csv(os.path.join(raw_path, file))

        # Drop unnamed columns
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        # Keep only required columns (if they exist)
        df = df[[col for col in required_columns if col in df.columns]]

        # Fill missing values with 0
        df = df.fillna(0)

        all_dataframes.append(df)

# Combine all datasets
combined_df = pd.concat(all_dataframes, ignore_index=True)

print("Combined Shape:", combined_df.shape)

# ---------------------------
# Apply labeling logic again
# ---------------------------
def classify(row):
    if row["Sugars"] > 15 or row["Saturated Fats"] > 5:
        return "Junk"
    elif row["Dietary Fiber"] > 5 and row["Sugars"] < 10:
        return "Healthy"
    else:
        return "Moderate"

combined_df["category"] = combined_df.apply(classify, axis=1)

# Save processed dataset
combined_df.to_csv("data/processed/final_nutrition_dataset.csv", index=False)

print("Final dataset saved successfully.")