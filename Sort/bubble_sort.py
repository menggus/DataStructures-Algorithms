def bubble_sort(val: list):
    """
        冒泡排序算法
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
    for i in range(n):
        exchange = False  # 无位置交换，表示已有序
        for j in range(n-i-1):
            if val[j] > val[j+1]:
                val[j], val[j+1] = val[j+1], val[j]
                exchange = True
        print("第{}次冒泡 - {}".format(i, val))
        if not exchange:
            break


if __name__ == '__main__':
    ist = [1, 2, 4, 9, 99, 999, 0]
    bubble_sort(ist)
    print(ist)
