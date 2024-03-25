nums = list(range(3))
nums + [10, 11]
nums += [10, 11]
nums.append(20)
nums.append([30, 31])
nums.insert(2,40)
nums.extend([50,51])

# 리스트에 요소 수정
nums[7]             #[30, 31]
print(nums)
nums[7] = 60        #[0, 1, 40, 2, 10, 11, 20, 60, 50, 51]
print(nums)

# 리스트에서 요소 제거
del nums[2]             #[0, 1, 2, 10, 11, 20, 60, 50, 51]
print(nums)
nums.remove(20)             #[0, 1, 2, 10, 11, 60, 50, 51]
print(nums)
nums.pop()              #[0, 1, 2, 10, 11, 60, 50]
print(nums)
nums.pop(5)             #[0, 1, 2, 10, 11, 50]
print(nums)
nums.clear()            #[]

# 리스트에서 요소 검색
nums = list(range(3))       #[0, 1, 2]
print(nums)
nums += [100, 10]        #[0, 1, 2, 100, 10]
print(nums)
print(nums[3])
print(3 in nums)
print(10 in nums)