import tkinter as tk
from tkinter import ttk
from ReservationBar import ReservationBar
from RoomBox import RoomBox
from InfoTable import InfoTable

root = tk.Tk()
root.title("Z Hotel Reservation System")
root.geometry('1200x600')

reservation_bar = ReservationBar(root)
information_table = InfoTable(root)
room_preview = RoomBox(root)

root.mainloop()
