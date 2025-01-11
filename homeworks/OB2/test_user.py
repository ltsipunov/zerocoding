from user import User,Admin
#Создаем администраторов
admin = Admin(user_id=1, name="Алексей")

# Создаем пользователей
user1 = User(user_id=2, name="Иван", access_level="employee")
user2 = User(user_id=3, name="Мария", access_level="employee")
user3 = User(user_id=4, name="Акулина", access_level="employee")
user4 = User(user_id=5, name="Федора", access_level="employee")
user5 = User(user_id=6, name="Антон", access_level="employee")

print('проверка прямого чтения name')
user1.set_name('Пётр')
try:
    print(user1.__name)
except AttributeError as e :
    print('==============! ', e)
print('проверка прямой записи name')
try:
    user1.name='Тимофей'
except AttributeError as e :
    print('==============! ', e)
print(user1.get_name())

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)
admin.add_user(admin)

# Список пользователей
admin.list_users()
# Изменение уровня доступа
user4.set_access_level('admin')
user3.set_access_level('advanced')
# Администратор удаляет пользователя
admin.remove_user(2)

# Обновленный список пользователей
admin.list_users()