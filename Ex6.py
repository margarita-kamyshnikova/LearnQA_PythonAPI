import requests

r = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
for response in r.history:
    print (response.url)