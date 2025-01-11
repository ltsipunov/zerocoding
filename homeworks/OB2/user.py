class User:
    def __init__(self, user_id, name, access_level):
        self.__user_id = user_id  # Защищенный атрибут
        self.__name = name  # Защищенный атрибут
        self.__access_level = access_level  # Защищенный атрибут

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        if not access_level=='admin':
            print('Уровень доступа для админа может быть только admin (ставится по умолчанию, если пропущен ) ')
            return
        super().__init__(user_id, name, access_level)  # Вызов конструктора родительского класса
        self.__users = []  # Список пользователей, которым может управлять администратор

    def add_user(self, user):
        if isinstance(user, User):  # Проверка, что добавляемый объект является экземпляром User
            self.__users.append(user)
            print(f'Пользователь {user.get_name()} добавлен.')
        else:
            print('Нельзя добавить. Это не пользователь.')

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f'Пользователь {user.get_name()} удален.')
                return
        print('Пользователь не найден.')

    def list_users(self):
        print("Список пользователей:")
        for user in self.__users:
            print(f'ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}')