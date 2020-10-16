import sqlite3
from pandas import DataFrame

conn = sqlite3.connect('temperature.db')
cur = conn.cursor()
cur.execute("select stamp, temp, hum, plug, heater from timelog")

myresult = DataFrame(cur.fetchall())
print(myresult.tail())
conn.close()


import matplotlib.pyplot as plt
# plt.hist(myresult[1], bins=100)
# plt.show()


# plt.hist(myresult[2], bins=100)
# plt.show()

pd_plug_on = myresult[myresult[3] == 1]
pd_plug_off = myresult[myresult[3] != 1]

import numpy

bins = numpy.linspace(20, 29, 10)

plt.hist(pd_plug_on[1], bins, alpha=0.5, label='on_light')
plt.hist(pd_plug_off[1], bins, alpha=0.5, label='off_light')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

pd_heater_on = myresult[myresult[4] == 1]
pd_heater_off = myresult[myresult[4] != 1]
plt.hist(pd_heater_on[1], bins, alpha=0.5, label='on_heater')
plt.hist(pd_heater_off[1], bins, alpha=0.5, label='off_heater')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()