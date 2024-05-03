#문자 1) 1부터 100까지의 합
# for문, while문 두 방법으로 해결
sum=0
for i in range(1, 101):
    sum += i
print(sum)

sum=0
i=1
while i<= 100:
    sum+=i
    i+=1
print(sum)

#문자 2) 문자열을 이용하여 369게임을 했을 때,
# 1부터 100까지 진행하여 박수를 친 횟수를 출력하는 코드
cnt=0
for i in range(1, 101):
    i = str(i)
    if i[-1] == '3' or i[-1] == '6' or i[-1] == '9': cnt+=1
print(cnt)

#문자 3) 입력받은 정수 n이 소수인지 판별하는 코드를 작성하시오
n = int(input())
for i in range(2, n):
    if n%i==0:
        print("소수가 아닙니다.")
        break;
    elif i == n-1:
        print("소수입니다.")

#문자 4) 별찍기
for i in range(1, 6):
    for j in range(1, 6):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()