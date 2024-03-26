import tkinter as tk

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
