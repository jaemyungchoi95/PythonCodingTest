a = input().split()
m = int(a[0])
n = int(a[1])

for i in range(m, n+1):
    temp = 0
    for j in range(1, i+1):
        if i%j == 0:
            temp += 1
    if temp == 2:
        print(i)
