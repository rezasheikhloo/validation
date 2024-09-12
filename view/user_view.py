from tkinter import *
import tkinter.messagebox as msg

from controller.user_controller import UserController
from view.component import EntryWithLabel


class UserView:
    def __init__(self, user):
        self.window = Tk()
        self.window.title("User Profile")
        self.window.geometry("550x300")

        Label(self.window, text=f"Welcome {user.username}", font=("Arial", 16)).place(x=250, y=20)

        self.username = EntryWithLabel(self.window, "Username", 20, 20)
        self.password = EntryWithLabel(self.window, "Password", 20, 60)
        self.name = EntryWithLabel(self.window, "Name", 20, 100)
        self.family = EntryWithLabel(self.window, "Family", 20, 140)

        Label(self.window, text="Active").place(x=20, y=180)
        self.active = IntVar()
        Radiobutton(self.window, text="Enable", variable=self.active, value=1).place(x=100, y=180)
        Radiobutton(self.window, text="Disable", variable=self.active, value=0).place(x=100, y=200)
        self.active.set(1)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=250)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=90, y=250)
        Button(self.window, text="Remove", width=7, command=self.remove_click).place(x=160, y=250)

        self.window.mainloop()

    def save_click(self):
        status, message = UserController.save(self.username.get(),
                                              self.password.get(),
                                              self.name.get(),
                                              self.family.get(),
                                              self.active.get())
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save error", message)

    def edit_click(self):
        status, message = UserController.edit(self.username.get(),
                                              self.password.get(),
                                              self.name.get(),
                                              self.family.get(),
                                              self.active.get())
        if status:
            msg.showinfo("Edit", message)
        else:
            msg.showerror("Edit error", message)

    def remove_click(self):
        status, message = UserController.remove(self.username.get())
        if status:
            msg.showinfo("Remove", message)
        else:
            msg.showerror("Remove error", message)
