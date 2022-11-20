import pytest

def check_passwd(username, password, min_leght=8, check_username=True):
    if len(password) < min_leght:
        print('пароль слишком короткий')
        return False
