from datetime import date

months = ['', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
dows = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

dow, month, day = input().split()
dow = dows.index(dow)
month = months.index(month)
day = int(day)

a, b = map(int, input().split('-'))
while a <= b:
    try:
        if date(a, month, day).weekday() == dow:
            print(a)
    except:
        pass
    a += 1