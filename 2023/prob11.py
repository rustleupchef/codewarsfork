n = int(input())

full, partial = n // 4, n % 4
arr =[]
if full == 1:
    arr.append("1 full car")
elif full > 1:
    arr.append(f"{full} full cars")

if partial: arr.append("1 partial car")

print(', '.join(arr))
