from twilio.rest import Client
import requests

account_sid = 'AC8b55bdf6224e4068ae101008f8f222ea'
auth_token = '3d881f5f5288f40a57b25b96023b4079'
client = Client(account_sid, auth_token)

people = requests.get('http://api.open-notify.org/astros.json')
dic = people.json()
print("Status Code: ", people.status_code)
print("People in space = ", dic['number'])
names = dic['people']
print('Names are ')
namez = " "
for i in names:
    namez += str(i['name'])
    namez += ","

iss_loc = requests.get('http://api.open-notify.org//iss-now.json')    
loc = iss_loc.json()
position = loc['iss_position']
print("Status Code: ", iss_loc.status_code)
lat = str(position['latitude'])
long = str(position['longitude'])
print(position)

Message = 'NASA API TEST BY ZP.Number of people in space right now is ' + str(dic['number']) + "." + ' There names are: ' + namez + 'ISS Pos: Lat {}, Long {}'.format(lat,long)
print(Message)
#formulate the message that will be sent

message_nitin = client.messages.create(
    to= "+919971806234",
    from_="+18647272921",
    body=Message)   
message_papa = client.messages.create(
    to= "+919971355506",
    from_="+18647272921",
    body=Message) 
message_runa = client.messages.create(
    to= "+919999672846",
    from_="+18647272921",
    body=Message) 
message_jivi = client.messages.create(
    to= "+919816092658",
    from_="+18647272921",
    body=Message)    
message_guffy = client.messages.create(
    to= "+917814555255",
    from_="+18647272921",
    body=Message) 
message_tommy = client.messages.create(
    to= "+917042352818",
    from_="+18647272921",
    body=Message)    
message_puru = client.messages.create(
    to= "+919711102572",
    from_="+18647272921",
    body=Message)    
message_vidit = client.messages.create(
    to= "+919986700567",
    from_="+18647272921",
    body=Message)

message = client.messages.create(
    to= "+919531839038",
    from_="+18647272921",
    body=Message) 

print(message.sid,message_vidit.sid, message_puru.sid, message_nitin.sid, message_jivi.sid, message_guffy.sid, message_papa.sid, message_runa.sid, message_tommy.sid)