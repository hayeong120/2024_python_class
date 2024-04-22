F = 1
n = int(input())
for i in range(1,n+1):
    F *= i
print("{}! = {}".format(n, F))