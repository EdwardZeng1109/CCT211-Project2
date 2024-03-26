import tkinter as tk
from reservation_bar import ReservationBar
from info_table import InfoTable
from room_box import RoomBox

def main():
    root = tk.Tk()
    root.title("Z Hotel Reservation System")
    root.geometry('1200x600')

    reservation_bar = ReservationBar(root)
    information_table = InfoTable(root)
    room_preview = RoomBox(root)

    root.mainloop()

if __name__ == "__main__":
    main()

