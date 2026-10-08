# Pharmaceutical Drug Spending Prediction

A machine learning project for predicting pharmaceutical drug spending using U.S. state drug utilization data.

## Project Overview

This project compares three machine learning models to predict the total amount reimbursed for pharmaceutical drugs:

1. Linear Regression
2. Random Forest
3. Ensemble Model

The project uses the U.S. State Drug Utilization Data 2024 dataset from HHS Official.

## Objectives

- Analyze pharmaceutical drug spending across U.S. states.
- Predict total drug spending using machine learning.
- Compare the performance of three machine learning models.
- Evaluate the models using MAE, MSE, and R².
- Understand patterns between drug utilization and spending.

## Dataset

**Dataset:** State Drug Utilization Data 2024  
**Source:** HHS Official

The dataset contains information such as:

- State
- Product Name
- Number of Prescriptions
- Units Reimbursed
- Year
- Quarter
- Total Amount Reimbursed

The full dataset is not included in this repository because of its large file size.

Dataset source:

https://huggingface.co/datasets/HHS-Official/state-drug-utilization-data-2024

## Machine Learning Models

### 1. Linear Regression

Linear Regression is used to find relationships between the input features and total drug spending.

### 2. Random Forest

Random Forest uses multiple decision trees to learn complex patterns in the data.

### 3. Ensemble Model

The Ensemble Model combines predictions from Linear Regression and Random Forest to improve prediction performance.

## Evaluation Metrics

The models are evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- VS Code
- GitHub

## Project Files

```text
drug-spending-ml/
│
├── united.ipynb
├── main.py
├── .gitignore
├── Proposal_Pharmaceutical_drug_spending.pdf
└── MD samim Rain.pdf
