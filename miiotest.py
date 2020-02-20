import miio
from miio import ChuangmiPlug

ip = '192.168.1.2'
token = 'e1ef4f9f97aaf257f54270adf2d998f3'
plug = ChuangmiPlug(ip, token , model="chuangmi.plug.m3")
print(plug.status())
plug.off()
plug.on()
