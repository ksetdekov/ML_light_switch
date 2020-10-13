import datetime
import sqlite3

import Adafruit_DHT


def add_data(temp_inp, hum_inp, cur_time):
    try:
        sqlite_con = sqlite3.connect('temperature.db')
        cursor = sqlite_con.cursor()
        sqlite_insert = """INSERT INTO 'timelog'
                ('stamp', 'temp', 'hum')
                VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (cur_time, temp_inp, hum_inp)
        cursor.execute(sqlite_insert, data_tuple)
        sqlite_con.commit()
    except sqlite3.Error as error:
        print("Error while working with sqlite", error)


sensor = Adafruit_DHT.DHT11
while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, 4)
    print('Temp: {} C humidity: {}'.format(temp, hum))
    add_data(temp, hum, datetime.datetime.now())
