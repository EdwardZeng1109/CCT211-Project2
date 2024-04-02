import tkinter as tk
from reservation_bar import ReservationBar
from info_table import InfoTable
from room_box import RoomBox

def main():
    root = tk.Tk()
    root.title("Z Hotel Reservation System")
    root.geometry('1300x600')

    reservation_bar = ReservationBar(root)
    information_table = InfoTable(root)
    reservation_bar.it=information_table #transfer the information from bar to table --- code in reservation_bar
    room_preview = RoomBox(root)

    root.mainloop()

if __name__ == "__main__":
    main()

