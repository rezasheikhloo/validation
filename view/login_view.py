from tkinter import *
import tkinter.messagebox as msg

from controller.user_controller import UserController
from view.component import EntryWithLabel
# pip install pillow
from PIL import Image, ImageTk

from view.user_view import UserView


class LoginView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("250x300")

        img = Image.open("view/image/login.png")
        img = ImageTk.PhotoImage(img)
        Label(self.window, image=img).place(x=78, y=20)

        self.username = EntryWithLabel(self.window, "Username", 20, 150)
        self.password = EntryWithLabel(self.window, "Password", 20, 190)

        Button(self.window, text="Login", width=10, command=self.login_click).place(x=80, y=250)

        self.window.mainloop()

    def login_click(self):
        status, user = UserController.find_by_username_and_password(self.username.get(), self.password.get())
        if status:
            self.window.destroy()
            user_view = UserView(user)
        else:
            msg.showerror("Login", "Access Denied !!!")
