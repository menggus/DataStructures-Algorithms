### 排序

-   排序算法执行效率的分析要点
    -   最好、最坏、平均情况的时间复杂度
    -   空间复杂度
    -   排序是否稳定，是否会打乱相等元素的顺序
    
-   比较常用的，经典的排序算法

    | 排序方法 | 平均情况 | 最好情况 | 最坏情况 | 空间复杂度 | 稳定性 |
    | :------: | :------: | :------: | :------: | :--------: | :----: |
    | 冒泡排序 |  O(n²)   |   O(n)   |  O(n²)   |    O(1)    |  稳定  |
    | 插入排序 |  O(n²)   |   O(n)   |  O(n²)   |    O(1)    |  稳定  |
    | 选择排序 |  O(n²)   |  O(n²)   |  O(n²)   |    O(1)    | 不稳定 |
    | 归并排序 | O(nlogn) | O(nlogn) | O(nlogn) |    O(n)    |  稳定  |
    | 快速排序 | O(nlogn) | O(nlogn) |  O(n²)   |    O(1)    | 不稳定 |

### 冒泡排序 & 插入排序 &选择排序

-   冒泡排序

    -   冒泡排序的过程

        ![bubble-sort](%E6%8E%92%E5%BA%8F.assets/bubble-sort.png)

        一次冒泡过程（从小到大排序）：

        ​		每次从头两个数据开始，比较两数据的大小，如果左比右大，则交换左右位置，否则不交换。直到该次冒泡过程中的最大值，移动到靠右的位置

        ​		`i=0 比较val[i]与val[i+1] 判断是否交换位置`

        ​		`i=1 同样比较val[i]与val[i+1] 判断是否交换位置`

        ​		`...`

        经过多次冒泡，数据从大倒小，从右到左排序。

    -   动图

        ![bubble-sort-gif](%E6%8E%92%E5%BA%8F.assets/bubble-sort-gif.gif)
    
    -   代码
    
        ```python
        def bubble_sort(val: list):
            n = len(val)
            if n <= 1:
                return
            for i in range(n):
                exchange = False  # 优化：一次冒泡是否有位置交换，无位置交换表示已有序
                for j in range(n-i-1):
                    if val[j] > val[j+1]:
                        val[j], val[j+1] = val[j+1], val[j]
                    exchange = True
                if not exchange:
                break
        ```
    
    -   分析
    
        -   最好时间复杂度：当待排序的数据已有序，则只需要一次冒泡即可； O(n)
        -   最坏时间复杂度:   当待排序的数据正好为倒序，需要n次冒泡，则为最坏情况；O(n²)
        -   平均时间复杂度:   O(n²)
        -   是否为原地排序：排序过程是在当前序列进行，所以为原地排序；O(1)
           -   稳定性：稳定排序，判断位置交换的条件为大于，左右位置数据一样时，并不进行位置交换
    
-   插入排序

    -   插入排序过程

        ![insertion-sort](%E6%8E%92%E5%BA%8F.assets/insertion-sort.png)

        -   首先从第一个元素开始，从当前位置，向左进行插入；由于第一个元素左边无元素，则插入在当前位置；
        -   然后第二个元素进行插入，同样向左，判断邻近位置数据9, 由于9比8大，所以9右移一位，由于前面已无元素，则8插入；当元素比前一个元素小时，则插入到当前位置；
        -   同样的插入过程，直到最后一个元素插入完成；

    -   动态

        ![](%E6%8E%92%E5%BA%8F.assets/insertion-sort-gif.gif)
    
    -   代码
    
        ```python
        def insertion_sort(val:list):
            n = len(val)
            if n <= 1:
                return
            for i in range(1, n):  # 第一个位置前无数据，所以从第二个位置开始
                current = val[i]
                j = i-1
                while j >= 0 and val[j] > current:
                 val[j+1]=val[j]
                     j -= 1
            val[j+1] = value
        ```
    
    -   分析
    
        -   最好时间复杂度：当待排序的数据已有序，则插入过程每次只需要进行一次判断； O(n)
        -   最坏时间复杂度:   当待排序的数据正好为倒序，则为最坏情况；O(n²)
        -   平均时间复杂度:   O(n²)
        -   是否为原地排序：排序过程是在当前序列进行，所以为原地排序；O(1)
        -   稳定性：稳定排序，当插入过程判断碰到一样的数据，则立即插入值，不会打乱顺序；
    
-   选择排序

    -   选择排序过程

        ![selection_sort](%E6%8E%92%E5%BA%8F.assets/selection_sort.png)

        从index=0开始向右查找，假设index=0位置为最小值，向右找到真实最小值与交换位置，这样index=0位置就是整个排序的最小值，同样再从index=1开始向右查找最小值，与index=1的值交换位置，这样就index=1位置上就是整个排序的第2小值，同理直到排序完成

        选择排序的过程本质：就是从未排序的序列查找最小值放到已排序序列的末尾

    -   动图

        ![selection-sort-gif](%E6%8E%92%E5%BA%8F.assets/selection_sort.gif)

    -   代码

        ```python
        def selection_sort(val:list):
            n = len(val)
            if n <= 1:
                return
            for i in range(n-1):  
                mini = i  # 假定未排序区间第一个位置最小值
                for j in range(i+1, n):
                    if val[j] < val[mini]:
                        mini = j
                val[i], val[mini] = val[mini], val[i]
        ```

    -   分析

        -   最好时间复杂度：当待排序的数据已有序，但查找未排序区间的最小值，还是会全部遍历； O(n²)
        -   最坏时间复杂度:   O(n²)
        -   平均时间复杂度:   O(n²)
        -   是否为原地排序：排序过程是在当前序列进行，所以为原地排序；O(1)
        -   稳定性：不稳定排序，在与未排序区间的最小值交换位置可能会打乱顺序；

        
