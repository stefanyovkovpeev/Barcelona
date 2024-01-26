from structure.structure import Player
from tkinter import *
from PIL import Image, ImageTk
import sqlite3



class User1(Player):

    def __init__(self):
        conn = sqlite3.connect('SQL3DB.db')
        mycursor = conn.cursor()
        mycursor.execute("select * from users")

        userinfo = []
        for x in mycursor:
            for y in x:
                userinfo.append(y)
        if len(userinfo) > 0:
            username, stored_hashed_password, email, birthdate, years, img_path = userinfo
            if not img_path:
                img_path = "Pictures/Anonymous.png"
        else:
            img_path = "Pictures/Anonymous.png"

        self.name = ""
        self.years = ""
        self.user1_img_uploaded = img_path
        self.user1_img = Image.open(self.user1_img_uploaded)
        self.user1_img = self.user1_img.resize((300, 300))
        self.user1_img = ImageTk.PhotoImage(self.user1_img)

    Birthdate = ""
    Birthday = False
    sent_message = False
    Hungry = False
    Tired = False

    def is_tired(self):
        self.Tired = False

    def is_hungry(self):
        self.Hungry = False

#commit