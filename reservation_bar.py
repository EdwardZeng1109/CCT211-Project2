import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3

class ReservationBar:
    def __init__(self, master, it=None):
        self.it = it
        self.frame = tk.Frame(master)
        self.frame.grid(sticky="nsew")

        # Create Entry Widget for Room Number
        room_number_label = tk.Label(self.frame, text="Room Number")
        room_number_label.grid(row=0, column=0, sticky="w")
        self.room_number_entry = tk.Entry(self.frame, width=10)
        self.room_number_entry.grid(row=0, column=1, sticky="w")

        # Create Entry Widget for Reservation Date
        self.reservation_date_label = tk.Label(self.frame, text="Reservation Date")
        self.reservation_date_label.grid(row=0, column=2, sticky="w")
        self.reservation_date_entry = DateEntry(self.frame)
        self.reservation_date_entry.grid(row=0, column=3, sticky="w")

        # Create Entry Widgets for First and Last Name
        first_name_label = tk.Label(self.frame, text="First Name")
        first_name_label.grid(row=0, column=4, sticky="w")
        self.first_name_entry = tk.Entry(self.frame)
        self.first_name_entry.grid(row=0, column=5, sticky="w")

        last_name_label = tk.Label(self.frame, text="Last Name")
        last_name_label.grid(row=0, column=6, sticky="w")
        self.last_name_entry = tk.Entry(self.frame)
        self.last_name_entry.grid(row=0, column=7, sticky="w")

        # Create Entry Widget for Check-in and Check-out Date
        self.checkin_date_label = tk.Label(self.frame, text="Checkin Date")
        self.checkin_date_label.grid(row=1, column=0, sticky="w")
        self.checkin_date_entry = DateEntry(self.frame)
        self.checkin_date_entry.grid(row=1, column=1, sticky="w")

        self.checkout_date_label = tk.Label(self.frame, text="Checkout Date")
        self.checkout_date_label.grid(row=1, column=2, sticky="w")
        self.checkout_date_entry = DateEntry(self.frame)
        self.checkout_date_entry.grid(row=1, column=3, sticky="w")

        # Create Entry Widget for Number of Guests
        self.number_of_guests_label = tk.Label(self.frame, text="Number of Guests")
        self.number_of_guests_label.grid(row=1, column=4, sticky="w")
        self.number_of_guests_entry = ttk.Combobox(self.frame, values=list(range(1, 11)))
        self.number_of_guests_entry.grid(row=1, column=5, sticky="w")

        # Create Entry Widget for Special Requirements
        special_requirements_label = tk.Label(self.frame, text="Special Requirements")
        special_requirements_label.grid(row=1, column=6, sticky="w")
        self.special_requirements_entry = tk.Entry(self.frame, width=20)
        self.special_requirements_entry.grid(row=1, column=7, sticky="w")

        # Create Entry Widget for Email
        email_label = tk.Label(self.frame, text="Email")
        email_label.grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(self.frame, width=30)
        self.email_entry.grid(row=2, column=1, columnspan=3, sticky="w")

        # Phone Number with validation
        validate_phone_number = (master.register(self.only_numbers), '%P')
        self.phone_number_label = tk.Label(self.frame, text="Phone Number")
        self.phone_number_label.grid(row=2, column=4, sticky="w")
        self.phone_number_entry = tk.Entry(self.frame, validate="key", validatecommand=validate_phone_number)
        self.phone_number_entry.grid(row=2, column=5, sticky="w")

        # Payment Method Combobox
        self.payment_method_label = tk.Label(self.frame, text="Payment Method")
        self.payment_method_label.grid(row=2, column=6, sticky="w")
        self.payment_method_entry = ttk.Combobox(self.frame, values=["Credit", "Debit", "Cash"])
        self.payment_method_entry.grid(row=2, column=7, sticky="w")

        # Booking Button connected to the database
        add_booking_button = tk.Button(self.frame, text="Add Booking", command=self.add_booking_to_database)
        add_booking_button.grid(row=3, column=0, columnspan=8, pady=10, sticky="e")

    def only_numbers(self, P):
        # This method will restrict the entry to only accept numeric characters
        return P.isdigit() or P == ""

    def add_booking_to_database(self):
        # Collecting data from Entry widgets
        room_number = self.room_number_entry.get()
        reservation_date = self.reservation_date_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        checkin_date = self.checkin_date_entry.get()
        checkout_date = self.checkout_date_entry.get()
        number_of_guests = self.number_of_guests_entry.get()
        special_requirements = self.special_requirements_entry.get()
        email = self.email_entry.get()
        phone_number = self.phone_number_entry.get()
        payment_method = self.payment_method_entry.get()

        # Connect to the database and insert data
        try:
            conn = sqlite3.connect('hotel_booking.db')
            c = conn.cursor()

            insert_sql = '''INSERT INTO reservations (room_number, reservation_date, first_name, last_name, 
                            checkin_date, checkout_date, number_of_guests, special_requirements, 
                            email, phone_number, payment_method) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

            c.execute(insert_sql, (room_number, reservation_date, first_name, last_name,
                                   checkin_date, checkout_date, number_of_guests, special_requirements,
                                   email, phone_number, payment_method))

            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Insertion error: {e}")
        finally:
            if conn:
                conn.close()

        # Assuming database operation is successful, now clear the fields and refresh the table
        self.clear_entry_fields()

        # Refresh the information in the table if 'it' is an instance of InfoTable
        if self.it:
            self.it.refresh_table_view()

    def clear_entry_fields(self):
        # Clear entry fields after booking is added
        self.room_number_entry.delete(0, tk.END)
        self.reservation_date_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.checkin_date_entry.delete(0, tk.END)
        self.checkout_date_entry.delete(0, tk.END)
        self.number_of_guests_entry.delete(0, tk.END)
        self.special_requirements_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.payment_method_entry.delete(0, tk.END)
