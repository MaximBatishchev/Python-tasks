from math import *
s1 = int(input())
s2 = int(input())
s3 = int(input())
s = (s1 + s2 + s3) / 2
print(sqrt(s * (s - s1) * (s - s2) * (s - s3)))