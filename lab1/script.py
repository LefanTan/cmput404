import requests

print(requests.__version__)

res = requests.get('https://www.google.com')
print(res)
