f = open('filepath')
a = [int(i) for i in f]

k = 0
mx = float('-inf')
mn = float('inf')
for a1, a2 in zip(a, a[1:]):
    if ...:
        k += 1
        mx = max(mx, ...) # если в качестве второго вопроса найти минимум, то
                          # mn = min(mn, ...)


print(mx, mn)