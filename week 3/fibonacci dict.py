def fib_dict(n, d):
    if n in d:
        return d[n]
    else:
        d[n] = fib_dict(n-1,d) + fib_dict(n-2, d)
        return d[n]

d = {1:1, 2:1}
print(fib_dict(8, d))
