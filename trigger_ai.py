import requests

url = "http://127.0.0.1:8000/reports/ai"

data = {
    "incident_type": "Suspicious proximity",
    "description": "AI detected prolonged close interaction",
    "location": "Block B Corridor",
    "risk_level": "HIGH"
}

response = requests.post(url, json=data)

print("AI Trigger Sent")
print(response.json())