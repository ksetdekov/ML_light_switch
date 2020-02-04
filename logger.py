from time import sleep, strftime, time
import matplotlib.pyplot as plt
import miio
import subprocess

plt.ion()
x = []
y = []

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False
    else:
         raise ValueError("Cannot covert {} to a bool".format(s))

def write_status(status1,status2):
    with open("/home/pi/Documents/testing/status.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(",".join([status1,status2]))))

def graph(status1):
    y.append(status1)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()

Goodvalues = ['TRUE', 'FALSE']

def responseformat(resp):
    if resp in Goodvalues:
        return resp
    else:
        return "nan"

while True:
    result1 = subprocess.run(['miplug', '--ip', "192.168.1.2", '--token', "e1ef4f9f97aaf257f54270adf2d998f3", 'status'], stdout=subprocess.PIPE)
    txt1=result1.stdout.decode("utf-8")
    status1 = txt1.split()[1]
    status1 = responseformat(status1)
    
    result2 = subprocess.run(['miplug', '--ip', "192.168.1.3", '--token', "9a959331e150c3a6919df3433952938e", 'status'], stdout=subprocess.PIPE)
    txt2=result2.stdout.decode("utf-8")
    status2 = txt2.split()[1]
    status1 = responseformat(status1)
    
    write_status(status1,status2)
    #graph(status1)
    plt.pause(60)
