def get_month(s):
    y, m, d = map(int, s.split("-"))
    return y * 12 + m, d

a, b, name = (input() for _ in range(3))
aa, a_day = get_month(a)
bb, b_day = get_month(b)
months = bb-aa
if a_day > b_day: months -= 1
print(f"{name} is {months} months old")
