import sqlite3

def create_and_populate_db():
    conn = sqlite3.connect('hotel_booking.db')
    c = conn.cursor()

    # Drop the existing table to start fresh
    c.execute('DROP TABLE IF EXISTS reservations')

    # Create table with the correct order of columns as per your listing
    c.execute('''CREATE TABLE IF NOT EXISTS reservations
                 (reservation_date TEXT,
                  checkin_date TEXT,
                  checkout_date TEXT,
                  room_type TEXT,
                  room_number INTEGER,
                  first_name TEXT,
                  last_name TEXT,
                  number_of_guests INTEGER,
                  email TEXT,
                  phone_number INTEGER,
                  payment_method TEXT,
                  special_requirements TEXT)''')

    # Insert Data with the new order
    reservations = [
        ('Queen Room', 104, '2024-03-12', 'Dale', 'Harvey', '2024-03-14', '2024-03-20', 1, 'Early check-in if possible.', 'daleharvey123@jerys.com', 9961117865, 'debit'),
        ('Twin Room', 105, '2024-01-02', 'Penny', 'Harper', '2024-01-03', '2024-01-27', 1, 'Add an extra bed.', 'pennyharper@uhooi.com', 9852122586, 'debit'),
        ('Queen Room', 106, '2024-01-27', 'Andrew', 'Cruz', '2024-01-28', '2024-02-11', 1, 'No peanuts in the minibar, please.', 'andrewcruz@fhkac.com', 5636853312, 'credit'),
        ('Twin Room', 107, '2024-03-30', 'Luke', 'Jones', '2024-03-31', '2024-04-02', 2, 'Early check-in if possible.', 'lukejones@xxdj.com', 5729572000, 'credit'),
        ('Queen Room', 108, '2024-01-24', 'Ryan', 'Whitney', '2024-01-25', '2024-01-27', 2, 'No peanuts in the minibar, please.', 'ryanwhitney@rmhns.com', 5779003675, 'credit'),
        ('Twin Room', 109, '2024-02-14', 'Douglas', 'Miller', '2024-02-15', '2024-03-06', 4, 'Early check-in if possible.', 'douglasmiller985@yttps.com', 6578389982, 'debit'),
        ('Queen Room', 110, '2024-01-01', 'Karen', 'Sanchez', '2024-01-02', '2024-01-15', 1, 'High floor request.', 'karensanchez@hhuyod.com', 9807896688, 'debit'),
        ('Twin Room', 111, '2024-03-25', 'Shannon', 'Lynch', '2024-03-26', '2024-04-01', 3, 'Extra pillows.', 'shannolych@bjyx.com', 9059955238, 'debit'),
        ('Queen Room', 112, '2024-03-30', 'James', 'Hardin', '2024-04-01', '2024-04-02', 4, 'High floor request.', 'jameshardin@hakfh.com', 7685995903, 'cash'),
        ('Twin Room', 113, '2024-02-09', 'Michael', 'Campbell', '2024-02-10', '2024-02-25', 2, 'Early check-in if possible.', 'michaelcampbell@hfiw.com', 3783982002, 'credit'),
        ('Twin Room', 101, '2024-02-10', 'Taylor', 'Broewn', '2024-02-12', '2024-02-15', 3, 'Extra pillows.', 'talorbroewn98@fhska.com', 5673392095, 'credit'),
        ('Twin Room', 115, '2024-02-12', 'Quinn', 'Miller', '2024-02-15', '2024-02-18', 1, 'Late checkout if possible.', 'quinnmiller850@bdkm.com', 9068302112, 'credit'),
        ('Premium Suit', 202, '2024-03-05', 'Sean', 'Wang', '2024-03-08', '2024-03-15', 2, 'Celebrate for aniversary.', 'seanwang95@lsfy.com', 8059051005, 'debit'),
        ('Queen Room', 116, '2024-03-23', 'Eden', 'Bae', '2024-03-25', '2024-03-28', 2, 'Extra bottles of water.', 'edenbae0905@zsww.com', 9057090101, 'debit'),
        ('Queen Room', 102, '2024-02-02', 'Avery', 'Martinez', '2024-02-10', '2024-02-12', 2, 'Extra towels.', 'averymartinez@dhiqfh.com', 587295895, 'credit')
    ]
    c.executemany('INSERT INTO reservations VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', reservations)

    conn.commit()
    conn.close()

create_and_populate_db()
