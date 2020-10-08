def flipSwitch(N):
    lamps = [False for i in range(0, N)]

    for i in range(1, N + 1):
        w = 1
        k = w * i

        while k < N:
            lamps[k - 1] = not lamps[k - 1]
            w += 1
            k = w * i

    counter = 0
    for lamp in lamps:
        if lamp == True:
            counter += 1

    return counter

res = flipSwitch(100)
print(res)