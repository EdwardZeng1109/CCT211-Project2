import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3

class ReservationBar:
    def __init__(self, master, it=None):
        self.it = it
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.X, padx=10, pady=5)

        # Use separate frames to organize the widgets in rows
        self.first_line_frame = tk.Frame(self.frame)
        self.first_line_frame.pack(fill=tk.X)

        self.second_line_frame = tk.Frame(self.frame)
        self.second_line_frame.pack(fill=tk.X)

        self.third_line_frame = tk.Frame(self.frame)
        self.third_line_frame.pack(fill=tk.X)

        # Create widgets in the first line
        room_number_label = tk.Label(self.first_line_frame, text="Room Number")
        room_number_label.pack(side=tk.LEFT)
        self.room_number_entry = tk.Entry(self.first_line_frame, width=10)
        self.room_number_entry.pack(side=tk.LEFT)

        self.reservation_date_label = tk.Label(self.first_line_frame, text="Reservation Date")
        self.reservation_date_label.pack(side=tk.LEFT)
        self.reservation_date_entry = DateEntry(self.first_line_frame)
        self.reservation_date_entry.pack(side=tk.LEFT)

        # Create widgets in the second line
        self.checkin_date_label = tk.Label(self.second_line_frame, text="Checkin Date")
        self.checkin_date_label.pack(side=tk.LEFT)
        self.checkin_date_entry = DateEntry(self.second_line_frame)
        self.checkin_date_entry.pack(side=tk.LEFT)

        self.checkout_date_label = tk.Label(self.second_line_frame, text="Checkout Date")
        self.checkout_date_label.pack(side=tk.LEFT)
        self.checkout_date_entry = DateEntry(self.second_line_frame)
        self.checkout_date_entry.pack(side=tk.LEFT)

        self.number_of_guests_label = tk.Label(self.second_line_frame, text="Number of Guests")
        self.number_of_guests_label.pack(side=tk.LEFT)
        self.number_of_guests_entry = ttk.Combobox(self.second_line_frame, values=list(range(1, 11)))
        self.number_of_guests_entry.pack(side=tk.LEFT)

        email_label = tk.Label(self.second_line_frame, text="Email")
        email_label.pack(side=tk.LEFT)
        self.email_entry = tk.Entry(self.second_line_frame, width=30)
        self.email_entry.pack(side=tk.LEFT)

        notes_label = tk.Label(self.second_line_frame, text="Notes")
        notes_label.pack(side=tk.LEFT)
        self.notes_entry = tk.Entry(self.second_line_frame, width=30)
        self.notes_entry.pack(side=tk.LEFT)

        # Create widgets in the third line
        self.phone_number_label = tk.Label(self.third_line_frame, text="Phone Number")
        self.phone_number_label.pack(side=tk.LEFT)
        validate_phone_number = (master.register(self.only_numbers), '%P')
        self.phone_number_entry = tk.Entry(self.third_line_frame, validate="key", validatecommand=validate_phone_number)
        self.phone_number_entry.pack(side=tk.LEFT)

        self.payment_method_label = tk.Label(self.third_line_frame, text="Payment Method")
        self.payment_method_label.pack(side=tk.LEFT)
        self.payment_method_entry = ttk.Combobox(self.third_line_frame, values=["Credit", "Debit", "Cash"])
        self.payment_method_entry.pack(side=tk.LEFT)

        # Place the Add Booking button below the last line
        add_booking_button = tk.Button(self.frame, text="Add Booking", command=self.add_booking_to_database)
        add_booking_button.pack(side=tk.RIGHT, padx=10, pady=5)

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
                                    email, phone_number, payment_method, notes)  # Add 'notes' column
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

                c.execute(insert_sql, (room_number, reservation_date, first_name, last_name,
                                       checkin_date, checkout_date, number_of_guests, special_requirements,
                                       email, phone_number, payment_method, notes))

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
