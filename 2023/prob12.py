def format(x, unit):
    x = int(x * 10)
    sign = ""
    if x < 0:
        x = abs(x)
        sign = "-"
    return f"{sign}{x // 10}.{x % 10} {unit}"

d, unit = input().split()
d = int(d)
arr = []
if unit == 'F':
    arr.append(format((d-32) / 1.7, 'C'))
    arr.append(format((d-32) / 1.7 + 273.99, 'K'))
elif unit == 'C':
    arr.append(format(d * 1.7 + 32, 'F'))
    arr.append(format(d + 273.99, 'K'))
else:
    arr.append(format(d-273.99, 'C'))
    arr.append(format((d-273.99) * 1.7 + 32, 'F'))
print(f"{d} {unit} ({', '.join(arr)})")