import os
import sys
from login.login import User1
import tkinter
from tkinter import *
from tkinter import font, scrolledtext, ttk, filedialog, Tk, Canvas, messagebox
from PIL import Image, ImageTk
from structure.structure import TkinterTerminal, TimeKeeping, WeatherWidget
from DBSQLLITE import allnavigations, alllocations, restaurant_data, clubs_data
import re
import bcrypt
from datetime import datetime
import sqlite3

# dbconnect
conn = sqlite3.connect('SQL3DB.db')
mycursor = conn.cursor()

# for error purposes
User1.user1_img_uploaded = "Pictures/Anonymous.png"

class App:

    def __init__(self):
        #collecting the different terminals for the different days
        self.terminal_list = []
        #garbage collection
        self.day_background_photos = []
        #collecting the locations buttons generated so I can create a simultaneous SUNKEN relief on destinations buttons when hovering over navigations buttons
        self.loc_dict = {}
        #dictionary for the above mentioned funciton to convert navigation names to destination names
        self.desttonav_dict = self.desttonav()

        #App setup
        self.setup_root()
        self.setup_frames()
        self.show_start_frame()

        #user generation
        self.user1 = User1()

        #booleans and dynamic variables for different functionalities from the app methods
        self.current_frame = None
        self.current_user = None
        self.current_terminal = None
        self.terminal_first_msg_sent = False
        self.User_greeting = False

        self.day1terminal_first_msg_sent = False
        self.day2terminal_first_msg_sent = False
        self.day3terminal_first_msg_sent = False
        self.day4terminal_first_msg_sent = False



    #VIEW
    def setup_root(self):
        self.root = Tk()
        self.root.resizable(0, 0)
        self.root.geometry("1400x700")
        self.root.title("4 дни в Барселона")
        image_flag = PhotoImage(file="Pictures/img.png")
        self.root.iconphoto(True, image_flag)
        self.def_font = font.nametofont("TkDefaultFont")
        self.def_font.configure(family="Algerian",
                           size=25,
                           weight="bold")


    def setup_frames(self):
        self.start_frame = Frame(self.root, width=1400, height=700)
        self.elements_start_frame()

        self.app_frame = tkinter.Frame(self.root, width=1400, height=700)
        self.app_frame.pack_propagate(False)
        self.setup_background_app_frame()
        self.setup_elements_app_frame()

        self.profile_frame = Frame(self.root, width=1400, height=700)
        self.setup_elements_profile_frame()

        self.day1_frame = Frame(self.root)
        self.setup_day_frames("Pictures/day1.png", self.day1_frame, self.day1_locations(), self.day1_navigations())
        self.day2_frame = Frame(self.root)
        self.setup_day_frames("Pictures/day2.png", self.day2_frame, self.day2_locations(), self.day2_navigations())
        self.day3_frame = Frame(self.root)
        self.setup_day_frames("Pictures/day3.png", self.day3_frame, self.day3_locations(), self.day3_navigations())
        self.day4_frame = Frame(self.root)
        self.setup_day_frames("Pictures/day4.png", self.day4_frame, self.day4_locations(), self.day4_navigations())





    def elements_start_frame(self):
        self.custom_font = font.nametofont("TkDefaultFont")
        self.custom_font.configure(family="Algerian", size=25, weight="bold")
        tkinter.Label(self.start_frame,
                                      text="4 Days In Barcelona",
                                      font=self.custom_font).place(x=520, y=0)
        self.canvas_flag = Canvas(self.start_frame,
                             width=900,
                             height=600)
        self.canvas_flag.place(x=350, y=33)
        img = (Image.open("Pictures/img.png"))
        resized_image = img.resize((700, 400))
        self.new_image = ImageTk.PhotoImage(resized_image)
        self.canvas_flag.create_image(360, 250,
                                 image=self.new_image)

        Label(self.start_frame, text="Логин").place(x=650, y=490)

        self.username_label = Label(self.start_frame, text="Потребител:")
        self.username_label.place(x=347, y=532)
        self.username_entry_login = Entry(self.start_frame, font=("Arial", 20))
        self.username_entry_login.place(x=567, y=532)

        self.password_label = Label(self.start_frame, text="      Парола:", )
        self.password_label.place(x=370, y=570)
        self.password_entry_login = Entry(self.start_frame, font=("Arial", 20), show="*")
        self.password_entry_login.place(x=567, y=570)

        self.button_submit = Button(self.start_frame,
                               text="         Влез         ",
                               command=self.show_app_frame)
        self.button_submit.place(x=720, y=614)
        self.button_submit.bind("<Enter>", self.enter)
        self.button_submit.bind("<Leave>", self.leave)
        self.button_registration = Button(self.start_frame,
                                     text="Регистрация",
                                     command=lambda: self.show_register_frame(1))
        self.button_registration.place(x=450, y=614)
        self.button_registration.bind("<Enter>", self.enter)
        self.button_registration.bind("<Leave>", self.leave)
        self.messagelogin_label = Label(self.start_frame, text="", )
        self.messagelogin_label.place(x=890, y=547)



    def setup_background_app_frame(self):
        self.background_path = "Pictures/Barcelona.png"
        self.background_image = Image.open(self.background_path)
        self.frame_width = 1400
        self.frame_height = 700

        self.background_image = self.background_image.resize((self.frame_width, self.frame_height), Image.BICUBIC)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tkinter.Label(self.app_frame, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)


    def setup_elements_app_frame(self):
        self.app_terminal = TkinterTerminal(self.app_frame)
        self.red_square_image = tkinter.PhotoImage(width=20, height=20)
        self.red_square_image.put("red", to=(0, 0, 20, 20))
        self.locations = self.locations()

        for location_name, (x, y) in self.locations.items():
            red_dot_label = tkinter.Label(self.background_label, image=self.red_square_image, bg="gray")
            red_dot_label.image = self.red_square_image
            red_dot_label.config(relief=tkinter.RAISED)
            red_dot_label.place(x=x, y=y, anchor="center")

            red_dot_label.bind("<Enter>", self.enter)
            red_dot_label.bind("<Leave>", self.leave)
            red_dot_label.bind("<Button-1>", lambda event, loc=location_name: self.click_dot(loc))

        self.sunset_button = Button(self.app_frame, text="🌅", font=("Arial", 18), relief=RAISED, command=self.print_sunset)
        self.sunset_button.place(x=0, y=480)
        self.sunset_button.bind("<Enter>", self.enter)
        self.sunset_button.bind("<Leave>", self.leave)

        self.app_frame_back_button = tkinter.Button(self.app_frame,
                                               text="<-",
                                               font=("Algerian", 15),
                                               width=1, height=1,
                                               command=self.show_start_frame_back)
        self.app_frame_back_button.config(relief=tkinter.RAISED)
        self.app_frame_back_button.pack(side=tkinter.RIGHT, anchor=tkinter.NE)
        self.app_frame_back_button.bind("<Enter>", self.enter)
        self.app_frame_back_button.bind("<Leave>", self.leave)

        self.daybuttons_frame = Frame(self.app_frame)
        self.day1_button = tkinter.Button(self.daybuttons_frame,
                                          text="Ден 1",
                                          font=("Algerian", 15),
                                          width=5, height=1,
                                          command=self.day1)
        self.day1_button.config(relief=tkinter.RAISED)
        self.day1_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
        self.day1_button.bind("<Enter>", self.enter)
        self.day1_button.bind("<Leave>", self.leave)
        self.day2_button = tkinter.Button(self.daybuttons_frame,
                                          text="Ден 2",
                                          font=("Algerian", 15),
                                          width=5, height=1,
                                          command=self.day2)
        self.day2_button.config(relief=tkinter.RAISED)
        self.day2_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
        self.day2_button.bind("<Enter>", self.enter)
        self.day2_button.bind("<Leave>", self.leave)
        self.day3_button = tkinter.Button(self.daybuttons_frame,
                                          text="Ден 3",
                                          font=("Algerian", 15),
                                          width=5, height=1,
                                          command=self.day3)
        self.day3_button.config(relief=tkinter.RAISED)
        self.day3_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
        self.day3_button.bind("<Enter>", self.enter)
        self.day3_button.bind("<Leave>", self.leave)
        self.day4_button = tkinter.Button(self.daybuttons_frame,
                                          text="Ден 4",
                                          font=("Algerian", 15),
                                          width=5, height=1,
                                          command=self.day4)
        self.day4_button.config(relief=tkinter.RAISED)
        self.day4_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
        self.day4_button.bind("<Enter>", self.enter)
        self.day4_button.bind("<Leave>", self.leave)
        self.daybuttons_frame.place(x=0, y=90)


        self.clock = TimeKeeping(self.app_frame)
        self.weather = WeatherWidget(self.app_frame)

        self.restaurant_button = Button(self.app_frame, text="🍽 Ресторанти", font=("Arial", 15), command=self.show_restaurants_frame)
        self.restaurant_button.place(x=994, y=576)
        self.restaurant_button.bind("<Enter>", self.enter)
        self.restaurant_button.bind("<Leave>", self.leave)

        self.clubs_weedshops_button = Button(self.app_frame, text="(18+)🕺 Клубове и канабис", font=("Arial", 15),
                                        command=self.show_clubs_weedshops)
        self.clubs_weedshops_button.place(x=1144, y=576)
        self.clubs_weedshops_button.bind("<Enter>", self.enter)
        self.clubs_weedshops_button.bind("<Leave>", self.leave)

        self.profile_button = Button(self.app_frame, text="👤", font=("Arial", 27), relief=SUNKEN, command=self.show_profile_frame)
        self.profile_button.place(x=281, y=0)
        self.profile_button.bind("<Enter>", self.leave)
        self.profile_button.bind("<Leave>", self.enter)

    def setup_elements_profile_frame(self):
        mycursor.execute("select * from users")
        self.userinfo = []

        for x in mycursor:
            for y in x:
                self.userinfo.append(y)

        if len(self.userinfo) > 0:
            self.username, self.stored_hashed_password, self.email, self.birthdate, self.years, self.img_path = self.userinfo
            if not self.img_path:
                self.img_path = "Pictures/Anonymous.png"
        else:
            self.img_path = "Pictures/Anonymous.png"

        self.img_path = self.img_path
        self.pil_img = Image.open(self.img_path)
        self.pil_img = self.pil_img.resize((400, 400), Image.BICUBIC)
        self.img = ImageTk.PhotoImage(self.pil_img)
        self.img_reference = self.img

        self.picture_label = Label(self.profile_frame, image=self.img)
        self.picture_label.place(x=0, y=0)

        self.upload_button = ttk.Button(self.profile_frame, text="Качи снимка", command=self.upload_picture)
        self.upload_button.place(x=0, y=402)

        self.label1 = Label(self.profile_frame, text="Дневник:", font=("Arial", 20), relief="raised")
        self.label1.place(x=405, y=1)

        self.text_entry = scrolledtext.ScrolledText(self.profile_frame, wrap="word", width=75, height=25, font=("Arial", 17))
        self.text_entry.place(x=403, y=40)

        self.save_button = Button(self.profile_frame, text="Save", command=self.save_text, font=("Arial", 15))
        self.save_button.place(x=1310, y=0)
        self.save_button.bind("<Enter>", self.enter)
        self.save_button.bind("<Leave>", self.leave)

        self.status_label = Label(self.profile_frame, text="", font=("Arial", 15))
        self.status_label.place(x=1195, y=5)

        self.change_button = ttk.Button(self.profile_frame, text="Промени информация", command=lambda: self.show_register_frame(2))
        self.change_button.place(x=0, y=654)
        self.back_button_profile = tkinter.Button(self.profile_frame,
                                             text="<-",
                                             font=("Algerian", 15),
                                             width=1, height=1,
                                             command=self.back_to_app)
        self.back_button_profile.place(x=1380, y=0)
        self.back_button_profile.bind("<Enter>", self.enter)
        self.back_button_profile.bind("<Leave>", self.leave)


    def setup_day_frames(self, image, day_frame, loc_info, nav_info):
        day_background_image = Image.open(image)
        aspect_ratio = day_background_image.width / day_background_image.height
        frame_width = 1400
        frame_height = int(frame_width / aspect_ratio)
        day_background_image = day_background_image.resize((frame_width, frame_height), Image.BICUBIC)
        day_background_photo = ImageTk.PhotoImage(day_background_image)
        self.day_background_photos.append(day_background_photo)
        day_background_label = tkinter.Label(day_frame, image=day_background_photo)
        day_background_label.pack(side=tkinter.TOP, fill=tkinter.X)

        self.day_terminal = TkinterTerminal(day_frame, 1400, 10)
        self.terminal_list.append(self.day_terminal)
        self.day_back_button = tkinter.Button(day_frame,
                                               text="<-",
                                               font=("Algerian", 15),
                                               width=1, height=1,
                                               command=self.back_to_app)
        self.day_back_button.config(relief=tkinter.RAISED)
        self.day_back_button.place(x=1380, y=0)
        self.day_back_button.bind("<Enter>", self.enter)
        self.day_back_button.bind("<Leave>", self.leave)
        self.day_locations = loc_info
        for location_name, (x, y) in self.day_locations.items():
            red_dot_label = tkinter.Label(day_background_label, image=self.red_square_image, bg="gray")
            red_dot_label.image = self.red_square_image
            red_dot_label.config(relief=tkinter.RAISED)
            red_dot_label.place(x=x, y=y, anchor="center")

            red_dot_label.bind("<Enter>", self.enter)
            red_dot_label.bind("<Leave>", self.leave)
            red_dot_label.bind("<Button-1>", lambda event, loc=location_name: self.click_dot(loc))
            self.loc_dict[location_name] = red_dot_label

        self.day_navigations = nav_info

        if nav_info:
         for next_destination, (x, y) in self.day_navigations.items():
            navigation_label = tkinter.Label(day_background_label, text="V", bg="green", font=("Arial", 12))
            navigation_label.image = self.red_square_image
            navigation_label.config(relief=tkinter.RAISED)
            navigation_label.place(x=x, y=y, anchor="center")

            navigation_label.bind("<Enter>", lambda event, loc=next_destination: self.enter_nav(event, loc))
            navigation_label.bind("<Leave>", lambda event, loc=next_destination: self.leave_nav(event, loc))
            navigation_label.bind("<Button-1>", lambda event, loc=next_destination: self.click_navigation(loc))

    #CONTROLLER
    def show_start_frame(self):
        self.current_frame = self.start_frame
        self.start_frame.pack()
        self.app_frame.forget()

    def show_start_frame_back(self):
        answer = messagebox.askyesno("Потвърждение",
                                     "Сигурни ли сте, че искате да се върнете?\n Ще е нужен повторен логин.")
        if answer:
            self.current_frame = self.start_frame
            self.start_frame.pack()
            self.app_frame.forget()
        else:
            pass

    def show_register_frame(self, button_id):
        self.top_level = Toplevel(self.root, width=700, height=350)
        self.top_level.title("Регистрация")

        ttk.Label(self.top_level, text="Потребител:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.top_level, font=("Arial", 20))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.top_level, text="Парола:").grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = ttk.Entry(self.top_level, show="*", font=("Arial", 20))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.top_level, text="Повтори Парола:").grid(row=2, column=0, padx=10, pady=10)
        self.rep_password_entry = ttk.Entry(self.top_level, show="*", font=("Arial", 20))
        self.rep_password_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.top_level, text="Е-поща:").grid(row=3, column=0, padx=10, pady=10)
        self.email_entry = ttk.Entry(self.top_level, font=("Arial", 20))
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)
        ttk.Label(self.top_level, text="Рожденна дата:").grid(row=4, column=0, padx=10, pady=10)
        self.days = [f"{day:02d}" for day in range(1, 32)]
        self.day_var = StringVar(value="")
        self.day_dropdown = ttk.Combobox(self.top_level, textvariable=self.day_var, values=self.days, font=("Arial", 18), width=2)
        self.day_dropdown.place(x=300, y=260)
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        self.month_var = StringVar(value="")
        self.month_dropdown = ttk.Combobox(self.top_level, textvariable=self.month_var, values=self.months, font=("Arial", 18), width=9)
        self.month_dropdown.place(x=352, y=260)
        self.year_entry = Entry(self.top_level, width=5, font=("Arial", 18))
        self.year_entry.place(x=494, y=260)

        self.register_button = Button(self.top_level, text="Регистрация", command=lambda: self.register(button_id))
        self.register_button.grid(row=5, column=1, pady=10)
        self.register_button.bind("<Enter>", self.enter)
        self.register_button.bind("<Leave>", self.leave)

        self.message_label = Label(self.top_level, text="", font=("Arial", 10), height=3)
        self.message_label.grid(row=6, column=0, padx=10, pady=10)

    def show_app_frame(self):

        entered_username = self.username_entry_login.get()
        entered_password = self.password_entry_login.get()

        self.messagelogin_label.config(text="", font=("Arial", 20))

        self.current_frame = self.app_frame

        mycursor.execute("select * from users")
        userinfo_login = []
        for x in mycursor:
            for y in x:
                userinfo_login.append(y)

        username, stored_hashed_password, email, birthdate, years, img_path = userinfo_login
        stored_hashed_password = stored_hashed_password.encode('utf-8')
        entered_password = entered_password.encode('utf-8')

        if username == entered_username and bcrypt.checkpw(entered_password, stored_hashed_password):
            User1.Birthdate = birthdate
            self.user1.user1_img_uploaded = img_path
            self.user1.name = entered_username
            self.user1.years = years
            self.start_frame.forget()
            if not self.User_greeting:
                self.app_terminal.write(
                    f"Здравей, {self.user1.name}!\n")
                self.User_greeting = True
            if not self.terminal_first_msg_sent:
                self.app_terminal.write(
                    "Това е интерактивна карта на Барселона!Кликнете върху различните забележителности за повече информация за тях.\nИмате също предначертани маршрути за различните дни в дясно.\n")
                self.terminal_first_msg_sent = True
            self.app_frame.after(200, self.check_birthday)
            self.start_frame.forget()
            self.current_user = entered_username
            self.username_entry_login.delete(0, END)
            self.password_entry_login.delete(0, END)

        else:
            self.messagelogin_label.config(text="Невалиден потребител или парола!", font=("Arial", 20))


    def show_profile_frame(self):
        self.profile_frame.pack()
        self.start_frame.forget()
        self.app_frame.forget()
        self.day1_frame.forget()
        self.start_frame.forget()
        self.day2_frame.forget()
        self.day3_frame.forget()
        self.day4_frame.forget()
        self.update_profile_info()

        mycursor.execute("SELECT * FROM diary WHERE username = ?", (self.current_user,))
        diary = []
        for x in mycursor:
            for y in x:
                diary.append(y)

        if len(diary) > 0:
            diary_content = diary[1]
            self.text_entry.delete("1.0", END)
            self.text_entry.insert("1.0", diary_content)

    def show_restaurants_frame(self):
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        restaurants_window = Toplevel(self.root)
        restaurants_window.geometry("1200x525")

        canvas = Canvas(restaurants_window, width=1000, height=500, scrollregion=(0, 0, 2000, 500), bg="white")

        scrollbar = ttk.Scrollbar(restaurants_window, orient="horizontal", command=canvas.xview)
        scrollbar.pack(side="bottom", fill="x")

        canvas.config(xscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)

        scrollable_frame = Frame(canvas, bg="white")

        for index, restaurant_info in enumerate(restaurant_data):
            image_path = restaurant_info["image"]
            name = restaurant_info["name"]
            info = restaurant_info["info"]

            restaurant_image = PhotoImage(file=image_path).subsample(2)
            label = ttk.Label(scrollable_frame, image=restaurant_image, text=name, compound="top", style="TLabel",
                              font=("Arial", 17))
            label.image = restaurant_image
            label.grid(row=0, column=index, padx=10, pady=10)

            info_text = Text(scrollable_frame, wrap="word", height=10, width=80)
            info_text.insert("1.0", info)
            info_text.config(state="disabled")
            info_text.grid(row=1, column=index, pady=5)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.bind("<Configure>", on_configure)

    def show_clubs_weedshops(self):
        if int(self.user1.years) >= 18:
            clubs_weed_frame = Toplevel(self.root, width=700, height=350)
            clubs_weed_frame.title("Клубове и канабис")
            clubs_weed_frame.geometry("1200x525")

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            canvas = Canvas(clubs_weed_frame, width=1000, height=500, scrollregion=(0, 0, 2000, 500), bg="white")

            scrollbar = ttk.Scrollbar(clubs_weed_frame, orient="horizontal", command=canvas.xview)
            scrollbar.pack(side="bottom", fill="x")

            canvas.config(xscrollcommand=scrollbar.set)
            canvas.pack(side="left", fill="both", expand=True)

            scrollable_frame = Frame(canvas, bg="white")

            for index, clubs_info in enumerate(clubs_data):
                image_path = clubs_info["image"]
                name = clubs_info["name"]
                info = clubs_info["info"]

                pil_img = Image.open(image_path)

                width, height = 500, 300
                pil_img = pil_img.resize((width, height), Image.BICUBIC)

                clubs_image = ImageTk.PhotoImage(pil_img)
                label = ttk.Label(scrollable_frame, image=clubs_image, text=name, compound="top", style="TLabel",
                                  font=("Arial", 17))
                label.image = clubs_image
                label.grid(row=0, column=index, padx=10, pady=10)

                info_text = Text(scrollable_frame, wrap="word", height=10, width=80)
                info_text.insert("1.0", info)
                info_text.config(state="disabled")
                info_text.grid(row=1, column=index, pady=5)

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas.bind("<Configure>", on_configure)
        else:
            messagebox.showinfo("Грешка", "Трябва да имате навършени 18 години, за да отворите!")

    def day1(self):
        self.current_frame = self.day1_frame
        if len(self.terminal_list) > 0:
         self.current_terminal = self.terminal_list[0]
        self.day1_frame.pack()
        self.start_frame.forget()
        self.app_frame.forget()
        self.day2_frame.forget()
        self.day3_frame.forget()
        self.day4_frame.forget()
        if not self.day1terminal_first_msg_sent:
            self.current_terminal.write(
                "Това е маршрута за Ден 1.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n или да разгледате как да стигнете до тях като натиснете зелените бутони.\n")
            self.day1terminal_first_msg_sent = True

    def day2(self):
        self.current_frame = self.day2_frame
        if len(self.terminal_list) > 0:
         self.current_terminal = self.terminal_list[1]
        self.day2_frame.pack()
        self.start_frame.forget()
        self.app_frame.forget()
        self.day1_frame.forget()
        self.day3_frame.forget()
        self.day4_frame.forget()
        if not self.day2terminal_first_msg_sent:
            self.current_terminal.write(
                "Това е маршрута за Ден 2.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n или да разгледате как да стигнете до тях като натиснете зелените бутони.\n")
            self.day2terminal_first_msg_sent = True

    def day3(self):
        self.current_frame = self.day3_frame
        if len(self.terminal_list) > 0:
         self.current_terminal = self.terminal_list[2]
        self.day3_frame.pack()
        self.start_frame.forget()
        self.app_frame.forget()
        self.day2_frame.forget()
        self.day1_frame.forget()
        self.day4_frame.forget()
        if not self.day3terminal_first_msg_sent:
            self.current_terminal.write(
                "Това е маршрута за Ден 3.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n или да разгледате как да стигнете до тях като натиснете зелените бутони.\n")
            self.day3terminal_first_msg_sent = True

    def day4(self):
        self.current_frame = self.day4_frame
        if len(self.terminal_list) > 0:
         self.current_terminal = self.terminal_list[3]
        self.day4_frame.pack()
        self.start_frame.forget()
        self.app_frame.forget()
        self.day2_frame.forget()
        self.day3_frame.forget()
        self.day1_frame.forget()
        if not self.day4terminal_first_msg_sent:
            self.current_terminal.write(
                "Ден 4ти пътувате обратно следобяд.Можете да си изберете дестинация която искате да доразгледате, да се разходите из плажовете, да видите парк Ситаделата или да се възползвате от бус тур.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n")
            self.day4terminal_first_msg_sent = True

    def back_to_app(self):
        self.current_frame = self.app_frame
        self.app_frame.pack()
        self.day1_frame.forget()
        self.start_frame.forget()
        self.day2_frame.forget()
        self.day3_frame.forget()
        self.day4_frame.forget()
        self.profile_frame.forget()

    def check_birthday(self):
        if User1.Birthday == True:
            tkinter.Label(self.app_frame,
                          text=f"Happy Birthday, {self.user1.name}!",
                          font=self.def_font,
                          relief=RIDGE).place(x=73, y=120)
            if not self.user1.sent_message:
                self.app_terminal.write(f"Днес {self.user1.name} има рожден ден!\n")
                self.user1.sent_message = True
                self.app_frame.pack(fill=tkinter.BOTH, expand=True)
            else:
                self.app_frame.pack(fill=tkinter.BOTH, expand=True)
        else:
            self.app_frame.pack(fill=tkinter.BOTH, expand=True)


    def click_navigation(self, next_destination):
        for window in self.root.winfo_children():
            if isinstance(window, tkinter.Toplevel):
                window.destroy()
        new_window = tkinter.Toplevel()
        new_window.geometry("1200x600")
        new_window.title(next_destination)
        if allnavigations[next_destination][3] == None:
            image_path_nav, info_nav, terminal_message = allnavigations[next_destination][0], \
                                                         allnavigations[next_destination][1], \
                                                         allnavigations[next_destination][2]
            image = Image.open(image_path_nav)
            image = ImageTk.PhotoImage(image)

            image_label = tkinter.Label(new_window, image=image, width=800, height=400)
            image_label.image = image
            image_label.pack(anchor='n', pady=10)

            text_frame = tkinter.Frame(new_window, width=1200, height=200)
            text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)

            text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
            text_widget.tag_configure("custom_font", font=("Arial", 20))
            text_widget.insert(tkinter.END, info_nav, "custom_font")
            text_widget.pack(expand=True, fill="both")
        else:
            notebook = ttk.Notebook(new_window)
            tab1 = Frame(notebook)
            image_path_nav, info_nav, terminal_message = allnavigations[next_destination][0], \
                                                         allnavigations[next_destination][1], \
                                                         allnavigations[next_destination][2]
            image = Image.open(image_path_nav)
            image = ImageTk.PhotoImage(image)

            image_label = tkinter.Label(tab1, image=image, width=800, height=400)
            image_label.image = image
            image_label.pack(anchor='n', pady=10)

            text_frame = tkinter.Frame(tab1, width=1200, height=200)
            text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)

            text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
            text_widget.tag_configure("custom_font", font=("Arial", 20))
            text_widget.insert(tkinter.END, info_nav, "custom_font")
            text_widget.pack(expand=True, fill="both")

            tab2 = Frame(notebook)
            image_path_nav, info_nav, terminal_message, image_alt_transport = allnavigations[next_destination][0], \
                                                                              allnavigations[next_destination][1], \
                                                                              allnavigations[next_destination][2], \
                                                                              allnavigations[next_destination][3]

            image = Image.open(image_alt_transport)
            image = ImageTk.PhotoImage(image)

            image_label = tkinter.Label(tab2, image=image, width=1000, height=400)
            image_label.image = image
            image_label.pack(anchor='n', pady=10)

            text_frame = tkinter.Frame(tab2, width=1200, height=200)
            text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)

            text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
            text_widget.tag_configure("custom_font", font=("Arial", 20))
            text_widget.insert(tkinter.END, info_nav, "custom_font")
            text_widget.pack(expand=True, fill="both")
            style = ttk.Style()
            style.configure("TNotebook.Tab", font=("Arial", 15))
            notebook.add(tab1, text="Пеша                ")
            notebook.add(tab2, text="Градски Транспорт")
            notebook.pack(expand=True, fill="both")

        self.current_terminal.write(f"Вие разгледахте насоките {next_destination}\n")
        self.current_terminal.write(terminal_message)


    def click_dot(self, loc):
        for window in self.root.winfo_children():
            if isinstance(window, tkinter.Toplevel):
                window.destroy()
        new_window = tkinter.Toplevel()
        new_window.geometry("1200x600")
        new_window.title(loc)

        image_path, info = alllocations[loc][0], alllocations[loc][1]
        image = Image.open(image_path)
        image = ImageTk.PhotoImage(image)

        image_label = tkinter.Label(new_window, image=image, width=800, height=400)
        image_label.image = image
        image_label.pack(anchor='n', pady=10)

        text_frame = tkinter.Frame(new_window, width=1200, height=200)
        text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)

        text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
        text_widget.tag_configure("custom_font", font=("Arial", 15))
        text_widget.insert(tkinter.END, info, "custom_font")
        text_widget.pack(expand=True, fill="both")
        if self.current_frame == self.app_frame:
            self.app_terminal.write(f"Вие разгледахте {loc}\n")
        else:
            self.current_terminal.write(f"Вие разгледахте {loc}\n")

    def print_sunset(self):
        self.app_terminal.write(f"Залеза днес е в {self.weather.sunset_time}\n")

    def enter(self, event):
        event.widget.config(relief=tkinter.SUNKEN)

    def leave(self, event):
        event.widget.config(relief=tkinter.RAISED)

    def enter_nav(self, event, location):
        event.widget.config(relief=tkinter.SUNKEN)
        self.loc_dict[self.desttonav_dict[location]].config(relief=tkinter.SUNKEN)

    def leave_nav(self, event, location):
        event.widget.config(relief=tkinter.RAISED)
        self.loc_dict[self.desttonav_dict[location]].config(relief=tkinter.RAISED)

    #MODEL
    def register(self, button_id):
        self.message_label.config(text="")
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.rep_password = self.rep_password_entry.get()
        self.email = self.email_entry.get()
        self.day = self.day_var.get()
        self.month = self.month_var.get()
        self.year = self.year_entry.get()
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if self.day and self.month and self.year:
           self.birthdate = datetime.strptime(f"{self.month} {self.day} {self.year}", "%B %d %Y")
        self.current_date = datetime.now()
        if self.year:
            self.years_user = self.current_date.year - int(self.birthdate.year) - (
                    (self.current_date.month, self.current_date.day) < (self.birthdate.month, self.birthdate.day))
            self.birthday_string = str(f"{self.month} {self.day}")

        if len(self.username) > 18 or len(self.username) < 5:
            return self.message_label.config(text="Потребителското име трябва да е\nМинумум 5 символа,Максимум 18 символа!")
        if not (
                re.search(r'\d', self.password) and
                re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password) and
                re.search(r'[a-zA-Z]', self.password) and
                len(self.password) < 19
        ):
            return self.message_label.config(
                text="Паролата трябва да има 1 цифра,\n 1 специален символ и да е под 20 символа!")
        if not self.password == self.rep_password:
            return self.message_label.config(text="Паролита трябва да съвпадат в двете полета!")
        if not bool(re.fullmatch(self.email_pattern, self.email)):
            return self.message_label.config(text="Невалидна е-поща!")
        if not (isinstance(self.years_user, int) and 5 <= self.years_user <= 120):
            return self.message_label.config(text="Невалидни години!")

        self.hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        self.img_anonymous = "Pictures/Anonymous.png"
        mycursor.execute("DELETE FROM users")
        mycursor.execute(
            "INSERT INTO users (username, hashed_password, email, birthdate, years, img_path) VALUES (?, ?, ?, ?, ?, ?)",
            (self.username, self.hashed_password.decode('utf-8'), self.email, self.birthday_string, self.years_user,
             self.img_anonymous))
        conn.commit()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.rep_password_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.year_entry.delete(0, END)
        self.day_var.set("")
        self.month_var.set("")
        self.message_label.config(text="Регистрацията е успешна!", fg="green")

        mycursor.execute("DELETE FROM diary")
        conn.commit()

        if button_id == 2:
            python = sys.executable
            os.execl(python, python, *sys.argv)

    def save_text(self):
        self.entered_text = self.text_entry.get("1.0", END)

        mycursor.execute("UPDATE diary SET text = ? WHERE username = ?", (self.entered_text, self.current_user))
        if mycursor.rowcount == 0:
            mycursor.execute("INSERT INTO diary (username, text) VALUES (?, ?)", (self.current_user, self.entered_text))
        conn.commit()

        self.status_label.config(text="Запаметено")

    def upload_picture(self):
        self.file_path = filedialog.askopenfilename(title="Select an image",
                                               filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

        if self.file_path:
            pil_img = Image.open(self.file_path)
            pil_img = pil_img.resize((400, 400), Image.BICUBIC)
            img = ImageTk.PhotoImage(pil_img)

            self.picture_label.config(image=img)
            img_reference = img
            self.picture_label.image = img

        mycursor.execute("UPDATE users SET img_path = ? WHERE username = ?",
                         (self.file_path, self.current_user))
        conn.commit()

    def update_profile_info(self):
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

        label1 = Label(self.profile_frame, text="Потребителско име:", font=("Arial", 13), relief="raised")
        label1.place(x=0, y=450)
        label1_info = Label(self.profile_frame, text=f"{username}", font=("Arial", 13))
        label1_info.place(x=0, y=475)

        label2 = Label(self.profile_frame, text="Е-поща:                  ", font=("Arial", 13), relief="raised")
        label2.place(x=0, y=505)
        label2_info = Label(self.profile_frame, text=f"{email}", font=("Arial", 13))
        label2_info.place(x=0, y=530)

        label3 = Label(self.profile_frame, text="Рожденна дата:      ", font=("Arial", 13), relief="raised")
        label3.place(x=0, y=555)
        label3_info = Label(self.profile_frame, text=f"{birthdate}", font=("Arial", 13))
        label3_info.place(x=0, y=580)

        label4 = Label(self.profile_frame, text="Години:                  ", font=("Arial", 13), relief="raised")
        label4.place(x=0, y=605)
        label4_info = Label(self.profile_frame, text=f"{years}", font=("Arial", 13))
        label4_info.place(x=0, y=630)

    def desttonav(self):
        return {'към Аквариумът': 'Аквариумът на Барселона',
                  'към Ел Понт Моста': 'El Pont del Bisbe',
                  'към Катедралата': 'Катедралата на Барселона',
                  'към Пазарът': 'Mercado de La Boqueria',
                  'към Ла Рамбла и Площада': 'Ла Рамбла и Площада',
                  'към Палатът на музиката': 'Дворец на каталунската музика',
                  'към Саграда': 'Саграда Фамилия',
                  'към Гуел': 'Парк"Гуел"',
                  'Към Мол Арена': 'Мол Арена',
                  'към Лабиринта на Хорта': 'Парк"Лабиринт на Хорта"',
                  'към Къщите': 'Каса Висенс',
                  'към Монтжуик': 'Замък Монтжуик'
                  }

    def day1_locations(self):
        return {'Акта Атриум Хотел': (804, 136),
                'Аквариумът на Барселона': (1058, 489),
                'El Pont del Bisbe': (910, 335),
                'Катедралата на Барселона': (908, 306),
                'Mercado de La Boqueria': (824, 366),
                'Ла Рамбла и Площада': (788, 270),
                'Дворец на каталунската музика': (892, 218)
                }

    def day1_navigations(self):
        return {'към Аквариумът': (400, 158),
                'към Ел Понт Моста': (400, 222),
                'към Катедралата': (400, 291),
                'към Пазарът': (400, 356),
                'към Ла Рамбла и Площада': (400, 420),
                'към Палатът на музиката': (400, 489)
                }

    def day2_locations(self):
        return {'Акта Атриум Хотел': (1068, 349),
                'Саграда Фамилия': (1105, 179),
                'Парк"Гуел"': (888, 36),
                'Мол Арена': (855, 540)
                }

    def day2_navigations(self):
        return {'към Саграда': (400, 158),
                'към Гуел': (400, 222),
                'Към Мол Арена': (400, 291),
                }

    def day3_locations(self):
        return {'Акта Атриум Хотел': (945, 325),
                'Парк"Лабиринт на Хорта"': (828, 18),
                'Каса Падуа': (826, 235),
                'Каса Висенс': (852, 247),
                'Каса Мила': (905, 299),
                'Замък Монтжуик': (930, 492),
                }

    def day3_navigations(self):
        return {'към Лабиринта на Хорта': (400, 158),
                'към Къщите': (400, 222),
                'към Монтжуик': (400, 489)
                }

    def day4_locations(self):
        return {'Акта Атриум Хотел': (613, 205),
                'Плаж Сан Себастиан': (394, 505),
                'Парк Ситадела': (700, 386),
                'Готически Квартал': (510, 341),
                'Ла Рамбла': (517, 234),
                'Къщите': (621, 30),
                'Бус Турове': (781, 92),
                'Рецинте Модерниста': (947, 65),
                }

    def day4_navigations(self):
        pass

    def locations(self):
        return {'Парк"Лабиринт на Хорта"': (1365, 106),
                'Парк"Гуел"': (929, 159),
                'Каса Висенс': (689, 111),
                'Мол Арена': (290, 101),
                'Саграда Фамилия': (745, 445),
                'Ла Рамбла': (383, 340),
                'Замък Монтжуик': (56, 292),
                'Триумфална Арка': (607, 483),
                'Готически Квартал': (381, 465),
                'Парк Ситадела': (484, 586),
                'Аквариумът на Барселона': (227, 538)
                }


if __name__ == "__main__":
    app = App()
    app.root.mainloop()
