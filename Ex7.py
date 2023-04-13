import requests

list = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]

for element in list:
    resp = requests.get('https://playground.learnqa.ru/api/compare_query_type', params=element)
    print (f' GET \n {resp.text})')
for element in list:
    resp = requests.post('https://playground.learnqa.ru/api/compare_query_type', data=element)
    print (f' POST \n {resp.text})')
for element in list:
    resp = requests.put('https://playground.learnqa.ru/api/compare_query_type', data=element)
    print (f' PUT \n {resp.text})')
for element in list:
    resp = requests.delete('https://playground.learnqa.ru/api/compare_query_type', data=element)
    print (f' DELETE \n {resp.text})')