from http.client import responses
from urllib import response
import requests
#https://www.machinelearningplus.com/python/requests-in-python/

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print('SUCCESS')
    print(response.json()['current_user_url'])
elif response.status_code == 404:
    print('NOT FOUND')

if responses:
    print('SUCCESS')
else:
    print('FAILED')