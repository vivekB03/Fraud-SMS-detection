import requests

url = "http://127.0.0.1:5000/test"
msg = "You won a lottery! Claim your prize now."
response = requests.get(url, params={"msg": msg})

if response.status_code == 200:
    data = response.json()

    print("Messsage:",data ["message"])
    print("prediction:",data ["predictiion"])
else:
    print("Error:",response.status_code,response.text)