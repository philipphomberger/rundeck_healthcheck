# !/usr/bin/python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys

#Get Helth Status Datasource Connnection
def health():
    global PROPERTIES
    global HEADERS
    url = URL + 'metrics/healthcheck'
    try:
        r = requests.get(url, headers=HEADERS, verify=False, timeout=PROPERTIES['TIMEOUT'])
        print(r.text)
    except:
        pass
        
#Get Helth StatusMetrics
def health2():
    global PROPERTIES
    global HEADERS
    url = URL + 'metrics/threads'
    try:
        r = requests.get(url, headers=HEADERS, verify=False, timeout=PROPERTIES['TIMEOUT'])
        print(r.text)
    except:
        pass

#Get Helth Pinng
def health3():
    global PROPERTIES
    global HEADERS
    url = URL + '/metrics/ping'
    try:
        r = requests.get(url, headers=HEADERS, verify=False, timeout=PROPERTIES['TIMEOUT'])
        print(r.text)
    except:
        pass
#
# Main
#
setting_filename = sys.argv[1] if len(sys.argv) > 1 else 'properties.json'
with open(setting_filename, 'r') as props_file:
    PROPERTIES = json.load(props_file)

protocol = 'http'
if PROPERTIES['SSL']:
    protocol = 'https'
    # disable warnings about unverified https connections
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

URL = '{0}://{1}:{2}/api/{3}/'.format(protocol, PROPERTIES['RUNDECKSERVER'], PROPERTIES['PORT'],
                                      PROPERTIES['API_VERSION'])
HEADERS = {'Content-Type': 'application/json', 'X-RunDeck-Auth-Token': PROPERTIES['API_KEY']}

health()
health2()
health3()
