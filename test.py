
import requests

# GET request
# res = requests.get("http://127.0.0.1:5000/api/cryptodata")
# print(res.json())


# PUT request
res = requests.put("http://127.0.0.1:5000/api/cryptodata", {"crypto-name": "bitcoin", "currency-name": "inr"})
print(res.json())