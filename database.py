import sqlite3

def create_and_populate_db():
    conn = sqlite3.connect('hotel_booking.db')
    c = conn.cursor()

    # Drop the existing table to start fresh
    c.execute('DROP TABLE IF EXISTS reservations')

    # Create table with the correct order of columns as per your listing
    c.execute('''CREATE TABLE IF NOT EXISTS reservations
                 (room_number INTEGER,
                  reservation_date TEXT,
                  first_name TEXT,
                  last_name TEXT,
                  checkin_date TEXT,
                  checkout_date TEXT,
                  number_of_guests INTEGER,
                  special_requirements TEXT)''')

    # Insert Data with the new order
    reservations = [
        (104, '2023-04-12', 'Dale', 'Harvey', '2023-04-14', '2023-04-20', 1, 'Early check-in if possible.'),
        (105, '2023-10-02', 'Penny', 'Harper', '2023-10-03', '2023-10-27', 1, 'Add an extra bed.'),
        (106, '2023-05-27', 'Andrew', 'Cruz', '2023-05-28', '2023-06-11', 1, 'No peanuts in the minibar, please.'),
        (107, '2023-06-30', 'Luke', 'Jones', '2023-07-01', '2023-07-20', 2, 'Early check-in if possible.'),
        (108, '2024-01-24', 'Ryan', 'Whitney', '2024-01-25', '2024-01-27', 2, 'No peanuts in the minibar, please.'),
        (109, '2023-10-14', 'Douglas', 'Miller', '2023-10-15', '2023-11-06', 4, 'Early check-in if possible.'),
        (110, '2023-12-26', 'Karen', 'Sanchez', '2023-12-27', '2023-12-31', 1, 'High floor request.'),
        (111, '2023-09-25', 'Shannon', 'Lynch', '2023-09-26', '2023-10-17', 3, 'Extra pillows.'),
        (112, '2023-04-15', 'James', 'Hardin', '2023-04-16', '2023-04-22', 4, 'High floor request.'),
        (113, '2023-06-09', 'Michael', 'Campbell', '2023-06-10', '2023-06-25', 2, 'Early check-in if possible.')
    ]
    c.executemany('INSERT INTO reservations VALUES (?,?,?,?,?,?,?,?)', reservations)

    conn.commit()
    conn.close()

create_and_populate_db()
