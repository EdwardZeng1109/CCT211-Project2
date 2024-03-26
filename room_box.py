import tkinter as tk

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
