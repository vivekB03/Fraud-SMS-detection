import requests

url = "http://127.0.0.1:5000/test"

print("SMS Spam Detector (type 'exit' to quit)")

while True:
    msg = input("\nEnter SMS: ")
    if msg.lower() == "exit":
        print("Bye")
        break

    try:
        data = requests.get(url, params={"msg": msg}).json()
        print(f" Prediction: {data['prediction']}  |  Message: {data['message']}")
    except Exception as e:
        print("Request failed:", e)
