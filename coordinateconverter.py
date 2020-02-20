from spatial import vincenty_inverse as vi

with open("coordinates.txt", "r") as f:
    data = f.readlines()
home = [float(data[1].split(":", 1)[1]), float(data[2].split(":", 1)[1])]
p1 = [55.5993645, 37.2696333]
print(vi(home, p1).km())
