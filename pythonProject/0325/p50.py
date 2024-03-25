# 기타 리스트 관련 함수
nums = [0, 1, 2, 100, 10]
print(len(nums))          #[0, 1, 2, 100, 10]
nums.sort()               #[0, 1, 2, 10, 100]
print(nums)
nums.reverse()            #[100, 10, 2, 1, 0]
print(nums)
print(nums.count(2))

# range 함수
print(range(3))
print(range(1, 10))
print(range(1, 10, 2))
print(set(range(1, 10, 2)))
print(list(range(1, -5, -2)))
for i in range(3): print(i)