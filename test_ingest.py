import requests
import time

url = "https://y1ymdn4gbf.execute-api.ap-south-1.amazonaws.com/default/ingest"

data = {
    "deviceId": "sensor-1",
    "temperature": 28.5,
    "humidity": 60,
    "timestamp": int(time.time())
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
