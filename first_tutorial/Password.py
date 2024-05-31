from cryptography.fernet import Fernet

master_pwd = input("What is your master's password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", passw)
        
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open ("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input ("Do u want to add a new password or view an existing one or quit. (view / add / q)").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add ()
    else:
        print("Invalid Mode")
        continue
