# Given list of scores
scores = [72, 45, 89, 30, 60]

# Iterate through the list
for score in scores:
    if score < 50:
        print("Fail")
        continue   # Skip further processing for failed scores
    else:
        print("Pass")