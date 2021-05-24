import requests

class Space_info():

    def __init__(self):
            
        iss_loc = requests.get('http://api.open-notify.org//iss-now.json')
        dic = iss_loc.json()
        position = dic['iss_position']
        print("Status Code: ", iss_loc.status_code)
        print(position)

Space_info()









