# Pharmaceutical Drug Spending Prediction
# Main Python file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print("Pharmaceutical Drug Spending ML Project")
print("Python environment is working successfully!")