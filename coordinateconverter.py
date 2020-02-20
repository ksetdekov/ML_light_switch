with open("coordinates.txt", "r") as f:
    data = f.readlines()
print(data[2])
print(data[3])


from spatial import vincenty_inverse as vi
home = [55.711295, 37.612321]
p1 = [-81.4061265, 41.250386]
print(vi(home, p1).km())