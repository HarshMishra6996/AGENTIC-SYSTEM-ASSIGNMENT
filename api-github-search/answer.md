# Conceptual Answers

## 1. What is the role of query parameters in this request?

Query parameters are used to customize the API request.

In this example:
- `q=python` → searches for repositories related to Python
- `sort=stars` → sorts the results based on the number of stars
- `order=desc` → arranges results in descending order
- `per_page=5` → limits the output to 5 repositories

They help us filter, sort, and control the data returned by the API.

---

## 2. Why do we use response.json() instead of response.text?

- `response.json()` converts the API response into a Python dictionary.
- This makes it easy to access specific data using keys (like `items`, `name`, `stargazers_count`).

On the other hand:
- `response.text` returns raw text (string format), which is harder to work with.

So, we use `response.json()` for structured and easy data handling.