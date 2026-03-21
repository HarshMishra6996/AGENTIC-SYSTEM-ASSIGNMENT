# Answers

## 1. Role of Query Parameters

Query parameters are used to customize the API request.

In this task:
- q=python → searches repositories related to Python
- sort=stars → sorts repositories based on stars
- order=desc → sorts in descending order
- per_page=5 → limits results to 5 repositories

They help us filter and control the data returned by the API.

---

## 2. Why use response.json() instead of response.text?

response.json():
- Converts API response directly into Python dictionary
- Easy to access data using keys

response.text:
- Returns raw text (string)
- Harder to work with structured data

Therefore, response.json() is preferred for working with API data.