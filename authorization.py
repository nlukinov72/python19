from cryptography.fernet import Fernet
from main import load_key


def authorization(login, password, fernet):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            line=line.rstrip()
            lgn,pwd = line.split("|")
            if lgn==login and fernet.decrypt(pwd.encode()).decode()==password:
                return True
    return False


def main():
    key=load_key()
    fernet = Fernet(key)
    while True:
        login=input("введите логин: ")
        password=input("введите пароль: ")
        if authorization(login, password, fernet):
            print("вы авторизованы")
            break 
        else:
            print("пользователь не найден")


if __name__ == "__main__":
    main()