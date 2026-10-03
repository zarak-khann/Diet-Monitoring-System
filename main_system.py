def main():

    print("Welcome to Diet Monitoring System")

    print("\nChoose option:")
    print("1. Food Identifier")
    print("2. Calorie Calculator")
    print("3. Diet Recommender")

    choice = input("Enter option: ")

    if choice == "1":
        from src.food_classifier.predict import run_food_identifier
        run_food_identifier()

    elif choice == "2":
        from calorie_calculator import run_calorie_calculator
        run_calorie_calculator()

    elif choice == "3":
        from diet_recommender.app import main as run_diet_recommender
        run_diet_recommender()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()