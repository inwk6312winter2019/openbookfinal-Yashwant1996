import create-ticket.py
import requests
import json
def GetToken():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    data = {}
    data['username'] = "devnetuser"
    data['password'] = "Cisco123!"
    data= json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data,headers=headers)
    return response.json()

print(GetToken())

import calc
for a in ipcalc.network('192.168.0.1/24'):
    print str(a)
    subnet = ipcalc.Network('255.255.255.0/24')
    print str(subnet.network())
print str(subnet.netmask())
    '192.168.0.1' in Network('192.168.0.1/24')
  def __str__(self):
          ipformat = ""
          for ips in self.ip:
              
