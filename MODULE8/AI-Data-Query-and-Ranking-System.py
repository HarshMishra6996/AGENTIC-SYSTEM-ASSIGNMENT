# AI Data Query and Ranking System
# Author: Harsh Mishra
# --------------------------------

import pandas as pd

# --------------------------------
# 1. Create sample dataset
# --------------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 92, 78, 88, 91, 65],
    "Passed": [True, True, False, True, True, False],
    "Category": ["A", "A", "B", "B", "A", "C"]
}

df = pd.DataFrame(data)

print("\n--- Original Dataset ---")
print(df)


# --------------------------------
# 2. Select a single column
# --------------------------------
print("\n--- Single Column: Name ---")
print(df["Name"])


# --------------------------------
# 3. Select multiple columns
# --------------------------------
print("\n--- Multiple Columns (Name & Score) ---")
name_score_df = df[["Name", "Score"]]
print(name_score_df)


# --------------------------------
# 4. Use iloc (first 3 rows)
# --------------------------------
print("\n--- First 3 Rows using iloc ---")
print(df.iloc[:3])


# --------------------------------
# 5. Use loc after setting index
# --------------------------------
df_indexed = df.set_index("Name")

print("\n--- Using loc with index 'Alice' ---")
print(df_indexed.loc["Alice"])


# --------------------------------
# 6. Filter rows where Score > 85
# --------------------------------
print("\n--- Students with Score > 85 ---")
high_score = df[df["Score"] > 85]
print(high_score)


# --------------------------------
# 7. Filter Score > 85 AND Passed = True
# --------------------------------
print("\n--- Students with Score > 85 AND Passed = True ---")
passed_high = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(passed_high)


# --------------------------------
# 8. Sort filtered results (descending)
# --------------------------------
print("\n--- High-performing students (Sorted by Score) ---")
result = passed_high.sort_values(by="Score", ascending=False)
print(result[["Name", "Score"]])