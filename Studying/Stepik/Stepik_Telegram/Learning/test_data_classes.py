from dataclasses import dataclass
from typing import Any


@dataclass
class Book:
    title:str
    author:str


book_1 = Book('Мартин Иден','Джек Лондон')
book_2 = Book('Приключения майора Звягина', 'Михаил Веллер')


@dataclass
class BaseBook:
    title: Any = None
    author: str = None

@dataclass
class Book(BaseBook):
    desc: str = None
    title: str = "Unknown"

print(Book.title)
print(BaseBook.title)

print(BaseBook.__annotations__) # Получить словарь атрибутов