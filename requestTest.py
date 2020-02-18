import requests

r = requests.get('https://www.baidu.com/')

if r.status_code == 200:
    print(r.text)