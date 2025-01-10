short = ["NICSRC", "NICDST", "ROUTER", "SWITCH", "HDDSRC", "HDDDST"]
long = ["source NIC", "destination NIC", "router", "switch", "source drive", "destination drive"]

arr = []
for line in open(0):
    name, speed = line.strip().split()
    if name == 'HDDSRC':
        speed = float(speed.split("/")[0])
    elif name == 'HDDDST':
        speed = float(speed.split("/")[1])
    else:
        speed = float(speed) * 125
    arr.append((speed, name))
speed, name = min(filter(lambda x: x[0] > 0, arr))
print(f"{((int)(speed * 10))/10:.1f}")
print(long[short.index(name)])
