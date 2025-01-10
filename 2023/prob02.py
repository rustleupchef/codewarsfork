for n in (int(x) for x in open(0)):
    if n == 0: break
    if n % 4 == 0:
        print(f"{n}/4 = {n//4}")
