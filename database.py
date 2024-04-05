import sqlite3

def create_and_populate_db():
    conn = sqlite3.connect('hotel_booking.db')
    c = conn.cursor()

    # Drop the existing table to start fresh
    c.execute('DROP TABLE IF EXISTS reservations')

    # Create table with the correct order of columns as per your listing
    c.execute('''CREATE TABLE IF NOT EXISTS reservations
                 (reservation_id INTEGER,
                  reservation_date TEXT,
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
        ('241708710612','2024-03-12', '2024-03-14', '2024-03-20', 'Queen Room', 104, 'Dale', 'Harvey', 1, 'daleharvey123@jerys.com', 9961117865, 'debit', 'Early check-in if possible.'),
        ('243017699723','2024-01-02', '2024-01-03', '2024-01-27', 'Twin Room', 105, 'Penny', 'Harper', 1, 'pennyharper@uhooi.com', 9852122586, 'debit', 'Add an extra bed.'),
        ('242764459132','2024-01-27', '2024-01-28', '2024-02-11', 'Queen Room', 106, 'Andrew', 'Cruz', 1, 'andrewcruz@fhkac.com', 5636853312, 'credit', 'No peanuts in the minibar, please.'),
        ('241982330234','2024-03-30', '2024-03-31', '2024-04-02', 'Twin Room', 107, 'Luke', 'Jones', 2, 'lukejones@xxdj.com', 5729572000, 'credit', 'Early check-in if possible.'),
        ('245646706656','2024-01-24', '2024-01-25', '2024-01-27', 'Queen Room', 108, 'Ryan', 'Whitney', 2, 'ryanwhitney@rmhns.com', 5779003675, 'credit', 'No peanuts in the minibar, please.'),
        ('240497440836','2024-02-14', '2024-02-15', '2024-03-06', 'Twin Room', 109, 'Douglas', 'Miller', 4, 'douglasmiller985@yttps.com', 6578389982, 'debit', 'Early check-in if possible.'),
        ('245292255078','2024-01-01', '2024-01-02', '2024-01-15', 'Queen Room', 110, 'Karen', 'Sanchez', 1, 'karensanchez@hhuyod.com', 9807896688, 'debit', 'High floor request.'),
        ('246286165953','2024-03-25', '2024-03-26', '2024-04-01', 'Twin Room', 111, 'Shannon', 'Lynch', 3, 'shannolych@bjyx.com', 9059955238, 'debit', 'Extra pillows.'),
        ('249163753565','2024-03-30', '2024-04-01', '2024-04-02', 'Queen Room', 112, 'James', 'Hardin', 4, 'jameshardin@hakfh.com', 7685995903, 'cash', 'High floor request.'),
        ('242422474117','2024-02-09', '2024-02-10', '2024-02-25', 'Twin Room', 113, 'Michael', 'Campbell', 2, 'michaelcampbell@hfiw.com', 3783982002, 'credit', 'Early check-in if possible.'),
        ('248559730890','2024-02-10', '2024-02-12', '2024-02-15', 'Twin Room', 101, 'Taylor', 'Broewn', 3, 'talorbroewn98@fhska.com', 5673392095, 'credit', 'Extra pillows.'),
        ('243017699043','2024-02-12', '2024-02-15', '2024-02-18', 'Twin Room', 115, 'Quinn', 'Miller', 1, 'quinnmiller850@bdkm.com', 9068302112, 'credit', 'Late checkout if possible.'),
        ('245646706365','2024-03-05', '2024-03-08', '2024-03-15', 'Premium Suit', 202, 'Sean', 'Wang', 2, 'seanwang95@lsfy.com', 8059051005, 'debit', 'Celebrate for aniversary.'),
        ('245292254012','2024-03-23', '2024-03-25', '2024-03-28', 'Queen Room', 116, 'Eden', 'Bae', 2, 'edenbae0905@zsww.com', 9057090101, 'debit', 'Extra bottles of water.'),
        ('244286165111','2024-02-02', '2024-02-10', '2024-02-12', 'Queen Room', 102, 'Avery', 'Martinez', 2, 'averymartinez@dhiqfh.com', 587295895, 'credit', 'Extra towels.')
    ]
    c.executemany('INSERT INTO reservations VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', reservations)

    conn.commit()
    conn.close()

create_and_populate_db()
