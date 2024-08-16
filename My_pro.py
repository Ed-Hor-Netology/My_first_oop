import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        User.users.append(self)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()

    def get_details(self):
        return f"Username: {self.username}, Email: {self.email}"

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        return f"Username: {self.username}, Email: {self.email}, Address: {self.address}"

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        return f"Username: {self.username}, Email: {self.email}, Admin Level: {self.admin_level}"
    
    def list_users(self, users):
        """
        Метод для вывода списка пользователей.
        """
        for user in users:
            print(user.get_details())

def delete_user(self, users, username):
    """
    Метод для удаления пользователя по его имени.
    """
    for user in users:
        if user.username == username:
            users.remove(user)
            print(f"User {username} has been deleted.")
            return
    print(f"User {username} not found.")

class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    def __init__(self):
        self.current_user = None

    def register(self, user_class, username, email, password, *args):
        new_user = user_class(username, email, password, *args)
        return new_user

    def login(self, username, password):
        for user in User.users:
            if user.username == username and user.check_password(user.password, password):
                self.current_user = user
                return True
        return False

    def logout(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user

# Пример использования
auth_service = AuthenticationService()