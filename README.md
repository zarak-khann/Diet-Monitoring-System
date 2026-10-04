# Diet Monitoring System

A Python-based diet monitoring application that combines **food classification, calorie estimation, and goal-based diet recommendations** into one system.

The project includes both a **command-line interface** and a **Flask web application**, with a machine-learning model trained to classify food categories from nutritional information.

## Features

* 🍎 Food category identification using a trained Random Forest classifier
* 🔢 Calorie estimation based on food and serving size
* 🥗 Goal-based diet recommendations
* 📊 Nutrition dataset processing and preparation
* 🤖 Machine-learning model training and evaluation
* 🌐 Flask-based web interface
* 💻 Command-line interface
* 💾 Saved model, scaler, and label-encoder artifacts

## How It Works

The system combines nutritional data, machine learning, and rule-based calculations:

```text
                    Diet Monitoring System
                            │
             ┌──────────────┴──────────────┐
             │                             │
        Command Line                  Flask Web App
             │                             │
             └──────────────┬──────────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
        Food Identifier          Calorie Calculator
              │                           │
              └─────────────┬─────────────┘
                            │
                    Diet Recommender
                            │
                    Nutrition Dataset
                            │
                    ML Model / Artifacts
```

### Food Classification

The food identifier uses nutritional features such as:

* Calories
* Fat
* Protein
* Carbohydrates

The features are scaled before being passed to a **Random Forest classifier**. Food categories are encoded using a `LabelEncoder`.

The trained artifacts are stored in:

```text
models/
├── food_model.pkl
├── scaler.pkl
└── label_encoder.pkl
```

### Calorie Calculator

The calorie calculator searches the nutrition dataset for a food item and estimates calories according to the entered serving mass.

Supported units:

```text
g
kg
```

The system converts kilograms to grams when necessary and calculates the estimated calories using the food's caloric value per 100 grams.

### Diet Recommender

The diet recommendation component provides recommendations based on the user's selected goal and relevant health calculations.

## Interfaces

### Command Line

Run:

```bash
python main_system.py
```

The CLI provides access to:

```text
1. Food Identifier
2. Calorie Calculator
3. Diet Recommender
```

### Web Application

Run:

```bash
python web_app/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

The web interface provides separate pages for the main diet-monitoring features.

## Machine Learning Pipeline

The food-classification model follows this general workflow:

```text
Nutrition Dataset
       ↓
Data Preparation
       ↓
Feature Selection
       ↓
Label Encoding
       ↓
Train/Test Split
       ↓
Feature Scaling
       ↓
Random Forest Training
       ↓
Model Evaluation
       ↓
Save Model Artifacts
```

The model is trained using **Scikit-learn's Random Forest classifier** with a stratified train/test split.

## Project Structure

```text
Diet-Monitoring-System/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── diet_recommender/
│   ├── app.py
│   ├── diet_engine.py
│   └── health_calculations.py
│
├── models/
│   ├── food_model.pkl
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│   └── README.md
│
├── src/
│   ├── calorei_estimator/
│   ├── diet_planner/
│   ├── food_classifier/
│   └── utils/
│
├── web_app/
│   ├── app.py
│   └── templates/
│
├── build_dataset.py
├── calorie_calculator.py
├── main.py
├── main_system.py
├── train_food_model.py
├── requirements.txt
├── PROJECT_BRIEF.md
└── README.md
```

## Technologies Used

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Core application development       |
| Pandas       | Dataset processing                 |
| Scikit-learn | Machine learning and preprocessing |
| Joblib       | Saving and loading model artifacts |
| Flask        | Web application                    |
| HTML/CSS     | Web interface                      |
| CSV          | Nutrition data storage             |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/zarak-khann/Diet-Monitoring-System.git
cd Diet-Monitoring-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Command-Line Application

```bash
python main_system.py
```

### Web Application

```bash
python web_app/app.py
```

Then visit:

```text
http://127.0.0.1:5000
```

## Rebuilding the Dataset and Model

If the dataset is modified, the project includes scripts for rebuilding the processed dataset and retraining the food-classification model.

Build the dataset:

```bash
python build_dataset.py
```

Train the model:

```bash
python train_food_model.py
```

The resulting model artifacts are saved in the `models/` directory.

## Project Purpose

This project was developed as a practical implementation of concepts in:

* Python programming
* Data processing
* Machine learning
* Classification
* Feature scaling
* Model evaluation
* Dataset preparation
* Flask web development
* Modular application design

The goal is to bring these concepts together into one practical diet-monitoring application.

## Limitations

This project is intended for **educational and demonstration purposes**.

The calorie estimates and diet recommendations should not be treated as professional medical or nutritional advice.

Model predictions depend on the quality and coverage of the available dataset. Real-world food composition and individual nutritional requirements can vary.

## Future Improvements

Possible future improvements include:

* User accounts and personal profiles
* Persistent diet history
* Daily calorie tracking
* Improved food recognition
* Larger and more diverse datasets
* More advanced recommendation models
* Personalized meal planning
* Nutrition dashboards and visualizations
* Automated testing
* Containerized deployment
* Improved web UI/UX

## Author

**Zarak Khan**

GitHub: [zarak-khann](https://github.com/zarak-khann)

---

> This project is a learning-focused implementation of machine-learning and software-development concepts rather than a production-grade medical or nutritional system.
