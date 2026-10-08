# Pharmaceutical Drug Spending Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def main():
    print("Pharmaceutical Drug Spending ML Project")
    print("Python environment is working successfully!")

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Ensemble": VotingRegressor([
            ("lr", LinearRegression()),
            ("rf", RandomForestRegressor(n_estimators=100, random_state=42))
        ])
    }

    print("Models included:")
    for model in models:
        print("-", model)


if __name__ == "__main__":
    main()