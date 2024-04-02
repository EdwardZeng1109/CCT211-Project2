import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime,date
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


        # First line
        self.create_label_with_necessary(self.first_line_frame, "Room Number")
        self.room_number_entry = ttk.Combobox(self.first_line_frame, values=["101", "102", "103", "104", "105"], width=10)
        self.room_number_entry.pack(side=tk.LEFT, padx=5, pady=5)

        #set reservation_date to today's date
        self.reservation_date_label = tk.Label(self.first_line_frame, text="Reservation Date")
        self.reservation_date_label.pack(side=tk.LEFT)
        today = datetime.now().strftime("%Y-%m-%d")
        self.reservation_date_entry = tk.Label(self.first_line_frame, text=today, fg="black")
        self.reservation_date_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_label_with_necessary(self.first_line_frame, "First Name")
        self.first_name_entry = tk.Entry(self.first_line_frame, width=20)
        self.first_name_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_label_with_necessary(self.first_line_frame, "Last Name")
        self.last_name_entry = tk.Entry(self.first_line_frame, width=20)
        self.last_name_entry.pack(side=tk.LEFT, padx=5, pady=5)
       
        # Second line

        # Date Calender Entry
        today_date = date.today()
        
        self.create_label_with_necessary(self.second_line_frame, "Checkin Date")
        self.checkin_date_entry = DateEntry(self.second_line_frame, date_pattern='yyyy-MM-dd', mindate=today_date)
        self.checkin_date_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_label_with_necessary(self.second_line_frame, "Checkout Date")
        self.checkout_date_entry = DateEntry(self.second_line_frame, date_pattern='yyyy-MM-dd', mindate=today_date)
        self.checkout_date_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_label_with_necessary(self.second_line_frame, "Number of Guests")
        self.number_of_guests_entry = ttk.Combobox(self.second_line_frame, values=list(range(1, 4)), width=10)
        self.number_of_guests_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_label_with_necessary(self.second_line_frame, "Email")
        self.email_entry = tk.Entry(self.second_line_frame, width=30)
        self.email_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Third line
        # Special Requirements is not necessary
        special_requirements_label = tk.Label(self.third_line_frame, text="Special Requirements")
        special_requirements_label.pack(side=tk.LEFT)
        self.special_requirements_entry = tk.Entry(self.third_line_frame, width=60)
        self.special_requirements_entry.pack(side=tk.LEFT, padx=10, pady=5)

        self.create_label_with_necessary(self.third_line_frame, "Phone Number")
        validate_phone_number = (master.register(self.only_numbers), '%P')
        self.phone_number_entry = tk.Entry(self.third_line_frame, validate="key", validatecommand=validate_phone_number)
        self.phone_number_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_label_with_necessary(self.third_line_frame, "Payment Method")
        self.payment_method_entry = ttk.Combobox(self.third_line_frame, values=["Credit", "Debit", "Cash"], width=10)
        self.payment_method_entry.pack(side=tk.LEFT, padx=5, pady=5)


        # Add Booking Button: Initialize the state to Disabled
        self.add_booking_button = tk.Button(self.third_line_frame, text="Add Booking",
                                            command=self.add_booking_to_database, state=tk.DISABLED)
        self.add_booking_button.pack(side=tk.RIGHT, padx=5)
        Tooltip(self.add_booking_button, "Please fill in all necessary fields to enable this button")

        # Call update_button_state
        # Combobox and DateEntry widgets use：ComboboxSelected
        self.room_number_entry.bind('<<ComboboxSelected>>', self.update_button_state)
        self.checkin_date_entry.bind('<<DateEntrySelected>>', self.update_button_state)
        self.checkout_date_entry.bind('<<DateEntrySelected>>', self.update_button_state)
        self.number_of_guests_entry.bind('<<ComboboxSelected>>', self.update_button_state)
        self.payment_method_entry.bind('<<ComboboxSelected>>', self.update_button_state)

        # Regular entry widget use: KeyRelease
        self.first_name_entry.bind('<KeyRelease>', self.update_button_state)
        self.last_name_entry.bind('<KeyRelease>', self.update_button_state)
        self.email_entry.bind('<KeyRelease>', self.update_button_state)
        self.phone_number_entry.bind('<KeyRelease>', self.update_button_state)
        self.special_requirements_entry.bind('<KeyRelease>', self.update_button_state)

    def update_button_state(self, event=None):
        # Check if all fields are filled
        if (self.room_number_entry.get() and
                self.first_name_entry.get() and self.last_name_entry.get() and
                self.checkin_date_entry.get() and self.checkout_date_entry.get() and
                self.number_of_guests_entry.get() and self.email_entry.get() and
                self.phone_number_entry.get() and self.payment_method_entry.get()):
            self.add_booking_button['state'] = tk.NORMAL
        else:
            self.add_booking_button['state'] = tk.DISABLED


    def only_numbers(self, P):
            return P.isdigit() or P == "" # only accept numeric characters


    #ADD STAR SIGN
    def create_label_with_necessary(self, parent, text):
        label_with_necessary = tk.Label(parent, text="*" + text, fg="black")
        label_with_necessary.pack(side=tk.LEFT, padx=5)


    def add_booking_to_database(self):
            # Collecting data from Entry widgets
            room_number = self.room_number_entry.get()
            reservation_date = datetime.now().strftime("%Y-%m-%d")
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

            self.clear_entry_fields()

            # Refresh the information in the table
            if self.it:
                self.it.refresh_table_view()

    def clear_entry_fields(self):
        # Clear entry fields for regular Entry widgets
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.special_requirements_entry.delete(0, tk.END)

        # Reset Combobox selections to default
        self.room_number_entry.set('')
        self.number_of_guests_entry.set('')
        self.payment_method_entry.set('')

        # Reset DateEntry fields to today's date or another appropriate default date
        today = datetime.now()
        self.checkin_date_entry.set_date(today)
        self.checkout_date_entry.set_date(today)




#TOOLTIP WHEN MOUSE OVER THE BOOKING BUTTON
class Tooltip:
    def __init__(self, widget, text='Widget info'):
        self.waittime = 500     # Milliseconds
        self.wraplength = 180   # Pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        self.schedule()

    def close(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow = None

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = getattr(self, 'id', None)
        if id:
            self.widget.after_cancel(id)
        self.id = None

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 0
        y += self.widget.winfo_rooty() + 20

        # Creates a toplevel window
        self.tipwindow = tw = tk.Toplevel(self.widget)

        # Leaves only the label and removes the app window
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=10)
