score = input().split()
Sum = 0
for i in score:
    Sum += int(i)
print(Sum)
print("{:.1f}".format(Sum/len(score)))