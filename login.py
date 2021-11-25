import pygame
from pygame import font
from tkinter import *
import tkinter.messagebox as tkMessageBox
import json
import pymysql
import constants as c



# db=pymysql.connect("localhost","ayushi","yourpassword","demo")
# cursor = db.cursor()
# query = f"select password from user where username = {USERNAME.get()}"
# try:
#     cursor.execute(query)
#     resultset = cursor.fetchall()
#     for record in resultset:
#         fname = record[0]
#         lname = record[1]
#         age = record[2]
#         enrolent_no = record[3]
#         print(f"Student: {fname} {lname}; Enrolment: {enrolment_no}; Age: {age}")
# except:
#     print("Sorry, we encountered a problem")

# https://data-flair.training/blogs/python-database-access/


#--  LOGIN THING  --#
#region Login

loggedIn = False

root = Tk()
root.title("Kesatria: Login Page")
 
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# def Database():
#     global conn, cursor
#     conn = sqlite3.connect("db_member.db")
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

#=======================================VARIABLES=====================================
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()

def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)
 
def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)

#=======================================METHODS=======================================
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
 
def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()
 
def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()

def crypt(thing2crypt, offset):
    not_crypted = thing2crypt
    chars = [ 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 
    'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 
    'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 
    'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '0', '1', '2', '3', '4', '5', 
    '6', '7', '8', '9' ]
    thing2crypt = list(thing2crypt)
    final = ""
    current = 0
    a = 0

    for i in range(len(thing2crypt)):
        if not thing2crypt[i] in chars:
            final += thing2crypt[i]
        for j in range(len(chars)):
            if thing2crypt[i] == chars[j]:
                if j + offset >= len(chars):
                    current = len(chars) - j
                    current = offset - current
                    a = 0 + current
                    final += chars[a]
                else:
                    final += chars[j + offset]
    print(f"From account [{USERNAME.get()}] : Crypted \"{not_crypted}\" in \"{final}\"")
    return final

def decrypt(thing2decrypt, offset):
    crypted = thing2decrypt
    chars = [ 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 
    'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 
    'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 
    'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '0', '1', '2', '3', '4', '5', 
    '6', '7', '8', '9' ]
    thing2decrypt = list(thing2decrypt)
    final = ""

    for i in range(len(thing2decrypt)):
        if not thing2decrypt[i] in chars:
            final += thing2decrypt[i]
        for j in range(len(chars)):
            if thing2decrypt[i] == chars[j]:
                if j - offset < 0:
                    final += chars[len(chars) + (j-offset)]
                else:
                    final += chars[j - offset]
    print(f"From account [{USERNAME.get()}] : Uncrypted \"{crypted}\" in \"{final}\"")
    return final

def get_accounts_data():
    try:
        with open("./accounts.json", "r") as account:
            users = json.load(account)
    except IOError:
        with open("./accounts.json", "w") as f:
            f.write("{}")
        with open("./accounts.json", "r") as account:
            users = json.load(account)
    return users

def open_account():
    users = get_accounts_data()

    # crypt

    crypted_password = crypt(PASSWORD.get(), 12)

    if USERNAME.get() in users:
        return False
    else:
        users[USERNAME.get()] = {}
        users[USERNAME.get()]["password"] = crypted_password
        users[USERNAME.get()]["persoFirstName"] = FIRSTNAME.get()
        users[USERNAME.get()]["persoLastName"] = LASTNAME.get()

        users[USERNAME.get()]["stats"] = {}
        users[USERNAME.get()]["stats"]["life"] = 1000
        users[USERNAME.get()]["stats"]["resistance"] = 50
        users[USERNAME.get()]["stats"]["determination"] = 50
        users[USERNAME.get()]["stats"]["magic"] = 50
        users[USERNAME.get()]["stats"]["gold"] = 0
        users[USERNAME.get()]["stats"]["damage"] = 50
        users[USERNAME.get()]["stats"]["level"] = 1
        users[USERNAME.get()]["stats"]["exp"] = 0

        users[USERNAME.get()]["weapons"] = {}
        users[USERNAME.get()]["weapons"]["Active Thorn"] = 0
        users[USERNAME.get()]["weapons"]["Non-Active Thorn"] = 0
        users[USERNAME.get()]["weapons"]["Wood Sword"] = 0
        users[USERNAME.get()]["weapons"]["Renforced Sword"] = 0
        users[USERNAME.get()]["weapons"]["Shadow Sword"] = 0
        users[USERNAME.get()]["weapons"]["Takeda Sword"] = 0
        users[USERNAME.get()]["weapons"]["Shinsu Sword"] = 0

        users[USERNAME.get()]["armor"] = {}
        users[USERNAME.get()]["armor"]["Wood Armor"] = 0
        users[USERNAME.get()]["armor"]["Renforced Armor"] = 0
        users[USERNAME.get()]["armor"]["Shadow Armor"] = 0
        users[USERNAME.get()]["armor"]["Takeda Armor"] = 0
        users[USERNAME.get()]["armor"]["Shinsu Armor"] = 0

    with open("./accounts.json", "w") as account:
        json.dump(users, account, indent = 4)
    return True

def Register():

    if USERNAME.get == "" or PASSWORD.get == "" or FIRSTNAME.get == "" or LASTNAME.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    elif (open_account() == True):
        lbl_result2.config(text="Successfully Created!", fg="black")
    elif (open_account() == False):
        lbl_result2.config(text="Username is already taken", fg="red")

def Login():
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    users = get_accounts_data()
    if USERNAME.get() in users:
        uncrypted_pass = decrypt(users[USERNAME.get()]["password"], 12)
        if PASSWORD.get() == uncrypted_pass:
            lbl_result1.config(text="You Successfully Login", fg="blue")
            root.destroy()

            FIRSTNAME = users[USERNAME.get()]["persoFirstName"]
            LASTNAME = users[USERNAME.get()]["persoLastName"]

            from userinit.player import player
            player.username = USERNAME.get()
            player.IGFirstName = FIRSTNAME
            player.IGLastName = LASTNAME

            player.life = users[USERNAME.get()]["stats"]["life"]
            player.resistance = users[USERNAME.get()]["stats"]["resistance"]
            player.determination = users[USERNAME.get()]["stats"]["determination"]
            player.magic = users[USERNAME.get()]["stats"]["magic"]
            player.gold = users[USERNAME.get()]["stats"]["gold"]
            player.damage = users[USERNAME.get()]["stats"]["damage"]
            player.level = users[USERNAME.get()]["stats"]["level"]
            player.exp = users[USERNAME.get()]["stats"]["exp"]

            player.active_thorn[1] = users[USERNAME.get()]["weapons"]["Activ Thorn"]
            player.non_active_THORN[1] = users[USERNAME.get()]["weapons"]["Non-Activ Thorn"]
            player.wood_sword[1] = users[USERNAME.get()]["weapons"]["Wood Sword"]
            player.renforced_sword[1] = users[USERNAME.get()]["weapons"]["Renforced Axe"]
            player.shadow_sword[1] = users[USERNAME.get()]["weapons"]["Shadow Sword"]
            player.takeda_sword[1] = users[USERNAME.get()]["weapons"]["Takeda Sword"]
            player.shinsu_sword[1] = users[USERNAME.get()]["weapons"]["Shinsu Sword"]

            player.wood_armor[1] = users[USERNAME.get()]["armor"]["Wood Armor"]
            player.renforced_armor[1] = users[USERNAME.get()]["armor"]["Renforced Armor"]
            player.shadow_armor[1] = users[USERNAME.get()]["armor"]["Shadow Armor"]
            player.takeda_armor[1] = users[USERNAME.get()]["armor"]["Takeda Armor"]
            player.shinsu_armor[1] = users[USERNAME.get()]["armor"]["Shinsu Armor"]
            
            import main as main
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
    else:
        lbl_result1.config(text="Invalid Username or password", fg="red")

LoginForm()
# Play()

#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()

#endregion Login