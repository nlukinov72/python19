from cryptography.fernet import Fernet
import os


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
    return key


def add(fernet):
    login=input("введите логин: ")
    password=input("введите пароль: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{login}|{fernet.encrypt(password.encode()).decode()}\n")


def view(fernet):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            line=line.rstrip()
            login,password = line.split("|")
            print(f"логин: {login}, пароль: {fernet.decrypt(password.encode()).decode()} ")


def main():
    if not os.path.exists("key.key"):
        write_key()
    key=load_key()
    fernet = Fernet(key)
    while True:
        choise=input("хотите добавить новый пароль или посмотреть уже существующие 1. посмотреть , 2. добавить? нажмите 3 чтобы выйти")
        if choise== "1":
            view(fernet)
        elif choise== "2":
            add(fernet)
        elif choise== "3":
            break
        else:
            print("проверьте свой выбор")


if __name__ == "__main__":
    main()