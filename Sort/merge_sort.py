from typing import List


def merge_sort(val: List[int]):
    """ 
        归并排序算法
        最好时间复杂度：O(nlogn)
        最坏时间复杂度：O(nlogn) 
        平均时间复杂度：O(nlogn)

        非原地排序：空间复杂度 O(n)
        稳定排序：相等不进行位置交换
    :param val: 待排序序列
    :return: 
    """
    n = len(val)
    if n <= 1:
        return val

    # 分解操作: 分解之后类似于 树, 深度为 log2(n) "2为底"
    mid = n // 2
    merge_left = merge_sort(val[:mid])
    merge_right = merge_sort(val[mid:])

    # 合并操作：对于树的同一深度的总合并时间为 n，则归并排序的时间复杂度为 O(nlogn)
    tmp = []  # 额外空间，非原地排序 O(n)
    left = 0
    right = 0
    while left <= len(merge_left)-1 and right <= len(merge_right)-1:
            if merge_left[left] <= merge_right[right]:
                tmp.append(merge_left[left])
                left += 1
            else:
                tmp.append(merge_right[right])
                right += 1
    # if left <= len(merge_left)-1:
    #     tmp.extend(merge_left[left:])
    # if right <= len(merge_right)-1:
    #     tmp.extend(merge_right[right:])
    # 由于Python切片的特性： a = [1,2,3] a[3:] = [],所以可省略 if 判断
    tmp.extend(merge_left[left:])
    tmp.extend(merge_right[right:])
    # print(tmp)
    return tmp

def merge_sort_test():
    a1 = []
    assert merge_sort(a1) == []
    a2 = [1]
    assert merge_sort(a2) == [1]
    a3 = [1, 2]
    assert merge_sort(a3) == [1, 2]
    a4 = [3, 6, 3, 4, 7, 0]
    assert merge_sort(a4) == [0, 3, 3, 4, 6, 7]


if __name__ == "__main__":
    merge_sort_test()
    ist = [3, 5, 2, 1, 7, 4, 9, 8, 6]
    sort_ist = merge_sort(ist)
    print(sort_ist)

    




