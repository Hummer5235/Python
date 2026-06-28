import ipinfo
import json

access_token = '1e3fc018849400'
handler = ipinfo.getHandler(access_token)
ip = '188.170.85.34'

details = handler.getDetails(ip)
print(details.loc)
# response = json.loads(str(details))
#
# city = response['city']
# region = response['region']
# country = response['country']
# latitude = response['loc'].split(',')[0]
# longitude = response['loc'].split(',')[1]
#
# print(city,latitude,longitude,sep = '\n')