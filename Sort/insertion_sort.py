def insertion_sort(val: list) -> list:
    """
        插入排序

        最好时间复杂度：O(n)   val原来有序
        最坏时间复杂度：O(n²)  val倒序
        平均时间复杂度：O(n²)

        原地排序：空间复杂度 O(1)
        稳定排序：相等不进行位置交换
    :param val: 待排序val
    :return: 
    """
    n = len(val)
    if n <= 1:
        return
    for i in range(1, n):
        current = val[i]  # 需要记录待插入值
        j = i-1
        while j >= 0 and val[j] > current:
            val[j+1] = val[j]
            j -= 1
        val[j+1] = current
        print("第{}次插入 - {}".format(i, val))


if __name__ == '__main__':
    ist = [3, 6, 4, 9, 99, 999, 0]
    insertion_sort(ist)
    print(ist)