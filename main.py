import tkinter as tk
from reservation_bar import ReservationBar
from info_table import InfoTable
from room_box import RoomBox
from login_system import Login

def main():
    #log in system page
    root1 = tk.Tk()
    root1.title("Z Hotel Log in System")
    root1.geometry('1200x600')
    login = Login(root1, on_login_success = loged_in)
    root1.mainloop()

def loged_in():
    root = tk.Tk()
    root.title("Z Hotel Reservation System")
    root.geometry('1200x600')
    reservation_bar = ReservationBar(root)
    information_table = InfoTable(root)
    reservation_bar.it=information_table #transfer the information from bar to table --- code in reservation_bar
    room_preview = RoomBox(root)
    root.mainloop()

if __name__ == "__main__":
    main()

