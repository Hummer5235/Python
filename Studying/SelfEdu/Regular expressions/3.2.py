import re
# with open('map.xml','r') as f:
# 	lon = []
# 	lat = []
# 	for text in f:
# 		match = re.findall(r'<point\s*lon\s*=\s*(?P<q>[\'"])(\d{2}[.]\d{4})(?P=q)\s+[^>]*lat\s*=\s*(?P<q2>[\'"])(\d+[.]\d+)(?P=q2)\s',text)
# 		print(match)
# 		if match:
# 			lon.append(match[0][1])
# 			lat.append(match[0][-1])
# print(lon)
# print(lat)



with open('map.xml','r') as f:
	lon = []
	lat = []
	for text in f:
		#Используем сохраняющие группы в регулярных выражениях
		match = re.search(r'<point\s*lon\s*=\s*(?P<q>[\'"])(?P<lon>\d+[.]\d+)(?P=q)\s+[^>]*lat\s*=\s*(?P<q2>[\'"])(?P<lat>\d+[.]\d+)(?P=q2)\s',text)
		print(match)
		if match:
			v = match.groupdict()
			if 'lon' in v and 'lat' in v:
				#В случае если изменится индекс элемента - это будет не важно, у нас доступ по ключу
				lon.append(v['lon'])
				lat.append(v['lat'])
print(lon)
print(lat)


