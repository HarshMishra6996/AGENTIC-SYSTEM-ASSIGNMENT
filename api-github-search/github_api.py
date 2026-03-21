import requests

# API URL
url = "https://api.github.com/search/repositories"

# Parameters
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 5
}

# Send request
response = requests.get(url, params=params)

# Convert response to JSON
data = response.json()

# Print results
print("Top 5 Python Repositories:\n")

for repo in data["items"]:
    print(f"Name: {repo['name']}")
    print(f"Stars: {repo['stargazers_count']}")
    print("-" * 30)