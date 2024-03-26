import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

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
        if username == "admin" and password == "1":
            self.open_new_window()
        else:
            messagebox.showerror("Login Fail", "Username or Password wrong")

    def open_new_window(self):
        self.root.destroy()

        new_window = tk.Tk()
        new_window.title("Function Page")
        tk.Label(new_window, text="To be implemented").pack()

        new_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()