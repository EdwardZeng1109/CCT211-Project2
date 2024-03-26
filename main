import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Z Hotel Reservation System")
root.geometry('1200x600')

class ReservationBar:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.X, padx=10, pady=5)

        check_in_label = tk.Label(self.frame, text="Room Number")
        check_in_label.pack(side=tk.LEFT)
        self.check_in_entry = tk.Entry(self.frame)
        self.check_in_entry.pack(side=tk.LEFT, padx=5)

        check_out_label = tk.Label(self.frame, text="First Name")
        check_out_label.pack(side=tk.LEFT)
        self.check_out_entry = tk.Entry(self.frame)
        self.check_out_entry.pack(side=tk.LEFT, padx=5)

        check_out_label = tk.Label(self.frame, text="Last Name")
        check_out_label.pack(side=tk.LEFT)
        self.check_out_entry = tk.Entry(self.frame)
        self.check_out_entry.pack(side=tk.LEFT, padx=5)

        check_out_label = tk.Label(self.frame, text="Date")
        check_out_label.pack(side=tk.LEFT)
        self.check_out_entry = tk.Entry(self.frame)
        self.check_out_entry.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(self.frame, text="Add Booking")
        search_button.pack(side=tk.RIGHT)

class InfoTable:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree_scroll = tk.Scrollbar(self.frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.frame, yscrollcommand=self.tree_scroll.set, selectmode="browse")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tree_scroll.config(command=self.tree.yview)

        # Define our columns
        self.tree['columns'] = ("Room Number", "First Name", "Last Name", "Reservation Date")

        # Format our columns
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Room Number", anchor=tk.W, width=80)
        self.tree.column("First Name", anchor=tk.W, width=120)
        self.tree.column("Last Name", anchor=tk.W, width=80)
        self.tree.column("Reservation Date", anchor=tk.W, width=120)

        # Create Headings
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Room Number", text="Room Number", anchor=tk.W)
        self.tree.heading("First Name", text="First Name", anchor=tk.W)
        self.tree.heading("Last Name", text="Last Name", anchor=tk.W)
        self.tree.heading("Reservation Date", text="Reservation Date", anchor=tk.W)

class RoomBox:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        box_1 = tk.LabelFrame(self.frame, text="Room Availability", padx=5, pady=5)
        box_1.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        box_2 = tk.LabelFrame(self.frame, text="Room Availability", padx=5, pady=5)
        box_2.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        box_3 = tk.LabelFrame(self.frame, text="Room Availability", padx=5, pady=5)
        box_3.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        box_4 = tk.LabelFrame(self.frame, text="Room Availability", padx=5, pady=5)
        box_4.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)


reservation_bar = ReservationBar(root)
information_table = InfoTable(root)
room_preview = RoomBox(root)

root.mainloop()
