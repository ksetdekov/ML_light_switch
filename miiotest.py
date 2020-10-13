import time

from miio import ChuangmiPlug

# plug
ip = '192.168.1.2'
token = 'e1ef4f9f97aaf257f54270adf2d998f3'
plug = ChuangmiPlug(ip, token, model="chuangmi.plug.m3")
print(plug.status().is_on)
plug.on()
print(plug.status().is_on)
time.sleep(5)
plug.off()
print(plug.status().is_on)

# heater
ip = '192.168.1.26'
token = "9881554e0c43a4f45a28823adf3d0825"
plug = ChuangmiPlug(ip, token, model="chuangmi.plug.m3")
print(plug.status().is_on)
plug.on()
print(plug.status().is_on)
time.sleep(5)
plug.off()
print(plug.status().is_on)
