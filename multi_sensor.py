import requests
import time
import random
import threading

URL = "https://y1ymdn4gbf.execute-api.ap-south-1.amazonaws.com/default/ingest"

DEVICES = ["sensor-1", "sensor-2", "sensor-3", "sensor-4", "sensor-5"]


def send_data(device_id):
    while True:
        data = {
            "deviceId": device_id,
            "temperature": round(random.uniform(25, 35), 2),
            "humidity": round(random.uniform(40, 70), 2),
            "timestamp": int(time.time())
        }

        try:
            response = requests.post(URL, json=data)
            print(f"{device_id} → Status {response.status_code} | Temp {data['temperature']} | Hum {data['humidity']}")
        except Exception as e:
            print(f"{device_id} → Error:", e)

        time.sleep(random.randint(2, 5))  # different interval per device


# Start one thread per sensor
threads = []

for device in DEVICES:
    t = threading.Thread(target=send_data, args=(device,))
    t.start()
    threads.append(t)

# Keep program alive
for t in threads:
    t.join()
