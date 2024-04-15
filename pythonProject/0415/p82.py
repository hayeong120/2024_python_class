table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
      print(str(col) + " ")
    print()

for i in range(1, 9+1):
    if i == 7:
        break
    print("2 X {} = {}".format(i, 2*i))

print()

for i in range(1, 9+1):
    if i % 2 == 0:
        continue
    print("2 X {} = {}".format(i, 2*i))