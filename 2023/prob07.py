for n in (int(x) for x in open(0)):
    if n == 0: break
    if n % 45 == 0:
        print(f"{n} FIZZ FUZZ!")
    elif n % 5 == 0:
        print(f"{n} FIZZ")
    elif n % 9 == 0:
        print(f"{n} FUZZ")
