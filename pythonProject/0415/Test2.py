n = int(input())
day30 = [4,6,9,11]
day31 = [1,3,5,7,8,10,12]
if n == 2:
    print("28일까지 입니다.")
elif n in day30:
    print("30일까지 입니다.")
elif n in day31:
    print("31일까지 입니다.")
else:
    print("없는 달입니다.")