from sys import stdin
import math

n, m = map(int, stdin.readline().split())
print(math.gcd(n,m))
print(math.lcm(n,m))