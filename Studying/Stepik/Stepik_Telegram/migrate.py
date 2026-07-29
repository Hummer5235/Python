import aiosqlite
import asyncio

DB_PATH = "trash_report.db"  # имя файла БД

async def migrate():
    async with aiosqlite.connect(DB_PATH) as db:
        # Добавляем колонки
        await db.execute("ALTER TABLE trash_reports ADD COLUMN iso_year INTEGER")
        await db.execute("ALTER TABLE trash_reports ADD COLUMN iso_week INTEGER")

        # Уникальный индекс: один отчёт на пользователя в неделю
        await db.execute(
            """
            CREATE UNIQUE INDEX IF NOT EXISTS idx_user_iso_week
            ON trash_reports (user_id, iso_year, iso_week)
            """
        )
        await db.commit()
        print("Миграция завершена.")

if __name__ == "__main__":
    asyncio.run(migrate())
