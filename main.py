import pytest

def check_passwd(username, password, min_leght=8, check_username=True):
    if len(password) < min_leght:
        print('пароль слишком короткий')
        return False
    elif check_username and username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
        
    def test_password_min_length():
        assert check_passwd('user', '12345', min_length=3) == True
        assert check_passwd('user', '123456', min_length=5) == False
        assert check_passwd('user', 'userpass', min_length=5) == False