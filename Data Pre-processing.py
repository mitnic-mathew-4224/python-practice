import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from scipy.stats import zscore
from sklearn.feature_selection import VarianceThreshold

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 35, 45, 29],
    'Gender': ['F', 'M', 'M', np.nan, 'F'],
    'Income': [50000, 60000, 80000, 120000, np.nan],
    'Loan_Status': ['Y', 'N', 'Y', 'N', 'Y']
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# 1. Handling Missing Values
# Identify missing data
print("\nMissing Data Count:")
print(df.isnull().sum())

# Fill missing values
# Fill 'Age' with mean, 'Gender' with mode, and 'Income' with median
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Income'].fillna(df['Income'].median(), inplace=True)

print("\nData after Handling Missing Values:")
print(df)

# 2. Encoding Categorical Variables
# Label Encoding for Binary Classes
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # F = 0, M = 1
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])  # N = 0, Y = 1

print("\nData after Label Encoding:")
print(df)

# 3. Feature Scaling
# Standardization (Z-score)
scaler = StandardScaler()
df[['Age', 'Income']] = scaler.fit_transform(df[['Age', 'Income']])

print("\nData after Standardization (Z-score Scaling):")
print(df)

# 4. Outlier Detection and Treatment using Z-Score
z_scores = zscore(df[['Age', 'Income']])
outliers = (np.abs(z_scores) > 3).any(axis=1)
print("\nOutliers Detected:")
print(df[outliers])

# Treat outliers (e.g., cap them for 'Income' column)
df['Income'] = np.where(df['Income'] > 2.5, 2.5, df['Income'])  # Cap income values

print("\nData after Treating Outliers (Capping 'Income'):")
print(df)

# 5. Feature Selection (Optional) - Using Variance Threshold
selector = VarianceThreshold(threshold=0.1)
features = selector.fit_transform(df[['Age', 'Income', 'Gender']])
print("\nSelected Features after Variance Threshold (Optional):")
print(features)

# 6. Final Preprocessed Data
print("\nFinal Preprocessed Data:")
print(df)
