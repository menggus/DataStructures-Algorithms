from typing import List

# 简单的二分查找
def bsearch(a: List[int], val: int) -> int:
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low)>>1)
        if a[mid] == val:
            return mid
        elif a[mid] < val: 
            low = mid + 1
        else: 
            high = mid - 1
    return -1

# 查找 第一个，值等于给定值的元素
def bsearch_first_equal_val(a: List[int], val: int) -> int:
    low = 0
    high = len(a)-1
    while low <= high:
        mid = low + ((high-low) >> 1)  # 注意：位操作优先级在 加减 之后
        if a[mid] > val:
            high = mid - 1
        elif a[mid] < val:
            low = mid + 1
        else:
            if mid == 0 or a[mid-1] != val:  
                return mid
            else:
                high = mid - 1
    return -1

# 查找 最后一个，值等于给定值的元素
def bsearch_last_equal_val(a: List[int], val: int):
    low = 0
    high = len(a)-1
    while low <= high:
        mid =  low + ((high-low) >> 1)
        if a[mid] > val:
            high = mid - 1
        elif a[mid] < val:
            low = mid + 1
        else:
            if mid == len(a)-1 or a[mid+1] != val:  
                return mid
            else:
                low = mid + 1
    return -1

# 查找 第一个，值大于等于给定值的元素
def bsearch_first_mt_equal_val(a: List[int], val: int):
    low = 0
    high = len(a)-1
    while low <= high:
        mid =  low + ((high-low) >> 1)
        if a[mid] >= val:
            if mid == 0 or a[mid-1] < val:
                return mid
            else:
            	high = mid - 1
        else:
            low = mid + 1
    return -1

# 查找 最后一个，值小于等于给定值的元素
def bsearch_last_lt_equal_value(a: List[int], val: int):
    low = 0
    high = len(a)-1
    while low <= high:
        mid =  low + ((high-low) >> 1)
        if a[mid] <= val:
            if mid == len(a)-1 or a[mid+1] > val:
                return mid
            else:
            	low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    # print(bsearch(a, 5)) 
    # print(bsearch_first_equal_val(a, 5))
    # print(bsearch_last_equal_val(a, 5))

    b = [1, 2, 3, 4, 6, 7, 8, 9]
    # print(bsearch_first_mt_equal_val(b, 5))
    print(bsearch_last_lt_equal_value(b, 5))