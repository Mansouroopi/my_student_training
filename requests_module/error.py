from urllib import response
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # if response was successfully, no exception will be raised
        response.raise_for_status()

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"Other error occurred: {err}")

    else:
        print('success!')