"""
1. 插入排序 - insert sort
https://www.runoob.com/python3/python-insertion-sort.html
"""
def insert_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
  return arr

"""
2. 冒泡排序
"""
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr


"""
3. 希尔排序
"""
def shell_sort(arr):
    n = len(arr)
    gap = int(n/2)
    while gap>0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = int(gap/2)
    return arr


"""
4. 快速排序
"""
"""
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
"""


def quick_sort(arr,i,j):
    if i >= j:
        return
    pivot = arr[i]
    low = i
    high = j
    while i < j:
        while i < j and arr[j] >= pivot: #大于等于pivot, j向左移，若小于，则arr[i]等于该值
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <=pivot: #小于等于pivot，i向右移，arr[j]等于该值
            i += 1
        arr[j] = arr[i]
    arr[j] = pivot
    quick_sort(arr, low, i-1)
    quick_sort(arr, i+1, high)
    return arr


"""
5. 选择排序
"""
def selection_sort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[min_idx] > arr[j]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)


"""
6. 归并排序
"""


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)
    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        # 归并临时数组到 arr[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # 拷贝 L[] 的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # 拷贝 R[] 的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

arr = [8, 3, 10, 9, 1, 5]
#insert_sort(arr)
#bubble_sort(arr)
#shell_sort(arr)
quick_sort(arr, 0, len(arr)-1)
#selection_sort(arr)
#merge_sort(arr, 0, len(arr)-1)