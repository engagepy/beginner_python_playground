import requests
from collections import namedtuple
import time
import progressbar
  
widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
  
bar = progressbar.ProgressBar(max_value=20, 
                              widgets=widgets).start()
  
for i in range(20):
    time.sleep(0.1)
    bar.update(i)

WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
names = ['astratechz', 'multitechnoservices', 'northlandindia', 'nivaunited', 'andamandoorstep', 'hpdoorstep', 'livenit', ]
namesin = [ 'goandamans', 'multitechno','singhotels']

def get_status(site):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    try:
        response = requests.head(site, timeout=5, allow_redirects=True, headers=headers)
        #response = requests.head(site, timeout=5)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    website_status = WebsiteStatus(status_code, reason)
    return website_status

print("TESTING .COM WEBSITES NOW >>>> \n")
for name in names:
    for i in range(20):
        time.sleep(0.1)
        bar.update(i)
    site = 'http://{}.com'.format(name)
    website_status = get_status(site)
    print("{0:30} {1:10} {2:10}".format(site, website_status.status_code, website_status.reason))

print("\n TESTING .IN WEBSITES NOW >>>> \n") 
          
for namein in namesin:
    for i in range(20):
        time.sleep(0.01)
        bar.update(i)

    site = 'http://{}.in'.format(namein)
    website_status = get_status(site)
    print("{0:30} {1:10} {2:10}".format(site, website_status.status_code, website_status.reason))