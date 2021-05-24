import requests

people = requests.get('http://api.open-notify.org/astros.json')
dic = people.json()
print("Status Code: ", people.status_code)
print("People in space = ", dic['number'])
names = dic['people']
print('Names are ')
namez = " "
for i in names:
    namez += str(i['name']) 

print(namez)