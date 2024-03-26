import tkinter as tk
from tkinter import ttk

class InfoTable:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree_scroll = tk.Scrollbar(self.frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.frame, yscrollcommand=self.tree_scroll.set, selectmode="browse")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tree_scroll.config(command=self.tree.yview)

        self.tree['columns'] = ("Room Number", "First Name", "Last Name", "Reservation Date")

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Room Number", anchor=tk.W, width=80)
        self.tree.column("First Name", anchor=tk.W, width=120)
        self.tree.column("Last Name", anchor=tk.W, width=120)
        self.tree.column("Reservation Date", anchor=tk.W, width=120)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Room Number", text="Room Number", anchor=tk.W)
        self.tree.heading("First Name", text="First Name", anchor=tk.W)
        self.tree.heading("Last Name", text="Last Name", anchor=tk.W)
        self.tree.heading("Reservation Date", text="Reservation Date", anchor=tk.W)
