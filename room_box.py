import tkinter as tk
import sqlite3
from tkinter import messagebox
from datetime import datetime


def get_room_reservations():
    '''
    Get room reservation info
    '''
    conn = sqlite3.connect('hotel_booking.db')
    c = conn.cursor()
    c.execute("SELECT room_type, room_number, checkin_date, checkout_date FROM reservations")
    reservations = c.fetchall()
    conn.close()

    # Process reservations into a more usable format
    room_reservations = {}
    for room_type, room, checkin, checkout in reservations:
        checkin_date = datetime.strptime(checkin, '%Y-%m-%d').date()
        checkout_date = datetime.strptime(checkout, '%Y-%m-%d').date()
        if room not in room_reservations:
            room_reservations[room] = []
        # Append a tuple with all the data
        room_reservations[room].append((room_type, checkin_date, checkout_date))
    return room_reservations

class RoomBox:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas to place the room blocks on, with the same background color as the frame
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create the room number labels
        self.room_numbers = []
        for i in range(101, 113):
            self.room_numbers.append(i)
        self.room_labels = []
        self.room_rectangles = []
        self.reservations = {}
        # Draw the initial room blocks
        self.update_room_boxes()
        self.root.after(1000, self.refresh_room_boxes)
        # Bind the canvas resize event
        self.canvas.bind("<Configure>", self.on_resize)

    def update_room_boxes(self):
        # Clear previous room labels and rectangles
        for label in self.room_labels:
            self.canvas.delete(label)
        for rectangle in self.room_rectangles:
            self.canvas.delete(rectangle)

        self.room_labels.clear()
        self.room_rectangles.clear()

        today = datetime.today().date()
        self.reservations = get_room_reservations()

        # Determine the size of the canvas and calculate room sizes
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        room_width = canvas_width // 6  # 6 rooms per row
        room_height = canvas_height // 2  # 2 rows

        for index, room_number in enumerate(self.room_numbers):
            x1 = (index % 6) * room_width
            y1 = (index // 6) * room_height
            x2 = x1 + room_width
            y2 = y1 + room_height
            # Create rectangle and text for each room
            room_color = 'green'  # Default to available
            if room_number in self.reservations:
                for room_type, checkin, checkout in self.reservations[room_number]:
                    if today == checkin:
                        room_color = 'red'  # Occupied today
                    elif today < checkin:
                        room_color = 'blue'  # Reserved in the future
            # Create rectangle and text for each room
            rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=room_color, tags="room")
            label = self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=f'Room {room_number}')
            self.room_labels.append(label)
            self.room_rectangles.append(rectangle)
            # Add click event to the room rectangle
            self.canvas.tag_bind(rectangle, "<Button-1>", lambda event, room=room_number: self.show_room_info(room))
    def refresh_room_boxes(self):
        '''
        Update room information
        '''
        self.update_room_boxes()
        # Reschedule the update
        self.root.after(1000, self.refresh_room_boxes)
    def on_resize(self, event):
        # Redraw room blocks with new sizes
        self.update_room_boxes()

    def show_room_info(self, room_number):
        reservations = self.reservations.get(room_number, [])
        # If there are no reservations, set a default message and room type
        if not reservations:
            dates_reserved = "No reservations"
            room_type = "Not set"
        else:
            # Pick the room type from the first reservation entry
            room_type = reservations[0][0]
            # Format the reserved dates as strings
            dates_reserved = ", ".join([
                f"{checkin.strftime('%Y-%m-%d')} to {checkout.strftime('%Y-%m-%d')}"
                for _, checkin, checkout in reservations
            ])

        # Display room info in a message box
        messagebox.showinfo(
            f"Room {room_number}",
            f"Type: {room_type}\nReserved dates: {dates_reserved}"
        )
