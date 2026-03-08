import pandas as pd
import numpy as np

# ---------------------------------
# 1. Create sample DataFrame
# ---------------------------------
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        60000, 58000, np.nan, 70000,
        52000, np.nan, 65000, 48000
    ],
    "Temporary_Notes": [
        "On probation", "Contract", "Pending docs", "Verified",
        "Intern", "New joiner", "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# ---------------------------------
# 2. Detect missing values
# ---------------------------------
print("\nMissing values in each column:")
print(df.isnull().sum())

# ---------------------------------
# 3. Fill missing Salary with mean
# ---------------------------------
salary_mean = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(salary_mean)

print("\nDataset after filling missing salaries:")
print(df)

# ---------------------------------
# 4. Drop Temporary_Notes column
# ---------------------------------
df = df.drop(columns=["Temporary_Notes"])

# ---------------------------------
# 5. Rename Salary column
# ---------------------------------
df = df.rename(columns={"Salary": "Annual_Salary"})

print("\nCleaned Dataset:")
print(df)

# ---------------------------------
# 6. Group by Department
# ---------------------------------
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

# ---------------------------------
# 7. Print summary
# ---------------------------------
print("\nDepartment Salary Summary:")
print(summary)