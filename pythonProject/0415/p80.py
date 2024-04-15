# 2단 출력
for i in range(1, 9+1):
    print("2 x {} = {}".format(i, 2*i))
# 3단 출력
for i in range(1, 9 + 1):
    print("3 x {} = {}".format(i, 3 * i))
# 4단 출력
for i in range(1, 9 + 1):
    print("4 x {} = {}".format(i, 4 * i))
# 5단 출력
for i in range(1, 9 + 1):
    print("5 x {} = {}".format(i, 5 * i))


# 2~5단 출력
for dan in range(2, 5+1):
    for i in range(1, 9+1):
        print("{} X {} = {}".format(dan, i, dan*i))
    print('---------------')