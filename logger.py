import datetime
import sqlite3
import subprocess
import time

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
ip_pl = '192.168.1.2'
token_pl = 'e1ef4f9f97aaf257f54270adf2d998f3'
plug = ChuangmiPlug(ip_pl, token_pl, model="chuangmi.plug.m3")
print(plug.status().is_on)

# heater
ip_h = '192.168.1.26'
token_h = "9881554e0c43a4f45a28823adf3d0825"
heater = ChuangmiPlug(ip_h, token_h, model="chuangmi.plug.m3")
print(heater.status().is_on)

while True:
    result1 = subprocess.run(['miplug', '--ip', ip_pl, '--token', token_pl, 'status'],
                             stdout=subprocess.PIPE)
    txt1 = result1.stdout.decode("utf-8")
    status1 = txt1.split()[1]
    print(status1)
    status1 = responseformat(status1)

    result2 = subprocess.run(['miplug', '--ip', ip_h, '--token', token_h, 'status'],
                             stdout=subprocess.PIPE)
    txt2 = result2.stdout.decode("utf-8")
    status2 = txt2.split()[1]
    print(status2)

    status2 = responseformat(status2)

    hum, temp = Adafruit_DHT.read_retry(sensor, 4)
    # hum, temp = (1, 1)
    print('Temp: {} C humidity: {}'.format(temp, hum))
    print(f'plug on? {status1}, heater on {status2}')
    add_data(temp, hum, status1, status2, datetime.datetime.now())
    time.sleep(1)
