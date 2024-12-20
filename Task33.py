a = int(input())
b = int(input())
c = int(input())
mn = min(a, b, c)
mx = max(a, b, c)
md = a + b + c - mn - mx
print(mn, md, mx)