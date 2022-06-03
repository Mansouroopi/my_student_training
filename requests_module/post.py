import requests

# res = requests.post('https://httpbin.org/post', data=[('key', 'value')])
# print(res.json())

response = requests.post('https://httpbin.org/post', json={'username':'mansour', 'password': '123456'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])