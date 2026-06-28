import os
import dotenv


dotenv.load_dotenv()

print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))


# Важное примечание. Файл .env, если вы его храните внутри своего проекта,
# обязательно добавить в .gitignore, чтобы он не попал в репозиторий.