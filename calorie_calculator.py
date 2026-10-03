
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "data/processed/final_nutrition_dataset.csv")


def calculate_calories(selected_row, mass, unit):
    """
    selected_row : dataframe row of selected food
    mass : float
    unit : 'g' or 'kg'
    """

    if mass < 0:
        raise ValueError("Mass must not be negative.")

    normalized_unit = unit.lower()
    if normalized_unit == "kg":
        mass = mass * 1000
    elif normalized_unit != "g":
        raise ValueError("Unit must be g or kg.")

    calories_per_100g = selected_row["Caloric Value"]
    total_calories = (calories_per_100g / 100) * mass

    return round(total_calories, 2)


# -------------------------------------
# FUNCTION FOR MAIN SYSTEM
# -------------------------------------

def run_calorie_calculator():

    print("\n--- Calorie Calculator ---")
    print("Type 'exit' to stop\n")

    while True:
        food = input("Enter food name: ").strip()

        if food.lower() == "exit":
            break

        # Search food
        matches = df[df["food"].str.lower().str.contains(food.lower(), na=False)]

        if matches.empty:
            print("Food not found in dataset.")
            print("-" * 40)
            continue

        # Show matches
        print("\nAvailable Matches:")
        for i, name in enumerate(matches["food"].values[:5]):
            print(f"{i + 1}. {name}")

        choice = input("\nSelect number (or type 0 to cancel): ")

        if not choice.isdigit():
            print("Invalid input.")
            print("-" * 40)
            continue

        choice = int(choice)

        if choice == 0:
            print("Cancelled.\n")
            continue

        if choice > len(matches[:5]):
            print("Invalid selection.")
            print("-" * 40)
            continue

        selected_row = matches.iloc[choice - 1]

        try:
            mass = float(input("Enter mass: "))
            unit = input("Enter unit (g/kg): ")
            total = calculate_calories(selected_row, mass, unit)
        except ValueError as exc:
            print(f"Invalid mass or unit: {exc}")
            print("-" * 40)
            continue

        print("\nEstimated Calories:", total)
        print("-" * 40)


# -------------------------------------
# Standalone Mode
# -------------------------------------

if __name__ == "__main__":
    run_calorie_calculator()