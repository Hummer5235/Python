import zipfile

# my_zip = zipfile.ZipFile("new.zip","w")

# my_zip.write("readme.txt")
# my_zip.write("road.jpg")

# my_zip.close()

# Использование контекстного менеджера

with zipfile.ZipFile("new.zip","w" , compression=zipfile.ZIP_DEFLATED) as my_zip:
	my_zip.write("readme.txt")
	my_zip.write("road.jpg")