from ip2geotools.databases.noncommercial import DbIpCity

response = DbIpCity.get('188.170.85.34')
print(response.ip_address)
print(response.city)
print(response.country)
print(response.latitude)
print(response.longitude)
