import pandas as pd
import joblib
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load model files
model = joblib.load(BASE_DIR / "models" / "food_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")
encoder = joblib.load(BASE_DIR / "models" / "label_encoder.pkl")

# Load dataset
df = pd.read_csv(BASE_DIR / "data/processed/final_nutrition_dataset.csv")

def run_food_identifier():

    print("\n--- Food Identifier ---")
    print("Type 'exit' to stop\n")

    while True:

        food_name = input("Enter food name: ").strip()

        if food_name.lower() == "exit":
            break

        matches = df[df["food"].str.lower().str.contains(food_name.lower(), na=False)]

        if matches.empty:
            print("Food not found.\n")
            continue

        if len(matches) > 1:

            print("\nMatches:")
            for i, name in enumerate(matches["food"].values[:5]):
                print(f"{i+1}. {name}")

            choice = input("Select number: ")

            if choice.isdigit() and 1 <= int(choice) <= min(len(matches), 5):
                selected_row = matches.iloc[int(choice) - 1]
            else:
                print("Invalid selection. Please choose one of the displayed numbers.\n")
                continue

        else:
            selected_row = matches.iloc[0]

        features = pd.DataFrame([{
            "calories": selected_row["Caloric Value"],
            "fat": selected_row["Fat"],
            "protein": selected_row["Protein"],
            "carbohydrates": selected_row["Carbohydrates"],
        }])

        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)

        result = encoder.inverse_transform(prediction)[0]

        print("\nPredicted Category:", result)
        print("-"*40)



if __name__ == "__main__":
    run_food_identifier()