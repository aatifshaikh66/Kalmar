
import requests
from time import sleep

url = 'http://192.168.0.108:8000/'
query = "This is just a random data to test\n"

while True:
    sleep(1)
    try:
        print("Sending data")
        res = requests.post(url, data=query)   
        if res.ok:
            print(res.ok)
    except:
        print("error")