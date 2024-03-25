# 리스트 생성
l = []          #빈 리스트
player = ["Messi", 10, True]         # ['Messi', 10, True]
list("Happy")                        # ['H', 'a', 'p', 'p', 'y']
list((1125, 2436))                   # [1125, 2436]
list({"menu":"pizza","price":10000})        # ['menu', 'price']
list({"사과", "배"})                  # ['사과', '배']
nums = list(range(3))                # [0, 1, 2]

# 리스트에 요소 추가
print(nums)
nums + [10, 11]                  # [0, 1, 2, 10, 11]
print(nums)
nums += [10, 11]                 # [0, 1, 2, 10, 11]
print(nums)
nums.append(20)                  # [0, 1, 2, 10, 11, 20]
print(nums)
nums.append([30, 31])               # [0, 1, 2, 10, 11, 20, [30, 31]]
print(nums)
nums.insert(2,40)           # [0, 1, 40, 2, 10, 11, 20, [30, 31]]
print(nums)
nums.extend([50,51])             # [0, 1, 40, 2, 10, 11, 20, [30, 31], 50, 51]
print(nums)