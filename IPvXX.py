import json
import requests
import os
from requests import get

# Tested on Ubuntu Mate 20.04.1 LTS (Focal Fossa) 64-bit ; Kernel Linux 5.4.0-42-genericx86_64
# Tested with Python 3.8.2
# Test success

# https://www.myip.com/api-docs/
print("\n-----------------------------------INFORMATION GATHERED FROM MYIP.COM--------------------------")
parameters={"ip":"","country":"","cc":""}
response1=requests.get("https://api.myip.com",params=parameters)
#print(response1.status_code)
data1=response1.json()
# print(type(data1))
print("Information gathered from www.myip.com is\n",data1)
print("\n")

# https://www.ipify.org/
print("\n-----------------------------------INFORMATION GATHERED FROM IPIFY.COM--------------------------")
ipv4=get("https://api.ipify.org").text
ipv6=get("https://api6.ipify.org").text
print("My public IPv4 address is: {}".format(ipv4))
print("My public IPv4 address is: {}".format(ipv6))
print("\n")

# https://ip-api.com/docs/api:json
print("\n-----------------------------------INFORMATION GATHERED FROM IP-API.COM--------------------------")
os.system("curl ip-api.com\n")


# https://ipapi.co/
print("\n-----------------------------------INFORMATION GATHERED FROM IPAPI.CO--------------------------")
#os.system("curl https://ipapi.co/json")
ipapi1=("https://ipapi.co/"+ipv4+"/json/")
ipapi2=requests.get(ipapi1)
ipapi3=ipapi2.json()
for key in ipapi3:              # just to make lines prettier. We print line by line
    print(key,":",ipapi3[key])  # if not, it is hard to read
