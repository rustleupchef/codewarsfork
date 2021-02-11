def fib(last, next, num, s):
    s += str(last) + ","
    n = last + next
    if num == 1:
        return s[:-1]
    else:
        return fib(next, n, num-1 , s)



f = int(input())
n = int(input())
num = int(input())
print(fib(f,n,num,""))
