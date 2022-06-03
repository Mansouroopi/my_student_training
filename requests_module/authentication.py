import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
from getpass import getpass
from requests.auth import AuthBase
import json
from pprint import pprint


response = requests.post('https://api.weitizen.shop/api/login', auth=HTTPBasicAuth('buyer@example.com', getpass()) )



# class TokenAuth(AuthBase):
#     """Implements a custom authentication scheme."""

#     def __init__(self, token):
#         self.token = token

#     def __call__(self, r):
#         """Attach an API token to a custom auth header."""
#         r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
#         return r


# response = requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
# print(response)
# print(response.request.url)
