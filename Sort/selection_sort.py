def selection_sort(val: list) -> list:
    """
        选择排序
        最好时间复杂度：O(n)   val原来有序
        最坏时间复杂度：O(n²)  val倒序
        平均时间复杂度：O(n²)

        原地排序：空间复杂度 O(1)
        不稳定排序：相等可能位置进行交换
    :param val: 待排序val
    :return: 
    """
    n = len(val)
    if n <= 1:
        return
    for i in range(n-1):
        mini = i  # 记录最小值下标
        for j in range(i+1, n):
            if val[j] < val[mini]:
                mini = j
        val[i], val[mini] = val[mini], val[i]
        print("第{}次选择 - {}".format(i, val))


if __name__ == '__main__':
    ist = [9999, 99999, 999, 99, 9]
    selection_sort(ist)
    print(ist)
