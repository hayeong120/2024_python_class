# 문제) Hello Python, one two three four 에서 반복문을 이용하여 문자 'o'를 제거하시오

a = "Hello Python, one two three four"
b = ' '
for i in a :
    if i != 'o':
        b += i
print(b)

c = list('Hello Python, one two three four')
while c.count('o') != 0 :
    c.remove('o')
print(c)
