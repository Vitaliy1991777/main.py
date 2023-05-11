for i in range(1, 21)
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    print(i, s)
