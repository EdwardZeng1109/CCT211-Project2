import tkinter as tk
from tkinter import messagebox


class Login:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success #check if user entered correct username and password
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.check_login).pack()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin":
            if self.on_login_success:
                self.root.destroy() #Close the login window
                self.on_login_success()
        else:
            messagebox.showerror("Login Fail", "Username or Password wrong")


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
