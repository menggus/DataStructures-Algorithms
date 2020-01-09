import random
from typing import List


def quick_sort(val: List[int], start: int, end: int):
    """
        快速排序算法
        最好时间复杂度：O(nlogn)
        最坏时间复杂度：O(n²)  总是只能划分2个区间情况时
        平均时间复杂度：O(nlogn)

        原地排序：空间复杂度 O(1)
        非稳定排序：可能打乱顺序
    :param val: 待排序序列
    :return: 
    """
    # start ~ end 区间只有一个元素时，直接返回
    if end - start <= 0:
        return 

    # 随机取一个值作为 区间分割值
    random_index = random.randint(start, end)
    val[start], val[random_index] = val[random_index], val[start]

    pivot = val[start]
    left, right = start, end

    while left < right:

        # val[right] >= pivot 中的 = 号是为了让，与pivot值相等的统一划分到右边
        while left < right and val[right] >= pivot:
            right -= 1
        
        # 在初次编写时，经常手动进行left的 移动， 这样如果经过上面循环直接 left=right 时，手动left += 1 操作会造成 left > right
        # 并且两次 val[left] = val[right] 和 val[right] = val[left] 会造成错乱， 所以提前 if left == right 时退出循环，
        # 其实这两条均可删除，在循环语句中自动进行left 和 right 移动
        # if left == right:
        #     break
        # val[left] = val[right]
        # left += 1
        val[left] = val[right]

        while left < right and val[left] < pivot:
            left += 1
        val[right] = val[left]
        
    val[left] = pivot
    quick_sort(val, start, left)
    quick_sort(val, left+1, end)



def quick_sort_test():
    a = []
    quick_sort(a, 0, 0)
    assert a == []
    b = [3, 2, 1, 0]
    quick_sort(b, 0, 3)
    assert b == [0, 1, 2, 3]
    c = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    quick_sort(c, 0, len(c)-1)
    assert c == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1, 0, len(a1)-1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2, 0, len(a2)-1)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3, 0, len(a3)-1)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4, 0, len(a4)-1)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    quick_sort_test()

    ist = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(ist, 0, len(ist)-1)
    print(ist)