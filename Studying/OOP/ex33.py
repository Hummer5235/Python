#33. Вложенные классы

class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self.user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)



    class Meta:
        ordering = ['id']
        def __init__(self, access):
            self._access = access

w = Women('root', '12345')
print('w.ordering: ', w.ordering)
print('w.Meta.ordering: ',w.Meta.ordering)
print(w.__dict__)