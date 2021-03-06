import datetime
import os
import sqlite3
import time

import Adafruit_DHT
from miio import ChuangmiPlug

os.chdir('/home/pi/Documents/ML_light_switch/')

Goodvalues = [True, False]


def responseformat(resp):
    if resp in Goodvalues:
        return resp
    else:
        return None


if not os.path.exists('temperature.db'):
    conn = sqlite3.connect('temperature.db')
    cur = conn.cursor()
    # Make some fresh tables using executescript()
    cur.executescript('''CREATE TABLE "timelog" (
    "stamp" TEXT,
    "temp"  NUMERIC,
    "hum"   NUMERIC,
    "plug"  INTEGER,
    "heater"    INTEGER,
    PRIMARY KEY("stamp")
    );''')
    conn.commit()
    cur.close()


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


sensor = Adafruit_DHT.DHT22

# plug
ip_pl = '192.168.1.2'
token_pl = 'e1ef4f9f97aaf257f54270adf2d998f3'
plug = ChuangmiPlug(ip_pl, token_pl, model="chuangmi.plug.m3")
# print(plug.status().is_on)

# heater
ip_h = '192.168.1.26'
token_h = "9881554e0c43a4f45a28823adf3d0825"
heater = ChuangmiPlug(ip_h, token_h, model="chuangmi.plug.m3")
# print(heater.status().is_on)

while True:
    try:
        status1 = plug.status().is_on
    except:
        status1 = None
    # status1 = responseformat(status1)

    try:
        status2 = heater.status().is_on
    except:
        status2 = None
    # status2 = responseformat(status2)

    hum, temp = Adafruit_DHT.read_retry(sensor, 4)
    # hum, temp = (1, 1)
    print('Temp: {} C humidity: {}'.format(temp, hum))
    print('plug on? {}, heater on {}'.format(status1, status2))
    add_data(temp, hum, status1, status2, datetime.datetime.now())
    time.sleep(1)
