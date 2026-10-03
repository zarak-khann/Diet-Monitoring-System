# Project Brief — Diet Monitoring System

## 1. Project Overview

The Diet Monitoring System is a Python-based application designed to combine basic nutrition analysis and machine learning into a single system.

The application provides three primary capabilities:

1. Food category identification
2. Calorie estimation
3. Goal-based diet recommendations

The project is available through both a command-line interface and a Flask web application.

## 2. Problem Statement

People often need simple ways to understand the nutritional characteristics of food and organize their dietary choices.

This project explores how a software system can combine a nutrition dataset, machine-learning classification, calorie calculations, and recommendation logic into one application.

## 3. Main Components

### Food Classification

A Random Forest classifier is trained using nutritional features including calories, fat, protein, and carbohydrates.

The training pipeline performs:

* Dataset loading
* Feature selection
* Label encoding
* Stratified train/test splitting
* Feature scaling
* Model training
* Accuracy evaluation
* Model serialization

### Calorie Calculator

The calculator searches the nutrition dataset for a selected food and estimates the total calories according to the entered serving size.

### Diet Recommendation

The recommendation component provides diet suggestions based on the application's recommendation logic and user goals.

### Web Application

A Flask interface provides a browser-based way to interact with the system.

### Command-Line Interface

A CLI provides a simple menu for accessing the major system components.

## 4. Technology Stack

| Area                | Technology   |
| ------------------- | ------------ |
| Language            | Python       |
| Data Processing     | Pandas       |
| Machine Learning    | Scikit-learn |
| Model Serialization | Joblib       |
| Web Framework       | Flask        |
| Dataset             | CSV          |
| Interface           | CLI + Web    |

## 5. Machine Learning Approach

The food classifier uses a Random Forest model.

The current training pipeline uses:

* Random Forest
* StandardScaler
* LabelEncoder
* Stratified train/test split
* Accuracy evaluation

The resulting model, scaler, and encoder are saved as serialized files and loaded by the prediction component.

## 6. Architecture

```text
                 User
                  │
          ┌───────┴────────┐
          │                │
        CLI             Flask UI
          │                │
          └───────┬────────┘
                  │
        ┌─────────┼─────────┐
        │         │         │
     Food ID   Calories   Diet
        │         │      Recommender
        │         │         │
        └─────────┼─────────┘
                  │
          Nutrition Dataset
                  │
          ML Model Artifacts
```

## 7. Learning Objectives

The project was used to gain practical experience with:

* Python project organization
* Pandas data manipulation
* Machine-learning workflows
* Classification models
* Feature preprocessing
* Model evaluation
* Saving/loading trained models
* Flask applications
* Command-line applications
* Separating functionality into modules

## 8. Current Scope

The project is intentionally focused on practical implementation rather than production deployment.

It demonstrates how several independent programming and machine-learning components can be connected into a single application.

## 9. Future Direction

The system could eventually be expanded into a more personalized nutrition platform with:

* User profiles
* Diet history
* Personalized recommendations
* Daily calorie tracking
* Nutrition dashboards
* Larger datasets
* Improved food recognition
* Better recommendation algorithms
* Automated testing
* Cloud deployment

## 10. Project Status

**Status:** Working learning project

The repository contains the core dataset-processing, machine-learning, calorie-calculation, recommendation, CLI, and Flask application components.
