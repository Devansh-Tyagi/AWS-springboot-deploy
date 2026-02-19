import requests
import time
import random

URL = "https://y1ymdn4gbf.execute-api.ap-south-1.amazonaws.com/default/ingest"

DEVICE_ID = "sensor-1"

while True:
    data = {
        "deviceId": DEVICE_ID,
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "timestamp": int(time.time())
    }

    try:
        response = requests.post(URL, json=data)
        print("Sent:", data, "| Status:", response.status_code)
    except Exception as e:
        print("Error:", e)

    # wait 3 seconds before next reading
    time.sleep(3)
