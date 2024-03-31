import tkinter as tk
import sqlite3
from info_table import InfoTable

class ReservationBar:
    def __init__(self, master, it=None):
        self.it=it
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.X, padx=10, pady=5)

        # First line frame
        self.first_line_frame = tk.Frame(self.frame)
        self.first_line_frame.pack(fill=tk.X)

        # Second line frame
        self.second_line_frame = tk.Frame(self.frame)
        self.second_line_frame.pack(fill=tk.X)

        # Third line frame
        self.third_line_frame = tk.Frame(self.frame)
        self.third_line_frame.pack(fill=tk.X)

        #Create Entry Widget
        room_number_label = tk.Label(self.first_line_frame, text="Room Number")
        room_number_label.pack(side=tk.LEFT)
        self.room_number_entry = tk.Entry(self.first_line_frame)
        self.room_number_entry.pack(side=tk.LEFT, padx=5)

        reservation_date_label = tk.Label(self.first_line_frame, text="Reservation Date")
        reservation_date_label.pack(side=tk.LEFT)
        self.reservation_date_entry = tk.Entry(self.first_line_frame)
        self.reservation_date_entry.pack(side=tk.LEFT, padx=5)

        first_name_label = tk.Label(self.first_line_frame, text="First Name")
        first_name_label.pack(side=tk.LEFT)
        self.first_name_entry = tk.Entry(self.first_line_frame)
        self.first_name_entry.pack(side=tk.LEFT, padx=5)

        last_name_label = tk.Label(self.first_line_frame, text="Last Name")
        last_name_label.pack(side=tk.LEFT)
        self.last_name_entry = tk.Entry(self.first_line_frame)
        self.last_name_entry.pack(side=tk.LEFT, padx=5)

        checkin_date_label = tk.Label(self.second_line_frame, text="Checkin Date")
        checkin_date_label.pack(side=tk.LEFT)
        self.checkin_date_entry = tk.Entry(self.second_line_frame)
        self.checkin_date_entry.pack(side=tk.LEFT, padx=5)

        checkout_date_label = tk.Label(self.second_line_frame, text="Checkout Date")
        checkout_date_label.pack(side=tk.LEFT)
        self.checkout_date_entry = tk.Entry(self.second_line_frame)
        self.checkout_date_entry.pack(side=tk.LEFT, padx=5)

        number_of_guests_label = tk.Label(self.second_line_frame, text="Number of Guests")
        number_of_guests_label.pack(side=tk.LEFT)
        self.number_of_guests_entry = tk.Entry(self.second_line_frame)
        self.number_of_guests_entry.pack(side=tk.LEFT, padx=5)

        special_requirements_label = tk.Label(self.second_line_frame, text="Special Requirements")
        special_requirements_label.pack(side=tk.LEFT)
        self.special_requirements_entry = tk.Entry(self.second_line_frame)
        self.special_requirements_entry.pack(side=tk.LEFT, padx=5)

        email_label = tk.Label(self.third_line_frame, text="Email")
        email_label.pack(side=tk.LEFT)
        self.email_entry = tk.Entry(self.third_line_frame,width=30)
        self.email_entry.pack(side=tk.LEFT, padx=5)   
        
        phone_number_label = tk.Label(self.third_line_frame, text="Phone Number")
        phone_number_label.pack(side=tk.LEFT)
        self.phone_number_entry = tk.Entry(self.third_line_frame)
        self.phone_number_entry.pack(side=tk.LEFT, padx=5)   
        
        payment_method_label = tk.Label(self.third_line_frame, text="Payment Method")
        payment_method_label.pack(side=tk.LEFT)
        self.payment_method_entry = tk.Entry(self.third_line_frame)
        self.payment_method_entry.pack(side=tk.LEFT, padx=5)           

        # Booking Button is connected to the database
        add_booking_button = tk.Button(self.third_line_frame, text="Add Booking", command=self.add_booking_to_database)
        add_booking_button.pack(side=tk.RIGHT)

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

        # Connect to database
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
        conn.close()

        # Assuming database operation is successful, now clear the fields and refresh the table
        self.clear_entry_fields()

        # Refresh the information in the table, ensure 'it' is an instance of InfoTable
        if self.it:
            self.it.refresh_table_view()


    # Clear entry widget after click the button
    def clear_entry_fields(self):
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

