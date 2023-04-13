import requests
import json
import time

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
print (response.text)
p = response.json()

response1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=p)
print (response1.text)

s = response1.json()
sec = p["seconds"]

if s["status"] == "Job is NOT ready":
    time.sleep(sec)

response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=p)
s1 = response2.json()

if s1["status"] == "Job is ready":
    print (response2.text)
