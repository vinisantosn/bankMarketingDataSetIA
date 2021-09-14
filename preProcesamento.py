# Libraries
from builtins import print

import numpy as np
import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# from imblearn.over_sampling import SMOTE
# from imblearn.under_sampling import NearMiss
# import seaborn as sns

# File to be read
df = pd.read_csv('data/bank-full.csv', sep=';', header=0)

# Information
df.info()

# Print df
numeroDeLinhas = 10
print(df.head(numeroDeLinhas))

# Converting some object measurements to int64

df.education = df.education.map({"primary": 0, "secondary": 1, "tertiary": 2})
df["default"] = df["default"].map({"no": 0, "yes": 1})
df["housing"] = df["housing"].map({"no": 0, "yes": 1})
df["loan"] = df["loan"].map({"no": 0, "yes": 1})
df.contact = df.contact.map({"cellular": 0, "unknown": 1, "telephone": 2})
df.month = pd.to_datetime(df.month, format="%b").dt.month
df.poutcome = df.poutcome.map({"unknown": 0, "failure": 1, "other": 2, "success": 3})
df["y"] = df["y"].map({"no": 0, "yes": 1})

# Information
df.info()

# Check missing values
print(df.isnull().sum())
# Remove missing values
df.dropna(inplace=True)
print(df.head())

# Turning Categorical Columns into Numeric Columns
df = pd.get_dummies(df)
print(df.head().T)
