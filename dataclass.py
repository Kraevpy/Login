class Login:

    default_name = 'Николай'
    default_password = '123'

    def __init__(self, name=default_name, password=default_password):
        self.name = name
        self.password = password

    @staticmethod
    def get_name() -> str:
        name = input('Введите свое имя для входа --> ')
        value_name = obj.compare_names(name)
        return value_name

    @staticmethod
    def get_password() -> str:
        password = input('Введите пороль для входа --> ')
        value_password = obj.password_check(password)
        return value_password

    def password_check(self, value_password) -> str:
        while value_password != self.default_password:
            print('Ошибка ввода пороля')
            return obj.get_password()
        else:
            return f'Добро пожаловать,теперь я уверен что это ты {self.default_name}'

    @staticmethod
    def case_conversion(value_name) -> str:
        if value_name.istitle():
            return value_name
        elif value_name[0].islower():
            return value_name.title()

    def compare_names(self, value_name) -> str:
        name_title = obj.case_conversion(value_name)
        if name_title == self.default_name:
            return f'Привет {name_title} рад тебя видеть '
        else:
            return f'Это не твой аккаунт {name_title}, а Николая'


obj = Login()
print(obj.get_name())
print(obj.get_password())
