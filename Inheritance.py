class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Геттеры и сеттеры для атрибутов
    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level

    # Сеттер для access_level не предоставлен, так как уровень доступа для обычного пользователя не должен изменяться.

    def __str__(self):
        return f"User ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Дополнительный уровень доступа для администратора

    def add_user(self, user_list, user):
        if user not in user_list:
            user_list.append(user)
            print(f"User {user.get_name()} added successfully.")
        else:
            print("User already exists.")

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f"User {user.get_name()} removed successfully.")
        else:
            print("User not found.")

    # Метод __str__ переопределен для отображения информации специфичной для администратора
    def __str__(self):
        return f"Admin ID: {self.get_user_id()}, Name: {self.get_name()}, Access Level: {self._access_level}"


# Пример использования
if __name__ == "__main__":
    user_list = []

    admin = Admin("01", "Alice")
    user1 = User("02", "Bob")
    user2 = User("03", "Charlie")

    print(admin)
    print(user1)

    admin.add_user(user_list, user1)
    admin.add_user(user_list, user2)
    admin.remove_user(user_list, user1)

    for user in user_list:
        print(user)