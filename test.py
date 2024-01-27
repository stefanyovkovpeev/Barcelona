# import os
# import sys
# from login.login import User1
# import tkinter
# from tkinter import *
# from tkinter import font, scrolledtext, ttk, filedialog, Tk, Canvas, messagebox
# from PIL import Image, ImageTk
# from structure.structure import TkinterTerminal, TimeKeeping, WeatherWidget
# from DBSQLLITE import allnavigations, alllocations, restaurant_data, clubs_data
# import re
# import bcrypt
# from datetime import datetime
# import sqlite3
#
# # dbconnect
# conn = sqlite3.connect('SQL3DB.db')
# mycursor = conn.cursor()
#
# # for error purposes
# User1.user1_img_uploaded = "Pictures/Anonymous.png"
#
# # root and frame creation, function around them also
# root = Tk()
# root.resizable(0, 0)
# root.geometry("1400x700")
# root.title("4 дни в Барселона")
# image_flag = PhotoImage(file="Pictures/img.png")
# root.iconphoto(True, image_flag)
#
# font = font.nametofont("TkDefaultFont")
# font.configure(family="Algerian",
#                size=25,
#                weight="bold")
#
# start_frame = tkinter.Frame(root, width=1400, height=700)
# profile_frame = tkinter.Frame(root, width=1400, height=700)
# app_frame = tkinter.Frame(root, width=1400, height=700)
# app_frame.pack_propagate(False)
# background_path = "Pictures/Barcelona.png"
# background_image = Image.open(background_path)
# frame_width = 1400
# frame_height = 700
#
# background_image = background_image.resize((frame_width, frame_height), Image.BICUBIC)
# background_photo = ImageTk.PhotoImage(background_image)
#
# background_label = tkinter.Label(app_frame, image=background_photo)
# background_label.place(relwidth=1, relheight=1)
#
# current_frame = None
#
#
# def show_profile_frame():
#     profile_frame.pack()
#     start_frame.forget()
#     app_frame.forget()
#     day1_frame.forget()
#     start_frame.forget()
#     day2_frame.forget()
#     day3_frame.forget()
#     day4_frame.forget()
#     update_profile_info()
#
#     mycursor.execute("SELECT * FROM diary WHERE username = ?", (current_user,))
#     diary = []
#     for x in mycursor:
#         for y in x:
#             diary.append(y)
#
#     if len(diary)>0:
#       diary_content = diary[1]
#       text_entry.delete("1.0", END)
#       text_entry.insert("1.0", diary_content)
#
#
# def show_start_frame():
#     global current_frame
#     current_frame = start_frame
#     start_frame.pack()
#     app_frame.forget()
#
#
# def show_start_frame_back():
#     answer = messagebox.askyesno("Потвърждение",
#                                  "Сигурни ли сте, че искате да се върнете?\n Ще е нужен повторен логин.")
#     if answer:
#         global current_frame
#         current_frame = start_frame
#         start_frame.pack()
#         app_frame.forget()
#     else:
#         pass
#
#
# def enter(event):
#     event.widget.config(relief=tkinter.SUNKEN)
#
#
# def leave(event):
#     event.widget.config(relief=tkinter.RAISED)
#
#
# user1 = User1()
#
# terminal_first_msg_sent = False
# User_greeting = False
# current_user = None
#
#
# def show_app_frame():
#     def check_birthday():
#         if User1.Birthday == True:
#             tkinter.Label(app_frame,
#                           text=f"Happy Birthday, {user1.name}!",
#                           font=font,
#                           relief=RIDGE).place(x=73, y=120)
#             if not user1.sent_message:
#                 app_terminal.write(f"Днес {user1.name} има рожден ден!\n")
#                 user1.sent_message = True
#                 app_frame.pack(fill=tkinter.BOTH, expand=True)
#             else:
#                 app_frame.pack(fill=tkinter.BOTH, expand=True)
#         else:
#             app_frame.pack(fill=tkinter.BOTH, expand=True)
#
#     entered_username = username_entry_login.get()
#     entered_password = password_entry_login.get()
#
#     messagelogin_label.config(text="", font=("Arial", 20))
#
#     global current_frame
#     current_frame = app_frame
#
#     mycursor.execute("select * from users")
#     userinfo_login = []
#     for x in mycursor:
#         for y in x:
#             userinfo_login.append(y)
#
#     username, stored_hashed_password, email, birthdate, years, img_path = userinfo_login
#     stored_hashed_password = stored_hashed_password.encode('utf-8')
#     entered_password = entered_password.encode('utf-8')
#
#     if username == entered_username and bcrypt.checkpw(entered_password, stored_hashed_password):
#         User1.Birthdate = birthdate
#         user1.user1_img_uploaded = img_path
#         user1.name = entered_username
#         user1.years = years
#         global terminal_first_msg_sent
#         global User_greeting
#         start_frame.forget()
#         if not User_greeting:
#             app_terminal.write(
#                 f"Здравей, {user1.name}!\n")
#             User_greeting = True
#         if not terminal_first_msg_sent:
#             app_terminal.write(
#                 "Това е интерактивна карта на Барселона!Кликнете върху различните забележителности за повече информация за тях.\nИмате също предначертани маршрути за различните дни в дясно.\n")
#             terminal_first_msg_sent = True
#         app_frame.after(200, check_birthday)
#         start_frame.forget()
#         global current_user
#         current_user = entered_username
#         username_entry_login.delete(0, END)
#         password_entry_login.delete(0, END)
#
#     else:
#         messagelogin_label.config(text="Невалиден потребител или парола!", font=("Arial", 20))
#
#
# def back_to_app():
#     global current_frame
#     current_frame = app_frame
#     app_frame.pack()
#     day1_frame.forget()
#     start_frame.forget()
#     day2_frame.forget()
#     day3_frame.forget()
#     day4_frame.forget()
#     profile_frame.forget()
#
#
# # BYPASS LOGIN PROCEDURE
# # def show_app_frame():
# #     def check_birthday():
# #         if User1.Birthday == True:
# #             tkinter.Label(app_frame,
# #                           text=f"Happy Birthday, {user1.name}!",
# #                           font=font,
# #                           relief=RIDGE).place(x=73, y=76)
# #             if not user1.sent_message:
# #                 app_terminal.write(f"Днес {user1.name} има рожден ден!\n")
# #                 font.configure(family="Algerian",
# #                                size=20,
# #                                weight="bold")
# #                 user1.sent_message = True
# #                 app_frame.pack(fill=tkinter.BOTH, expand=True)
# #             else:
# #                 app_frame.pack(fill=tkinter.BOTH, expand=True)
# #         else:
# #             app_frame.pack(fill=tkinter.BOTH, expand=True)
# #
# #     global current_frame
# #     current_frame = app_frame
# #     global terminal_first_msg_sent
# #     global User_greeting
# #     with open("user_info.txt", "r") as file:
# #         for line in file:
# #             username, stored_hashed_password, email, birthdate, years, img_path = line.strip().split(',')
# #             user1.name = username
# #             User1.Birthdate = birthdate
# #             user1.user1_img_uploaded = img_path
# #             user1.years = years
# #     if not User_greeting:
# #         app_terminal.write(
# #             f"Здравей, {user1.name}!\n")
# #         User_greeting = True
# #         if not terminal_first_msg_sent:
# #             app_terminal.write(
# #                 "Това е интерактивна карта на Барселона!Кликнете върху различните забележителности за повече информация за тях.\nИмате също предначертани маршрути за различните дни в дясно.\n")
# #             terminal_first_msg_sent = True
# #     app_frame.after(200, check_birthday)
# #     start_frame.forget()
#
#
# # login_frame
# def register(button_id):
#     message_label.config(text="")
#     username = username_entry.get()
#     password = password_entry.get()
#     rep_password = rep_password_entry.get()
#     email = email_entry.get()
#     day = day_var.get()
#     month = month_var.get()
#     year = year_entry.get()
#     email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
#     birthdate = datetime.strptime(f"{month} {day} {year}", "%B %d %Y")
#     current_date = datetime.now()
#     if year:
#         years_user = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
#         birthday_string = str(f"{month} {day}")
#
#     if len(username) > 18 or len(username) < 5:
#         return message_label.config(text="Потребителското име трябва да е\nМинумум 5 символа,Максимум 18 символа!")
#     if not (
#             re.search(r'\d', password) and
#             re.search(r'[!@#$%^&*(),.?":{}|<>]', password) and
#             re.search(r'[a-zA-Z]', password) and
#             len(password) < 19
#     ):
#         return message_label.config(text="Паролата трябва да има 1 цифра,\n 1 специален символ и да е под 20 символа!")
#     if not password == rep_password:
#         return message_label.config(text="Паролита трябва да съвпадат в двете полета!")
#     if not bool(re.fullmatch(email_pattern, email)):
#         return message_label.config(text="Невалидна е-поща!")
#     if not (isinstance(years_user, int) and 5 <= years_user <= 120):
#         return message_label.config(text="Невалидни години!")
#
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#     img_anonymous = "Pictures/Anonymous.png"
#     mycursor.execute("DELETE FROM users")
#     mycursor.execute(
#         "INSERT INTO users (username, hashed_password, email, birthdate, years, img_path) VALUES (?, ?, ?, ?, ?, ?)",
#         (username, hashed_password.decode('utf-8'), email, birthday_string, years_user, img_anonymous))
#     conn.commit()
#
#     username_entry.delete(0, END)
#     password_entry.delete(0, END)
#     rep_password_entry.delete(0, END)
#     email_entry.delete(0, END)
#     year_entry.delete(0, END)
#     day_var.set("")
#     month_var.set("")
#     message_label.config(text="Регистрацията е успешна!", fg="green")
#
#     mycursor.execute("DELETE FROM diary")
#     conn.commit()
#
#     if button_id == 2:
#         python = sys.executable
#         os.execl(python, python, *sys.argv)
#
#
# def show_register_frame(button_id):
#     top_level = Toplevel(root, width=700, height=350)
#     top_level.title("Регистрация")
#
#     ttk.Label(top_level, text="Потребител:").grid(row=0, column=0, padx=10, pady=10)
#     global username_entry
#     username_entry = ttk.Entry(top_level, font=("Arial", 20))
#     username_entry.grid(row=0, column=1, padx=10, pady=10)
#
#     ttk.Label(top_level, text="Парола:").grid(row=1, column=0, padx=10, pady=10)
#     global password_entry
#
#     password_entry = ttk.Entry(top_level, show="*", font=("Arial", 20))
#     password_entry.grid(row=1, column=1, padx=10, pady=10)
#
#     ttk.Label(top_level, text="Повтори Парола:").grid(row=2, column=0, padx=10, pady=10)
#     global rep_password_entry
#     rep_password_entry = ttk.Entry(top_level, show="*", font=("Arial", 20))
#     rep_password_entry.grid(row=2, column=1, padx=10, pady=10)
#
#     ttk.Label(top_level, text="Е-поща:").grid(row=3, column=0, padx=10, pady=10)
#     global email_entry
#     email_entry = ttk.Entry(top_level, font=("Arial", 20))
#     email_entry.grid(row=3, column=1, padx=10, pady=10)
#     global day_var, month_var, year_entry
#     ttk.Label(top_level, text="Рожденна дата:").grid(row=4, column=0, padx=10, pady=10)
#     days = [f"{day:02d}" for day in range(1, 32)]
#     day_var = StringVar(value="")
#     day_dropdown = ttk.Combobox(top_level, textvariable=day_var, values=days, font=("Arial", 18), width=2)
#     day_dropdown.place(x=300, y=260)
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
#               "November", "December"]
#     month_var = StringVar(value="")
#     month_dropdown = ttk.Combobox(top_level, textvariable=month_var, values=months, font=("Arial", 18), width=9)
#     month_dropdown.place(x=352, y=260)
#     year_entry = Entry(top_level, width=5, font=("Arial", 18))
#     year_entry.place(x=494, y=260)
#
#     register_button = Button(top_level, text="Регистрация", command=lambda: register(button_id))
#     register_button.grid(row=5, column=1, pady=10)
#     register_button.bind("<Enter>", enter)
#     register_button.bind("<Leave>", leave)
#
#     global message_label
#     message_label = Label(top_level, text="", font=("Arial", 10), height=3)
#     message_label.grid(row=6, column=0, padx=10, pady=10)
#
#
# # login frame code end
# # profile frame
# def save_text():
#     entered_text = text_entry.get("1.0", END)
#
#     mycursor.execute("UPDATE diary SET text = ? WHERE username = ?", (entered_text, current_user))
#     if mycursor.rowcount == 0:
#         mycursor.execute("INSERT INTO diary (username, text) VALUES (?, ?)", (current_user, entered_text))
#     conn.commit()
#
#     status_label.config(text="Запаметено")
#
#
# def upload_picture():
#     file_path = filedialog.askopenfilename(title="Select an image",
#                                            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
#
#     if file_path:
#         pil_img = Image.open(file_path)
#         pil_img = pil_img.resize((400, 400), Image.BICUBIC)
#         img = ImageTk.PhotoImage(pil_img)
#
#         picture_label.config(image=img)
#         img_reference = img
#         picture_label.image = img
#
#     mycursor.execute("UPDATE users SET img_path = ? WHERE username = ?",
#                      (file_path, current_user))
#     conn.commit()
#
#
# mycursor.execute("select * from users")
# userinfo = []
#
# for x in mycursor:
#     for y in x:
#         userinfo.append(y)
#
# if len(userinfo) > 0:
#     username, stored_hashed_password, email, birthdate, years, img_path = userinfo
#     if not img_path:
#         img_path = "Pictures/Anonymous.png"
# else:
#     img_path = "Pictures/Anonymous.png"
#
# img_path = img_path
# pil_img = Image.open(img_path)
# pil_img = pil_img.resize((400, 400), Image.BICUBIC)
# img = ImageTk.PhotoImage(pil_img)
# global picture_label, img_reference
# img_reference = img
#
# picture_label = Label(profile_frame, image=img)
# picture_label.place(x=0, y=0)
#
# upload_button = ttk.Button(profile_frame, text="Качи снимка", command=upload_picture)
# upload_button.place(x=0, y=402)
#
#
# def update_profile_info():
#     mycursor.execute("select * from users")
#     userinfo = []
#
#     for x in mycursor:
#         for y in x:
#             userinfo.append(y)
#
#     if len(userinfo) > 0:
#         username, stored_hashed_password, email, birthdate, years, img_path = userinfo
#         if not img_path:
#             img_path = "Pictures/Anonymous.png"
#     else:
#         img_path = "Pictures/Anonymous.png"
#
#     label1 = Label(profile_frame, text="Потребителско име:", font=("Arial", 13), relief="raised")
#     label1.place(x=0, y=450)
#     label1_info = Label(profile_frame, text=f"{username}", font=("Arial", 13))
#     label1_info.place(x=0, y=475)
#
#     label2 = Label(profile_frame, text="Е-поща:                  ", font=("Arial", 13), relief="raised")
#     label2.place(x=0, y=505)
#     label2_info = Label(profile_frame, text=f"{email}", font=("Arial", 13))
#     label2_info.place(x=0, y=530)
#
#     label3 = Label(profile_frame, text="Рожденна дата:      ", font=("Arial", 13), relief="raised")
#     label3.place(x=0, y=555)
#     label3_info = Label(profile_frame, text=f"{birthdate}", font=("Arial", 13))
#     label3_info.place(x=0, y=580)
#
#     label4 = Label(profile_frame, text="Години:                  ", font=("Arial", 13), relief="raised")
#     label4.place(x=0, y=605)
#     label4_info = Label(profile_frame, text=f"{years}", font=("Arial", 13))
#     label4_info.place(x=0, y=630)
#
#
# label1 = Label(profile_frame, text="Дневник:", font=("Arial", 20), relief="raised")
# label1.place(x=405, y=1)
#
# text_entry = scrolledtext.ScrolledText(profile_frame, wrap="word", width=75, height=25, font=("Arial", 17))
# text_entry.place(x=403, y=40)
#
# save_button = Button(profile_frame, text="Save", command=save_text, font=("Arial", 15))
# save_button.place(x=1310, y=0)
# save_button.bind("<Enter>", enter)
# save_button.bind("<Leave>", leave)
#
# status_label = Label(profile_frame, text="", font=("Arial", 15))
# status_label.place(x=1195, y=5)
#
# change_button = ttk.Button(profile_frame, text="Промени информация", command=lambda: show_register_frame(2))
# change_button.place(x=0, y=654)
# back_button_profile = tkinter.Button(profile_frame,
#                                      text="<-",
#                                      font=("Algerian", 15),
#                                      width=1, height=1,
#                                      command=back_to_app)
# back_button_profile.place(x=1380, y=0)
# back_button_profile.bind("<Enter>", enter)
# back_button_profile.bind("<Leave>", leave)
# # profile frame code end
# # login_frame code more but im scared to move it to the previous because of errors
# title_label_1 = tkinter.Label(start_frame,
#                               text="4 Days In Barcelona",
#                               font=font).place(x=520, y=0)
# canvas_flag = Canvas(start_frame,
#                      width=900,
#                      height=600)
# canvas_flag.place(x=350, y=33)
# img = (Image.open("Pictures/img.png"))
# resized_image = img.resize((700, 400))
# new_image = ImageTk.PhotoImage(resized_image)
# canvas_flag.create_image(360, 250,
#                          image=new_image)
#
# titleLabel = Label(start_frame, text="Логин").place(x=650, y=490)
#
# username_label = Label(start_frame, text="Потребител:")
# username_label.place(x=347, y=532)
# username_entry_login = Entry(start_frame, font=("Arial", 20))
# username_entry_login.place(x=567, y=532)
#
# password_label = Label(start_frame, text="      Парола:", )
# password_label.place(x=370, y=570)
# password_entry_login = Entry(start_frame, font=("Arial", 20), show="*")
# password_entry_login.place(x=567, y=570)
#
# button_submit = Button(start_frame,
#                        text="         Влез         ",
#                        command=show_app_frame)
# button_submit.place(x=720, y=614)
# button_submit.bind("<Enter>", enter)
# button_submit.bind("<Leave>", leave)
# button_registration = Button(start_frame,
#                              text="Регистрация",
#                              command=lambda: show_register_frame(1))
# button_registration.place(x=450, y=614)
# button_registration.bind("<Enter>", enter)
# button_registration.bind("<Leave>", leave)
# messagelogin_label = Label(start_frame, text="", )
# messagelogin_label.place(x=890, y=547)
#
#
# # restaurants frame
#
# def show_restaurants_frame():
#     def on_configure(event):
#         canvas.configure(scrollregion=canvas.bbox("all"))
#
#     restaurants_window = Toplevel(root)
#     restaurants_window.geometry("1200x525")
#
#     canvas = Canvas(restaurants_window, width=1000, height=500, scrollregion=(0, 0, 2000, 500), bg="white")
#
#     scrollbar = ttk.Scrollbar(restaurants_window, orient="horizontal", command=canvas.xview)
#     scrollbar.pack(side="bottom", fill="x")
#
#     canvas.config(xscrollcommand=scrollbar.set)
#     canvas.pack(side="left", fill="both", expand=True)
#
#     scrollable_frame = Frame(canvas, bg="white")
#
#     for index, restaurant_info in enumerate(restaurant_data):
#         image_path = restaurant_info["image"]
#         name = restaurant_info["name"]
#         info = restaurant_info["info"]
#
#         restaurant_image = PhotoImage(file=image_path).subsample(2)
#         label = ttk.Label(scrollable_frame, image=restaurant_image, text=name, compound="top", style="TLabel",
#                           font=("Arial", 17))
#         label.image = restaurant_image
#         label.grid(row=0, column=index, padx=10, pady=10)
#
#         info_text = Text(scrollable_frame, wrap="word", height=10, width=80)
#         info_text.insert("1.0", info)
#         info_text.config(state="disabled")
#         info_text.grid(row=1, column=index, pady=5)
#
#     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#
#     canvas.bind("<Configure>", on_configure)
#
#
# # login frame code end
# # destionation and navigation buttons functionality, restaurants, clubs and days frames
#
# def show_clubs_weedshops():
#     if int(user1.years) >= 18:
#         clubs_weed_frame = Toplevel(root, width=700, height=350)
#         clubs_weed_frame.title("Клубове и канабис")
#         clubs_weed_frame.geometry("1200x525")
#
#         def on_configure(event):
#             canvas.configure(scrollregion=canvas.bbox("all"))
#
#         canvas = Canvas(clubs_weed_frame, width=1000, height=500, scrollregion=(0, 0, 2000, 500), bg="white")
#
#         scrollbar = ttk.Scrollbar(clubs_weed_frame, orient="horizontal", command=canvas.xview)
#         scrollbar.pack(side="bottom", fill="x")
#
#         canvas.config(xscrollcommand=scrollbar.set)
#         canvas.pack(side="left", fill="both", expand=True)
#
#         scrollable_frame = Frame(canvas, bg="white")
#
#         for index, clubs_info in enumerate(clubs_data):
#             image_path = clubs_info["image"]
#             name = clubs_info["name"]
#             info = clubs_info["info"]
#
#             pil_img = Image.open(image_path)
#
#             width, height = 500, 300
#             pil_img = pil_img.resize((width, height), Image.BICUBIC)
#
#             clubs_image = ImageTk.PhotoImage(pil_img)
#             label = ttk.Label(scrollable_frame, image=clubs_image, text=name, compound="top", style="TLabel",
#                               font=("Arial", 17))
#             label.image = clubs_image
#             label.grid(row=0, column=index, padx=10, pady=10)
#
#             info_text = Text(scrollable_frame, wrap="word", height=10, width=80)
#             info_text.insert("1.0", info)
#             info_text.config(state="disabled")
#             info_text.grid(row=1, column=index, pady=5)
#
#         canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#
#         canvas.bind("<Configure>", on_configure)
#     else:
#         messagebox.showinfo("Грешка","Трябва да имате навършени 18 години, за да отворите!")
#
#
# restaurant_button = Button(app_frame, text="🍽 Ресторанти", font=("Arial", 15), command=show_restaurants_frame)
# restaurant_button.place(x=994, y=580)
# restaurant_button.bind("<Enter>", enter)
# restaurant_button.bind("<Leave>", leave)
#
# clubs_weedshops_button = Button(app_frame, text="(18+)🕺 Клубове и канабис", font=("Arial", 15),
#                                 command=show_clubs_weedshops)
# clubs_weedshops_button.place(x=1144, y=580)
# clubs_weedshops_button.bind("<Enter>", enter)
# clubs_weedshops_button.bind("<Leave>", leave)
#
# current_terminal = None
#
# day1terminal_first_msg_sent = False
#
#
# def day1():
#     global current_frame
#     current_frame = day1_frame
#     global current_terminal
#     current_terminal = day1_terminal
#     day1_frame.pack()
#     start_frame.forget()
#     app_frame.forget()
#     day2_frame.forget()
#     day3_frame.forget()
#     day4_frame.forget()
#     global day1terminal_first_msg_sent
#     if not day1terminal_first_msg_sent:
#         current_terminal.write(
#             "Това е маршрута за Ден 1.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n или да разгледате как да стигнете до тях като натиснете зелените бутони.\n")
#         day1terminal_first_msg_sent = True
#
#
# day2terminal_first_msg_sent = False
#
#
# def day2():
#     global current_frame
#     current_frame = day2_frame
#     global current_terminal
#     current_terminal = day2_terminal
#     day2_frame.pack()
#     start_frame.forget()
#     app_frame.forget()
#     day1_frame.forget()
#     day3_frame.forget()
#     day4_frame.forget()
#     global day2terminal_first_msg_sent
#     if not day2terminal_first_msg_sent:
#         current_terminal.write(
#             "Това е маршрута за Ден 2.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n или да разгледате как да стигнете до тях като натиснете зелените бутони.\n")
#         day2terminal_first_msg_sent = True
#
#
# day3terminal_first_msg_sent = False
#
#
# def day3():
#     global current_frame
#     current_frame = day3_frame
#     global current_terminal
#     current_terminal = day3_terminal
#     day3_frame.pack()
#     start_frame.forget()
#     app_frame.forget()
#     day2_frame.forget()
#     day1_frame.forget()
#     day4_frame.forget()
#     global day3terminal_first_msg_sent
#     if not day3terminal_first_msg_sent:
#         current_terminal.write(
#             "Това е маршрута за Ден 3.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n или да разгледате как да стигнете до тях като натиснете зелените бутони.\n")
#         day3terminal_first_msg_sent = True
#
#
# day4terminal_first_msg_sent = False
#
#
# def day4():
#     global current_frame
#     current_frame = day4_frame
#     global current_terminal
#     current_terminal = day4_terminal
#     day4_frame.pack()
#     start_frame.forget()
#     app_frame.forget()
#     day2_frame.forget()
#     day3_frame.forget()
#     day1_frame.forget()
#     global day4terminal_first_msg_sent
#     if not day4terminal_first_msg_sent:
#         current_terminal.write(
#             "Ден 4ти пътувате обратно следобяд.Можете да си изберете дестинация която искате да доразгледате, да се разходите из плажовете, да видите парк Ситаделата или да се възползвате от бус тур.Можете да разгледате различните дестинации на картата като натиснете червените бутони\n")
#         day4terminal_first_msg_sent = True
#
#
# app_terminal = TkinterTerminal(app_frame)
#
# clock = TimeKeeping(app_frame)
#
#
# def print_sunset():
#     app_terminal.write(f"Залеза днес е в {weather.sunset_time}\n")
#
#
# weather = WeatherWidget(app_frame)
#
# sunset_button = Button(app_frame, text="🌅", font=("Arial", 18), relief=RAISED, command=print_sunset)
# sunset_button.place(x=0, y=480)
# sunset_button.bind("<Enter>", enter)
# sunset_button.bind("<Leave>", leave)
#
# app_frame_back_button = tkinter.Button(app_frame,
#                                        text="<-",
#                                        font=("Algerian", 15),
#                                        width=1, height=1,
#                                        command=show_start_frame_back)
# app_frame_back_button.config(relief=tkinter.RAISED)
# app_frame_back_button.pack(side=tkinter.RIGHT, anchor=tkinter.NE)
# app_frame_back_button.bind("<Enter>", enter)
# app_frame_back_button.bind("<Leave>", leave)
#
# daybuttons_frame = Frame(app_frame)
# day1_button = tkinter.Button(daybuttons_frame,
#                              text="Ден 1",
#                              font=("Algerian", 15),
#                              width=5, height=1,
#                              command=day1)
# day1_button.config(relief=tkinter.RAISED)
# day1_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
# day1_button.bind("<Enter>", enter)
# day1_button.bind("<Leave>", leave)
# day2_button = tkinter.Button(daybuttons_frame,
#                              text="Ден 2",
#                              font=("Algerian", 15),
#                              width=5, height=1,
#                              command=day2)
# day2_button.config(relief=tkinter.RAISED)
# day2_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
# day2_button.bind("<Enter>", enter)
# day2_button.bind("<Leave>", leave)
# day3_button = tkinter.Button(daybuttons_frame,
#                              text="Ден 3",
#                              font=("Algerian", 15),
#                              width=5, height=1,
#                              command=day3)
# day3_button.config(relief=tkinter.RAISED)
# day3_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
# day3_button.bind("<Enter>", enter)
# day3_button.bind("<Leave>", leave)
# day4_button = tkinter.Button(daybuttons_frame,
#                              text="Ден 4",
#                              font=("Algerian", 15),
#                              width=5, height=1,
#                              command=day4)
# day4_button.config(relief=tkinter.RAISED)
# day4_button.pack(side=tkinter.TOP, anchor=tkinter.NE)
# day4_button.bind("<Enter>", enter)
# day4_button.bind("<Leave>", leave)
# daybuttons_frame.place(x=0, y=90)
#
#
# def click_dot(loc):
#     for window in root.winfo_children():
#         if isinstance(window, tkinter.Toplevel):
#             window.destroy()
#     new_window = tkinter.Toplevel()
#     new_window.geometry("1200x600")
#     new_window.title(loc)
#
#     image_path, info = alllocations[loc][0], alllocations[loc][1]
#     image = Image.open(image_path)
#     image = ImageTk.PhotoImage(image)
#
#     image_label = tkinter.Label(new_window, image=image, width=800, height=400)
#     image_label.image = image
#     image_label.pack(anchor='n', pady=10)
#
#     text_frame = tkinter.Frame(new_window, width=1200, height=200)
#     text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)
#
#     text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
#     text_widget.tag_configure("custom_font", font=("Arial", 15))
#     text_widget.insert(tkinter.END, info, "custom_font")
#     text_widget.pack(expand=True, fill="both")
#
#     if current_frame == app_frame:
#         app_terminal.write(f"Вие разгледахте {loc}\n")
#     else:
#         current_terminal.write(f"Вие разгледахте {loc}\n")
#
#
# locations = {'Парк"Лабиринт на Хорта"': (1365, 106),
#              'Парк"Гуел"': (929, 159),
#              'Каса Висенс': (689, 111),
#              'Мол Арена': (290, 101),
#              'Саграда Фамилия': (745, 445),
#              'Ла Рамбла': (383, 340),
#              'Замък Монтжуик': (56, 292),
#              'Триумфална Арка': (607, 483),
#              'Готически Квартал': (381, 465),
#              'Парк Ситадела': (484, 586),
#              'Аквариумът на Барселона': (227, 538)
#              }
#
# desttonav_dict = {'към Аквариумът': 'Аквариумът на Барселона',
#                   'към Ел Понт Моста': 'El Pont del Bisbe',
#                   'към Катедралата': 'Катедралата на Барселона',
#                   'към Пазарът': 'Mercado de La Boqueria',
#                   'към Ла Рамбла и Площада': 'Ла Рамбла и Площада',
#                   'към Палатът на музиката': 'Дворец на каталунската музика',
#                   'към Саграда': 'Саграда Фамилия',
#                   'към Гуел': 'Парк"Гуел"',
#                   'Към Мол Арена': 'Мол Арена',
#                   'към Лабиринта на Хорта': 'Парк"Лабиринт на Хорта"',
#                   'към Къщите': 'Каса Висенс',
#                   'към Монтжуик': 'Замък Монтжуик'
#                   }
#
#
# def enter_nav(event, location):
#     event.widget.config(relief=tkinter.SUNKEN)
#     loc_dict[desttonav_dict[location]].config(relief=tkinter.SUNKEN)
#
#
# def leave_nav(event, location):
#     event.widget.config(relief=tkinter.RAISED)
#     loc_dict[desttonav_dict[location]].config(relief=tkinter.RAISED)
#
#
# red_square_image = tkinter.PhotoImage(width=20, height=20)
# red_square_image.put("red", to=(0, 0, 20, 20))
#
# for location_name, (x, y) in locations.items():
#     red_dot_label = tkinter.Label(background_label, image=red_square_image, bg="gray")
#     red_dot_label.image = red_square_image
#     red_dot_label.config(relief=tkinter.RAISED)
#     red_dot_label.place(x=x, y=y, anchor="center")
#
#     red_dot_label.bind("<Enter>", enter)
#     red_dot_label.bind("<Leave>", leave)
#     red_dot_label.bind("<Button-1>", lambda event, loc=location_name: click_dot(loc))
#
#
# def click_navigation(next_destination):
#     for window in root.winfo_children():
#         if isinstance(window, tkinter.Toplevel):
#             window.destroy()
#     new_window = tkinter.Toplevel()
#     new_window.geometry("1200x600")
#     new_window.title(next_destination)
#     if allnavigations[next_destination][3] == None:
#         image_path_nav, info_nav, terminal_message = allnavigations[next_destination][0], \
#                                                      allnavigations[next_destination][1], \
#                                                      allnavigations[next_destination][2]
#         image = Image.open(image_path_nav)
#         image = ImageTk.PhotoImage(image)
#
#         image_label = tkinter.Label(new_window, image=image, width=800, height=400)
#         image_label.image = image
#         image_label.pack(anchor='n', pady=10)
#
#         text_frame = tkinter.Frame(new_window, width=1200, height=200)
#         text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)
#
#         text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
#         text_widget.tag_configure("custom_font", font=("Arial", 20))
#         text_widget.insert(tkinter.END, info_nav, "custom_font")
#         text_widget.pack(expand=True, fill="both")
#     else:
#         notebook = ttk.Notebook(new_window)
#         tab1 = Frame(notebook)
#         image_path_nav, info_nav, terminal_message = allnavigations[next_destination][0], \
#                                                      allnavigations[next_destination][1], \
#                                                      allnavigations[next_destination][2]
#         image = Image.open(image_path_nav)
#         image = ImageTk.PhotoImage(image)
#
#         image_label = tkinter.Label(tab1, image=image, width=800, height=400)
#         image_label.image = image
#         image_label.pack(anchor='n', pady=10)
#
#         text_frame = tkinter.Frame(tab1, width=1200, height=200)
#         text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)
#
#         text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
#         text_widget.tag_configure("custom_font", font=("Arial", 20))
#         text_widget.insert(tkinter.END, info_nav, "custom_font")
#         text_widget.pack(expand=True, fill="both")
#
#         tab2 = Frame(notebook)
#         image_path_nav, info_nav, terminal_message, image_alt_transport = allnavigations[next_destination][0], \
#                                                                           allnavigations[next_destination][1], \
#                                                                           allnavigations[next_destination][2], \
#                                                                           allnavigations[next_destination][3]
#
#         image = Image.open(image_alt_transport)
#         image = ImageTk.PhotoImage(image)
#
#         image_label = tkinter.Label(tab2, image=image, width=1000, height=400)
#         image_label.image = image
#         image_label.pack(anchor='n', pady=10)
#
#         text_frame = tkinter.Frame(tab2, width=1200, height=200)
#         text_frame.pack(side=tkinter.BOTTOM, fill="both", expand=True)
#
#         text_widget = scrolledtext.ScrolledText(text_frame, wrap=tkinter.WORD, width=100, height=10)
#         text_widget.tag_configure("custom_font", font=("Arial", 20))
#         text_widget.insert(tkinter.END, info_nav, "custom_font")
#         text_widget.pack(expand=True, fill="both")
#         style = ttk.Style()
#         style.configure("TNotebook.Tab", font=("Arial", 15))
#         notebook.add(tab1, text="Пеша                ")
#         notebook.add(tab2, text="Градски Транспорт")
#         notebook.pack(expand=True, fill="both")
#
#     current_terminal.write(f"Вие разгледахте насоките {next_destination}\n")
#     current_terminal.write(terminal_message)
#
#
# profile_button = Button(app_frame, text="👤", font=("Arial", 27), relief=SUNKEN, command=show_profile_frame)
# profile_button.place(x=281, y=0)
# profile_button.bind("<Enter>", leave)
# profile_button.bind("<Leave>", enter)
#
# day1_frame = tkinter.Frame(root, width=1400, height=700)
# day1_frame.pack_propagate(False)
# day1_background_image = Image.open("Pictures/day1.png")
# aspect_ratio = day1_background_image.width / day1_background_image.height
# frame_width = 1400
# frame_height = int(frame_width / aspect_ratio)
# day1_background_image = day1_background_image.resize((frame_width, frame_height), Image.BICUBIC)
# day1_background_photo = ImageTk.PhotoImage(day1_background_image)
# day1_background_label = tkinter.Label(day1_frame, image=day1_background_photo)
# day1_background_label.pack(side=tkinter.TOP, fill=tkinter.X)
# day1_terminal = TkinterTerminal(day1_frame, 1400, 10)
# day1_back_button = tkinter.Button(day1_frame,
#                                   text="<-",
#                                   font=("Algerian", 15),
#                                   width=1, height=1,
#                                   command=back_to_app)
# day1_back_button.config(relief=tkinter.RAISED)
# day1_back_button.place(x=1380, y=0)
# day1_back_button.bind("<Enter>", enter)
# day1_back_button.bind("<Leave>", leave)
# day1_locations = {'Акта Атриум Хотел': (804, 136),
#                   'Аквариумът на Барселона': (1058, 489),
#                   'El Pont del Bisbe': (910, 335),
#                   'Катедралата на Барселона': (908, 306),
#                   'Mercado de La Boqueria': (824, 366),
#                   'Ла Рамбла и Площада': (788, 270),
#                   'Дворец на каталунската музика': (892, 218)
#                   }
# loc_dict = {}
# for location_name, (x, y) in day1_locations.items():
#     red_dot_label = tkinter.Label(day1_background_label, image=red_square_image, bg="gray")
#     red_dot_label.image = red_square_image
#     red_dot_label.config(relief=tkinter.RAISED)
#     red_dot_label.place(x=x, y=y, anchor="center")
#
#     red_dot_label.bind("<Enter>", enter)
#     red_dot_label.bind("<Leave>", leave)
#     red_dot_label.bind("<Button-1>", lambda event, loc=location_name: click_dot(loc))
#     loc_dict[location_name] = red_dot_label
#
# day1_navigations = {'към Аквариумът': (400, 158),
#                     'към Ел Понт Моста': (400, 222),
#                     'към Катедралата': (400, 291),
#                     'към Пазарът': (400, 356),
#                     'към Ла Рамбла и Площада': (400, 420),
#                     'към Палатът на музиката': (400, 489)
#                     }
# for next_destination, (x, y) in day1_navigations.items():
#     navigation_label = tkinter.Label(day1_background_label, text="V", bg="green", font=("Arial", 12))
#     navigation_label.image = red_square_image
#     navigation_label.config(relief=tkinter.RAISED)
#     navigation_label.place(x=x, y=y, anchor="center")
#
#     navigation_label.bind("<Enter>", lambda event, loc=next_destination: enter_nav(event, loc))
#     navigation_label.bind("<Leave>", lambda event, loc=next_destination: leave_nav(event, loc))
#     navigation_label.bind("<Button-1>", lambda event, loc=next_destination: click_navigation(loc))
#
# day2_frame = tkinter.Frame(root, width=1400, height=700)
# day2_frame.pack_propagate(False)
#
# day2_background_image = Image.open("Pictures/day2.png")
# aspect_ratio = day2_background_image.width / day2_background_image.height
# frame_width = 1400
# frame_height = int(frame_width / aspect_ratio)
# day2_background_image = day2_background_image.resize((frame_width, frame_height), Image.BICUBIC)
# day2_background_photo = ImageTk.PhotoImage(day2_background_image)
# day2_background_label = tkinter.Label(day2_frame, image=day2_background_photo)
# day2_background_label.pack(side=tkinter.TOP, fill=tkinter.X)
# day2_terminal = TkinterTerminal(day2_frame, 1400, 10)
# day2_back_button = tkinter.Button(day2_frame,
#                                   text="<-",
#                                   font=("Algerian", 15),
#                                   width=1, height=1,
#                                   command=back_to_app)
# day2_back_button.config(relief=tkinter.RAISED)
# day2_back_button.place(x=1380, y=0)
# day2_back_button.bind("<Enter>", enter)
# day2_back_button.bind("<Leave>", leave)
# day2_locations = {'Акта Атриум Хотел': (1068, 349),
#                   'Саграда Фамилия': (1105, 179),
#                   'Парк"Гуел"': (888, 36),
#                   'Мол Арена': (855, 540)
#                   }
# for location_name, (x, y) in day2_locations.items():
#     red_dot_label = tkinter.Label(day2_background_label, image=red_square_image, bg="gray")
#     red_dot_label.image = red_square_image
#     red_dot_label.config(relief=tkinter.RAISED)
#     red_dot_label.place(x=x, y=y, anchor="center")
#
#     red_dot_label.bind("<Enter>", enter)
#     red_dot_label.bind("<Leave>", leave)
#     red_dot_label.bind("<Button-1>", lambda event, loc=location_name: click_dot(loc))
#     loc_dict[location_name] = red_dot_label
#
# day2_navigations = {'към Саграда': (400, 158),
#                     'към Гуел': (400, 222),
#                     'Към Мол Арена': (400, 291),
#                     }
# for next_destination, (x, y) in day2_navigations.items():
#     navigation_label = tkinter.Label(day2_background_label, text="V", bg="green", font=("Arial", 12))
#     navigation_label.image = red_square_image
#     navigation_label.config(relief=tkinter.RAISED)
#     navigation_label.place(x=x, y=y, anchor="center")
#
#     navigation_label.bind("<Enter>", lambda event, loc=next_destination: enter_nav(event, loc))
#     navigation_label.bind("<Leave>", lambda event, loc=next_destination: leave_nav(event, loc))
#     navigation_label.bind("<Button-1>", lambda event, loc=next_destination: click_navigation(loc))
#
# day3_frame = tkinter.Frame(root, width=1400, height=700)
# day3_frame.pack_propagate(False)
# day3_background_image = Image.open("Pictures/day3.png")
# aspect_ratio = day3_background_image.width / day3_background_image.height
# frame_width = 1400
# frame_height = int(frame_width / aspect_ratio)
# day3_background_image = day3_background_image.resize((frame_width, frame_height), Image.BICUBIC)
# day3_background_photo = ImageTk.PhotoImage(day3_background_image)
# day3_background_label = tkinter.Label(day3_frame, image=day3_background_photo)
# day3_background_label.pack(side=tkinter.TOP, fill=tkinter.X)
# day3_back_button = tkinter.Button(day3_frame,
#                                   text="<-",
#                                   font=("Algerian", 15),
#                                   width=1, height=1,
#                                   command=back_to_app)
# day3_terminal = TkinterTerminal(day3_frame, 1400, 10)
# day3_back_button.config(relief=tkinter.RAISED)
# day3_back_button.place(x=1380, y=0)
# day3_back_button.bind("<Enter>", enter)
# day3_back_button.bind("<Leave>", leave)
# day3_locations = {'Акта Атриум Хотел': (945, 325),
#                   'Парк"Лабиринт на Хорта"': (828, 18),
#                   'Каса Падуа': (826, 235),
#                   'Каса Висенс': (852, 247),
#                   'Каса Мила': (905, 299),
#                   'Замък Монтжуик': (930, 492),
#                   }
# for location_name, (x, y) in day3_locations.items():
#     red_dot_label = tkinter.Label(day3_background_label, image=red_square_image, bg="gray")
#     red_dot_label.image = red_square_image
#     red_dot_label.config(relief=tkinter.RAISED)
#     red_dot_label.place(x=x, y=y, anchor="center")
#
#     red_dot_label.bind("<Enter>", enter)
#     red_dot_label.bind("<Leave>", leave)
#     red_dot_label.bind("<Button-1>", lambda event, loc=location_name: click_dot(loc))
#     loc_dict[location_name] = red_dot_label
#
# day3_navigations = {'към Лабиринта на Хорта': (400, 158),
#                     'към Къщите': (400, 222),
#                     'към Монтжуик': (400, 489)
#                     }
# for next_destination, (x, y) in day3_navigations.items():
#     navigation_label = tkinter.Label(day3_background_label, text="V", bg="green", font=("Arial", 12))
#     navigation_label.image = red_square_image
#     navigation_label.config(relief=tkinter.RAISED)
#     navigation_label.place(x=x, y=y, anchor="center")
#
#     navigation_label.bind("<Enter>", lambda event, loc=next_destination: enter_nav(event, loc))
#     navigation_label.bind("<Leave>", lambda event, loc=next_destination: leave_nav(event, loc))
#     navigation_label.bind("<Button-1>", lambda event, loc=next_destination: click_navigation(loc))
#
# day4_frame = tkinter.Frame(root, width=1400, height=700)
# day4_frame.pack_propagate(False)
# day4_background_image = Image.open("Pictures/day4.png")
# aspect_ratio = day4_background_image.width / day4_background_image.height
# frame_width = 1400
# frame_height = int(frame_width / aspect_ratio)
# day4_background_image = day4_background_image.resize((frame_width, frame_height), Image.BICUBIC)
# day4_background_photo = ImageTk.PhotoImage(day4_background_image)
# day4_background_label = tkinter.Label(day4_frame, image=day4_background_photo)
# day4_background_label.pack(side=tkinter.TOP, fill=tkinter.X)
# day4_back_button = tkinter.Button(day4_frame,
#                                   text="<-",
#                                   font=("Algerian", 15),
#                                   width=1, height=1,
#                                   command=back_to_app)
# day4_terminal = TkinterTerminal(day4_frame, 1400, 10)
# day4_back_button.config(relief=tkinter.RAISED)
# day4_back_button.place(x=1380, y=0)
# day4_back_button.bind("<Enter>", enter)
# day4_back_button.bind("<Leave>", leave)
# day4_locations = {'Акта Атриум Хотел': (613, 205),
#                   'Плаж Сан Себастиан': (394, 505),
#                   'Парк Ситадела': (700, 386),
#                   'Готически Квартал': (510, 341),
#                   'Ла Рамбла': (517, 234),
#                   'Къщите': (621, 30),
#                   'Бус Турове': (781, 92),
#                   'Рецинте Модерниста': (947, 65),
#                   }
# for location_name, (x, y) in day4_locations.items():
#     red_dot_label = tkinter.Label(day4_background_label, image=red_square_image, bg="gray")
#     red_dot_label.image = red_square_image
#     red_dot_label.config(relief=tkinter.RAISED)
#     red_dot_label.place(x=x, y=y, anchor="center")
#
#     red_dot_label.bind("<Enter>", enter)
#     red_dot_label.bind("<Leave>", leave)
#     red_dot_label.bind("<Button-1>", lambda event, loc=location_name: click_dot(loc))
#     loc_dict[location_name] = red_dot_label
#
# #function to find coordinates for the destinations
# # def do_something(event):
# #      print("Mouse coordinates: " + str(event.x) + ", " + str(event.y))
# # day4_background_label.bind("<Button-1>", do_something)
#
#
# show_start_frame()
# root.mainloop()