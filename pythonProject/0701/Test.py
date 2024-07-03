# 문자열을 반전시키는 함수 정의
def reverse_string(input_string):
    return input_string[::-1]

# 사용자로부터 문자열 입력 받기
user_input = input("문자열을 입력하세요: ")

# 입력받은 문자열을 반전시키고 출력하기
reversed_string = reverse_string(user_input)
print(f"반전된 문자열: {reversed_string}")
