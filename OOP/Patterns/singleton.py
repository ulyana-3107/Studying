# Singleton pattern : может быть создан только один экземпляр класса.


class DataBase:
    # __instance это ссылка на экземпляр класса, т.е. если экземпляр не создан, то __instance = None,
    # в противном случае - __instance будет хранить ссылку.
    __instance = None

    # в данном методе идет проверка, существует ли экземпляр у класса, если он существует, то вернется ссылка на него,
    # а в противном случае будет создан экземпляр и присвоен переменной__instance: cls.__instance = super().__new__(cls)
    # таким образом можно контролировать то, что существует ровно один объект данного класса.
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # финализатор создан для того, чтобы при удалении экземпляра класса переменная __instance снова стала None
    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connecting to DB: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('closing connection with DB')

    def read(self):
        print('data from DB')

    def write(self, data):
        print(f'writing in DB {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
# при попытке создать два экземпляра класса остался один, это можно проверить сравнив их id.
print(id(db) == id(db2))