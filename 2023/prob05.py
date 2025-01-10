for x in map(ord, input()):
    last = x % 6
    x //= 6
    print(f"{x // 6}{x % 6}{last}", end="")
print()
