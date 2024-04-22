x = 3
while x < 6:
    print(x)
    x += 1

echo = input()
while echo != "exit":       # 변수가 exit가 아니면 코드 블록을 실행한다.
    print(echo)
    echo = input()          # 새로 입력을 받아 변수를 바꾼다.

echo = input()
while True:                 # 코드 블록을 무한 반복한다.
    if echo == "exit":
        break
    print(echo)
    echo = input()