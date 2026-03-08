import pandas as pd
import numpy as np

# -------------------------------
# 1. Create a sample dataset
# -------------------------------
np.random.seed(42)

data = {
    "Age": np.random.randint(18, 60, 20),
    "Score": np.random.randint(50, 100, 20),
    "Label": np.random.choice(["Pass", "Fail"], 20)
}

df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("sample_dataset.csv", index=False)

# -------------------------------
# 2. Load dataset
# -------------------------------
df = pd.read_csv("sample_dataset.csv")

# -------------------------------
# 3. Display dataset information
# -------------------------------
print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -------------------------------
# 4. Select single column
# -------------------------------
age_column = df["Age"]
print("\nSelected Age column:")
print(age_column.head())

# -------------------------------
# 5. Select multiple columns
# -------------------------------
selected_columns = df[["Age", "Score"]]
print("\nSelected Age and Score columns:")
print(selected_columns.head())

# -------------------------------
# 6. Filter rows based on condition
# -------------------------------
filtered_rows = df[df["Score"] > 80]

print("\nFiltered rows (Score > 80):")
print(filtered_rows)