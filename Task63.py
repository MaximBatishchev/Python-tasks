tot = 0
cnt = 0
while True:
    a = int(input())
    if a == 0:
        break
    tot += a
    cnt += 1
print(tot / cnt)
