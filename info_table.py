import tkinter as tk
from tkinter import ttk
import sqlite3


class InfoTable:
    def __init__(self, master):
        # Main Frame
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree_scroll = tk.Scrollbar(self.frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.frame, yscrollcommand=self.tree_scroll.set, selectmode="browse")
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True) #Pack it on TOP for leaving space for Delete Button
        self.tree_scroll.config(command=self.tree.yview)

        #Create Columns
        self.tree['columns'] = ("Room Number", "Reservation Date", "First Name", "Last Name", "Checkin Date",
                                "Checkout Date", "Number of Guests", "Special Requirements",
                                "Email", "Phone Number", "Payment Method")

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Room Number", anchor=tk.CENTER, width=60)
        self.tree.column("Reservation Date", anchor=tk.CENTER, width=120)
        self.tree.column("First Name", anchor=tk.CENTER, width=120)
        self.tree.column("Last Name", anchor=tk.CENTER, width=120)
        self.tree.column("Checkin Date", anchor=tk.CENTER, width=120)
        self.tree.column("Checkout Date", anchor=tk.CENTER, width=120)
        self.tree.column("Number of Guests", anchor=tk.CENTER, width=60)
        self.tree.column("Special Requirements", anchor=tk.W, width=120)
        self.tree.column("Email", anchor=tk.W, width=160)
        self.tree.column("Phone Number", anchor=tk.CENTER, width=120)
        self.tree.column("Payment Method", anchor=tk.CENTER, width=60)

        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("Room Number", text="Room", anchor=tk.CENTER)
        self.tree.heading("Reservation Date", text="Reservation Date", anchor=tk.CENTER)
        self.tree.heading("First Name", text="First Name", anchor=tk.CENTER)
        self.tree.heading("Last Name", text="Last Name", anchor=tk.CENTER)
        self.tree.heading("Checkin Date", text="Checkin", anchor=tk.CENTER)
        self.tree.heading("Checkout Date", text="Checkout", anchor=tk.CENTER)
        self.tree.heading("Number of Guests", text="Guests", anchor=tk.CENTER)
        self.tree.heading("Special Requirements", text="Notes", anchor=tk.CENTER)
        self.tree.heading("Email", text="Email", anchor=tk.CENTER)
        self.tree.heading("Phone Number", text="Phone Number", anchor=tk.CENTER)
        self.tree.heading("Payment Method", text="Payment", anchor=tk.CENTER)

        self.load_data_from_db()

        self.delete_button = tk.Button(self.frame, text="Delete Selected", command=self.delete_selected_entry)
        self.delete_button.pack(side=tk.BOTTOM, pady=5)

    

    def load_data_from_db(self):
        """Load reservation data from the SQLite database and populate the Treeview."""
        try:
            conn = sqlite3.connect('hotel_booking.db')
            c = conn.cursor()
            c.execute('SELECT * FROM reservations')
            rows = c.fetchall()
            if rows:
                print(f"{len(rows)} rows fetched from the database.")
            else:
                print("No data fetched. The database might be empty or not connected properly.")

            for row in rows:
                print(f"Inserting row: {row}")
                self.tree.insert("", 0, values=row)  # O means Insert at the beginning
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()


    def refresh_table_view(self):

        # Clear existing entries in the table view.
        for entry in self.tree.get_children():
            self.tree.delete(entry)

        # Query the database for the latest reservation data.
        conn = sqlite3.connect('hotel_booking.db')
        c = conn.cursor()
        c.execute(
            "SELECT room_number, reservation_date, first_name, last_name, checkin_date, checkout_date, number_of_guests, special_requirements, email, phone_number, payment_method FROM reservations")
        rows = c.fetchall()

        # Repopulate the table view with the latest data.
        for row in rows:
            self.tree.insert("", 0, values=row) 


if __name__ == "__main__":
    root = tk.Tk()
    app = InfoTable(root)
    root.title("Hotel Booking Information")
    root.geometry("800x400")
    root.mainloop()
