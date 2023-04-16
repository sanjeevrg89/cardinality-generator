import requests
from random import randint

url = "http://a6ebf1761fc9440cdbdabbf918e0db77-1311737121.us-west-2.elb.amazonaws.com/headers"  # Replace with the actual LoadBalancer IP or hostname

for _ in range(1000):
    headers = {
        "X-CUSTOM-TAG1": f"{randint(1, 100)}",
        "X-CUSTOM-TAG2": f"{randint(1, 100)}",
    }
    response = requests.get(url, headers=headers)
    print(response.json())