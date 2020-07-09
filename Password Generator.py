import random
pass_list = open("passwords.txt", "w+")
pass_list.close()
def random_pass():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!?"
    new_pass = ""
    for y in range(15):
        new_pass += characters[random.randrange(len(characters))]
    return new_pass

while(True):
    action = input("Generate Password or Search Password: ")
    if action == "Generate Password" or action == "Generate Passwords":
        amount = int(input("How Many Passwords? "))
        for x in range(amount):
            account = input("Which Account(Google,Netflix,Twitch, etc.): ")
            new_password = random_pass()
            print (account + ": " + new_password)
            with open("passwords.txt", "a+") as pass_list:
                pass_list.writelines(account + " " + new_password)
                pass_list.writelines("\n")
    elif action == "Search Password" or action == "Search Passwords":
        with open("passwords.txt", "r") as pass_list:
            account = input("Which Account(Google,Netflix,Twitch, etc.): ")
            password_list = pass_list.readlines()
            in_list = False
            for lines in password_list:
                if account == lines.split()[0]:
                    print (account + ": " + lines.split()[1])
                    in_list = True
            if not in_list:
                print ("password not found")
    elif action == "Clear Passwords":
        comfirmation = input("Are you sure you want to delete ALL your passwords?(yes/no) ")
        if comfirmation == "yes":
            with open("passwords.txt", "r+") as pass_list:
                pass_list.truncate(0)
    pass_list.close()
