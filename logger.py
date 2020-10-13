import datetime
import sqlite3

import Adafruit_DHT
from miio import ChuangmiPlug

Goodvalues = ['True', 'False']


def responseformat(resp):
    if resp in Goodvalues:
        return resp
    else:
        return "nan"


def add_data(temp_inp, hum_inp, plug_status, heater_status, cur_time):
    try:
        sqlite_con = sqlite3.connect('temperature.db')
        cursor = sqlite_con.cursor()
        sqlite_insert = """INSERT INTO 'timelog'
                ('stamp', 'temp', 'hum', 'plug', 'heater')
                VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (cur_time, temp_inp, hum_inp, plug_status, heater_status)
        cursor.execute(sqlite_insert, data_tuple)
        sqlite_con.commit()
    except sqlite3.Error as error:
        print("Error while working with sqlite", error)


sensor = Adafruit_DHT.DHT11

# plug
ip = '192.168.1.2'
token = 'e1ef4f9f97aaf257f54270adf2d998f3'
plug = ChuangmiPlug(ip, token, model="chuangmi.plug.m3")
print(plug.status().is_on)

# heater
ip = '192.168.1.26'
token = "9881554e0c43a4f45a28823adf3d0825"
heater = ChuangmiPlug(ip, token, model="chuangmi.plug.m3")
print(heater.status().is_on)

while True:
    status1 = plug.status().is_on
    status1 = responseformat(status1)

    status2 = heater.status().is_on
    status2 = responseformat(status2)

    hum, temp = Adafruit_DHT.read_retry(sensor, 4)
    print('Temp: {} C humidity: {}'.format(temp, hum))
    add_data(temp, hum, status1, status2, datetime.datetime.now())
