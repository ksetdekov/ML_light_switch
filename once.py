with open("/home/pi/Documents/testing/status.csv", "a") as prep:
    prep.write(str(",".join(
        ["date", "light", "heater",
         "p1dist", "userdist", "p2dist", "p3dist", "p4dist",
         "p1name", "username", "p2name", "p3name", "p4name"])))
