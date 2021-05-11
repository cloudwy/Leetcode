"""
Muster 1
- 检索nums中等于target的元素，没有返回-1
- 注意：返回的索引随机，与nums的长度有关,不一定位于边界
"""
def binarySearch1(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

"""
- 查找大于或等于target的左边界
- 若该元素不在nums内，返回left = len(nums)
"""
def left_binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

#nums = [0, 0, 1, 2]
#ans = left_binarySearch(nums, target=3)
#print(ans)

"""
Muster 2
- 寻找大于等于target的最小值
"""
def left_binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    if left != len(nums) and nums[left] >= target:
        return left
    return -1

nums = [0, 0, 1, 3]
#ans = left_binarySearch(nums, target=0)
#print(ans)

"""
Muster2：
寻找大于target的最小值
代表例题：744
"""
def left_binarySearch2(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if left == len(nums):
        return -1
    else:
        return left

"""
Muster3: 寻找小于等于x的最大值
"""
def right_binarySearch(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1

    if(left != len(nums)) and nums[left] <= target:
        return left
    return -1;