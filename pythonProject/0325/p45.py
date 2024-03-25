h = "  Happy Programming! "
print(len(h))           # 글자 수 세기
print(h.count("p"))     # h 문자열에서 인자 'p'의 개수 세기
print(h.upper())        # 모두 대문자로 변환하기
print(h.lower())        # 모두 소문자로 변환하기
print(h.strip())        # 왼쪽, 오른쪽 모두 공백 없애기
print(h.replace("Happy", "Funny"))      #문자열 대체하기
print(h.find("ap"))     # h 문자열에서 인자 'ap'를 왼쪽부터 찾기
print(h.rfind("a"))     # h 문자열에서 인자 'a'를 오른쪽부터 찾기
print(h.find("zoo"))    # 찾지 못하면 –1 리턴

print("a" in h)         # h 문자열에 'a'가 있는지 확인하기
print("amp" in h)       # h 문자열에 'amp'가 있는지 확인하기
x = "01::23::ab::&&"
y = x.split("::")       # x 문자열을 '::'로 나누어 리스트 만들기
print(y)
print(", ".join(y))     # y 리스트를 ', '로 이어서 문자열 만들기
