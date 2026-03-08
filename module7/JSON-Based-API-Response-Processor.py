import json

# Step 1: Store JSON formatted string
api_response = '''
{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}
'''

try:
    # Step 2: Parse JSON string into Python object
    data = json.loads(api_response)

    # Step 3: Extract required fields
    request_id = data["id"]
    status = data["status"]
    text_result = data["result"]["text"]
    confidence = data["result"]["confidence"]

    # Print extracted data
    print("Request ID:", request_id)
    print("Status:", status)
    print("Text:", text_result)
    print("Confidence:", confidence)

    # Step 4: Check confidence score
    if confidence < 0.9:
        print("Warning: Confidence score is below 0.9")

    # Step 5: Create follow-up result dictionary
    follow_up = {
        "request_id": request_id,
        "status": status,
        "processed_text": text_result.upper(),
        "confidence": confidence
    }

    # Convert dictionary to JSON
    json_output = json.dumps(follow_up, indent=4)

    # Step 6: Write JSON to file
    with open("response.json", "w") as file:
        file.write(json_output)

    print("\nJSON response saved to response.json")

except json.JSONDecodeError:
    print("Error: Invalid JSON format")