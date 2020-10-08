def countingValleys(n, steps):
    seaLevel = valleys = 0

    for step in steps:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1

        if step == 'U' and seaLevel == 0:
            valleys += 1

    return valleys

n = 8
steps = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
res = countingValleys(n, steps)
print(res)