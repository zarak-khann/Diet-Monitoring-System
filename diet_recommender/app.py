from .diet_engine import load_dataset, filter_by_goal


from .health_calculations import (
    calculate_bmi,
    bmi_category,
    calculate_bmr,
    calculate_tdee,
    adjust_calories
)


def main():

    age = int(input("Age: "))
    gender = input("Gender (male/female): ")
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    activity = input("Activity (sedentary/light/moderate/active): ")
    goal = input("Goal (loss/gain/maintain): ")

    # BMI
    bmi = calculate_bmi(weight, height)

    category = bmi_category(bmi)

    print("\nBMI:", round(bmi, 2))
    print("Health Status:", category)

    # BMR
    bmr = calculate_bmr(weight, height, age, gender)

    # TDEE
    tdee = calculate_tdee(bmr, activity)

    # Target calories
    target_calories = adjust_calories(tdee, goal)

    print("Maintenance Calories (TDEE):", int(tdee))
    print("Target Calories:", int(target_calories))

    difference = target_calories - tdee

    if difference > 0:
        print("Calorie Surplus Needed:", int(difference), "kcal")
    elif difference < 0:
        print("Calorie Deficit Needed:", abs(int(difference)), "kcal")
    else:
        print("You are at maintenance calories.")

    df = load_dataset()

    recommended = filter_by_goal(df, goal)

    print("\nTop Recommended Foods:\n")
    print(recommended[["food", "Caloric Value", "Protein"]].head(10))


if __name__ == "__main__":
    main()