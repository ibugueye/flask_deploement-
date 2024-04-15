import requests

def test_index():
    url = "https://flask-deploement.onrender.com/"
    response = requests.get(url)
    print('Status Code:', response.status_code)
    print('Body:', response.text)

def test_get_ids():
    url = "https://flask-deploement.onrender.com/get_ids"
    response = requests.get(url)
    print('Status Code:', response.status_code)
    print('Body:', response.json())

def test_prediction():
    url = "https://flask-deploement.onrender.com/prediction"
    data = {'SK_ID_CURR': 100002}  # Assurez-vous que cet ID existe ou testez avec un ID approprié
    response = requests.post(url, json=data)
    print('Status Code:', response.status_code)
    print('Body:', response.json())

if __name__ == "__main__":
    print("Testing Index Route")
    test_index()
    print("\nTesting Get IDs Route")
    test_get_ids()
    print("\nTesting Prediction Route")
    test_prediction()
