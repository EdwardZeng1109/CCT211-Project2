import sqlite3

def create_and_populate_db():
    conn = sqlite3.connect('hotel_booking.db')
    c = conn.cursor()

    # Drop the existing table to start fresh
    c.execute('DROP TABLE IF EXISTS reservations')

    # Create table with the correct order of columns as per your listing
    c.execute('''CREATE TABLE IF NOT EXISTS reservations
                 (room_type TEXT,
                 room_number INTEGER,
                  reservation_date TEXT,
                  first_name TEXT,
                  last_name TEXT,
                  checkin_date TEXT,
                  checkout_date TEXT,
                  number_of_guests INTEGER,
                  special_requirements TEXT,
                  email TEXT,
                  phone_number INTEGER,
                  payment_method TEXT)''')

    # Insert Data with the new order
    reservations = [
        ('Queen Room', 104, '2023-04-12', 'Dale', 'Harvey', '2023-04-14', '2023-04-20', 1, 'Early check-in if possible.', 'daleharvey123@jerys.com', 9961117865, 'debit'),
        ('Twin Room', 105, '2023-10-02', 'Penny', 'Harper', '2023-10-03', '2023-10-27', 1, 'Add an extra bed.', 'pennyharper@uhooi.com', 9852122586, 'debit'),
        ('Queen Room', 106, '2023-05-27', 'Andrew', 'Cruz', '2023-05-28', '2023-06-11', 1, 'No peanuts in the minibar, please.', 'andrewcruz@fhkac.com', 5636853312, 'credit'),
        ('Twin Room', 107, '2023-06-30', 'Luke', 'Jones', '2023-07-01', '2023-07-20', 2, 'Early check-in if possible.', 'lukejones@xxdj.com', 5729572000, 'credit'),
        ('Queen Room', 108, '2024-01-24', 'Ryan', 'Whitney', '2024-01-25', '2024-01-27', 2, 'No peanuts in the minibar, please.', 'ryanwhitney@rmhns.com', 5779003675, 'credit'),
        ('Twin Room', 109, '2023-10-14', 'Douglas', 'Miller', '2023-10-15', '2023-11-06', 4, 'Early check-in if possible.', 'douglasmiller985@yttps.com', 6578389982, 'debit'),
        ('Queen Room', 110, '2023-12-26', 'Karen', 'Sanchez', '2023-12-27', '2023-12-31', 1, 'High floor request.', 'karensanchez@hhuyod.com', 9807896688, 'debit'),
        ('Twin Room', 111, '2023-09-25', 'Shannon', 'Lynch', '2023-09-26', '2023-10-17', 3, 'Extra pillows.', 'shannolych@bjyx.com', 9059955238, 'debit'),
        ('Queen Room', 112, '2023-04-15', 'James', 'Hardin', '2023-04-16', '2023-04-22', 4, 'High floor request.', 'jameshardin@hakfh.com', 7685995903, 'cash'),
        ('Twin Room', 113, '2023-06-09', 'Michael', 'Campbell', '2023-06-10', '2023-06-25', 2, 'Early check-in if possible.', 'michaelcampbell@hfiw.com', 3783982002, 'credit'),
        ('Twin Room', 101, '2023-06-10', 'Taylor', 'Broewn', '2023-06-12', '2023-06-15', 3, 'Extra pillows.', 'talorbroewn98@fhska.com', 5673392095, 'credit'),
        ('Twin Room', 115, '2023-06-12', 'Quinn', 'Miller', '2023-06-15', '2023-06-18', 1, 'Late checkout if possible.', 'quinnmiller850@bdkm.com', 9068302112, 'credit'),
        ('Queen Room', 118, '2023-09-05', 'Sean', 'Wang', '2023-09-08', '2023-09-15', 2, 'Celebrate for aniversary.', 'seanwang95@lsfy.com', 8059051005, 'debit'),
        ('Queen Room', 116, '2023-06-22', 'Eden', 'Bae', '2023-06-23', '2023-06-27', 2, 'Extra bottles of water.', 'edenbae0905@zsww.com', 9057090101, 'debit'),
        ('Queen Room', 102, '2023-07-07', 'Avery', 'Martinez', '2023-07-10', '2023-07-12', 2, 'Extra towels.', 'averymartinez@dhiqfh.com', 587295895, 'credit')
    ]
    c.executemany('INSERT INTO reservations VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', reservations)

    conn.commit()
    conn.close()

create_and_populate_db()
