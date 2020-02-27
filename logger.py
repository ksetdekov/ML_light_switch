from time import strftime, time

import matplotlib.pyplot as plt
from miio import ChuangmiPlug

from getlocation import string_distances

plt.ion()
x = []
y = []


def write_status(st1, st2, st3):
    with open("/home/pi/Documents/testing/status.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(",".join([st1, st2, st3]))))


def graph(variable1):
    y.append(variable1)
    x.append(time())
    plt.clf()
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.draw()


Goodvalues = ['True', 'False']


def responseformat(resp):
    if resp in Goodvalues:
        return resp
    else:
        return "nan"


ip1 = '192.168.1.2'
token1 = 'e1ef4f9f97aaf257f54270adf2d998f3'
plug1 = ChuangmiPlug(ip1, token1, model="chuangmi.plug.m3")

ip2 = '192.168.1.3'
token2 = '9a959331e150c3a6919df3433952938e'
plug2 = ChuangmiPlug(ip2, token2, model="chuangmi.plug.m3")

while True:
    txt1 = str(plug1.status())
    status1 = txt1.split()[1]
    status1 = responseformat(status1)

    txt2 = str(plug2.status())
    status2 = txt2.split()[1]
    status1 = responseformat(status1)
    distances = string_distances()

    write_status(status1, status2, distances)
    # graph(status1)
    plt.pause(60)
