import miio
ip = '192.168.1.2'
token = 'e1ef4f9f97aaf257f54270adf2d998f3'
switch = miio.miplug.Miplug(ip, token)
switch.on()
