P = int(input())
V = int(input())
T = int(input())
T += 273.15
R = 8.314
n = (P * V) / (R * T)
print(n, 'моль')