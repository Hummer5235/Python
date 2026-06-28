import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Users\\Lenovo\\Desktop\\Методички\\Online ДЗ"','"C:\\Users\\Lenovo\\Desktop\\Методички\\Roblox"']

# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Users\\Lenovo\\OneDrive'

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.

today = target_dir+ os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip - архива
now = time.strftime("%H%M%S")

# Создаем каталог, если его еще нет
if not os.path.exists(today):
	os.mkdir(today) # Создание каталога
	print("Каталог успешно создан", today)
# Имя zip файла
target = today + os.sep + now + ".zip"

# 5. Используем команду "zip" для помещения файлов в zip-архив
print("Пытаюсь поместить файлы в zip Архив")
zip_command = "zip -qr {0} {1}".format(target," ".join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
	print("Резервная копия успешно создана в",target)
	time.sleep(1)
	print("\nВыполняю запуск облака для синхронизации")
	os.system("C:\\Users\\Lenovo\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe")
else:
	print("Создание резервной копии НЕ УДАЛОСЬ")
