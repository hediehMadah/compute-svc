import requests
import time

url = "http://185.204.169.82:8080/compute"

while True:
    for i in range(1, 100):
        payload = {"n": i}
        response = requests.post(url, json=payload)
        print(f'Sent {payload}, received {response.json()}')
    time.sleep(10)  
