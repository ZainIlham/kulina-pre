from collections import Counter

def sockMerchant(n, ar):
    C = map(int, ar)
    c = Counter(C)
    total = 0
    for i in c:
        total += c[i]//2
    return total

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(n, ar)
print(result)
