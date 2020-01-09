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

        ![](http://im.taolius.com/image/sort-bubble-sort.png)

        一次冒泡过程（从小到大排序）：

        ​		每次从头两个数据开始，比较两数据的大小，如果左比右大，则交换左右位置，否则不交换。直到该次冒泡过程中的最大值，移动到靠右的位置

        ​		`i=0 比较val[i]与val[i+1] 判断是否交换位置`

        ​		`i=1 同样比较val[i]与val[i+1] 判断是否交换位置`

        ​		`...`

        经过多次冒泡，数据从大倒小，从右到左排序。

    -   动图

        ![](http://im.taolius.com/image/sort-bubble-sort-gif.gif)
    
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

        ![](http://im.taolius.com/image/sort-insertion-sort.png)

        -   首先从第一个元素开始，从当前位置，向左进行插入；由于第一个元素左边无元素，则插入在当前位置；
        -   然后第二个元素进行插入，同样向左，判断邻近位置数据9, 由于9比8大，所以9右移一位，由于前面已无元素，则8插入；当元素比前一个元素小时，则插入到当前位置；
        -   同样的插入过程，直到最后一个元素插入完成；

    -   动态

        ![](http://im.taolius.com/image/sort-insertion-sort-gif.gif)
    
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

        ![](http://im.taolius.com/image/sort-selection_sort.png)

        从index=0开始向右查找，假设index=0位置为最小值，向右找到真实最小值与交换位置，这样index=0位置就是整个排序的最小值，同样再从index=1开始向右查找最小值，与index=1的值交换位置，这样就index=1位置上就是整个排序的第2小值，同理直到排序完成

        选择排序的过程本质：就是从未排序的序列查找最小值放到已排序序列的末尾

    -   动图

        ![](http://im.taolius.com/image/sort-selection-sort-gif.gif)

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

-   插入排序为何优于冒泡排序？

    -   首先插入排序与冒泡排序在 时间复杂度、空间复杂度、以及稳定性方面，均是相同
    -   主要优势：插入排序的核心循环部分是比较之后进行值的移动，而冒泡排序需要进行位置的交换；所以在CPU执行层面来看冒泡排序的执行指令要比插入排序多；在实际的测试中，处理同样随机数据时插入排序总是比冒泡排序花费时间少

### 归并排序 & 快排

-   归并排序

    -   归并排序的过程

        ![](http://im.taolius.com/image/sort-merge-sort.png)

        归并排序的过程分为 分解过程和归并过程；

        分解过程：就是把数据分解为单一的一个元素，这样对于单一元素就是有序的

        归并过程：对子序列进行合并，合并过程中进行排序

    -   动图

        ![](http://im.taolius.com/image/sort-merge-sort-gif.gif)

    -   代码

        ```python
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
            # 注意由于Python切片的特性： a = [1,2,3] a[3:] = [],所以可省略 if 判断
            tmp.extend(merge_left[left:])
            tmp.extend(merge_right[right:])
            # print(tmp)
            return tmp
        
        if __name__ == "__main__":
            ist = [3, 5, 2, 1, 7, 4, 9, 8, 6]
            sort_ist = merge_sort(ist)
            print(sort_ist)
        ```
    
-   分析
  
    -   最坏、最好、平均情况时间复杂度均为 O(nlogn)
    -   属于非原地排序：在合并子序列并进行排序时，需要一个临时的序列空间进行存储已排序的数据；O(n)
    -   稳定性：属于稳定排序，不会打乱元素顺序
    
-   快排

    -   快排过程

        ![](http://im.taolius.com/image/sort-quick-sort.png)

        快排的过程主要是：通过获取随机的pivot值来进行，区间划分，大于pivot放在一个子序列区间，小于pivot放在一个子序列区间，对子序列进行同样，直到子序列为一个元素；这样序列就已为有序；

        快排与归并排序的异同：

        ![](http://im.taolius.com/image/sort-quick-sort-2.png)

        快排是：边分解边排序

        归并是：先分解完，再执行子序列的合并排序

    -   动图

        ![](http://im.taolius.com/image/sort-quick-sort-gif.gif)

    -   代码

        ```python
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
                
        if __name__ == "__main__":
            ist = [5, -1, 9, 3, 7, 8, 3, -2, 9]
            quick_sort(ist, 0, len(ist)-1)
            print(ist)
        ```
        
    -   分析
      
        -   最好时间复杂度、平均时间复杂度为 O(nlogn)
        -   最坏时间复杂度：O(n²)   当pivot划分时，每次只能划分两个区间，即pivot和另一区间时，为最坏情况
        -   原地排序：空间复杂度 O(1)
        -   稳定性： 不稳定，因为pivot划分时，每次与pivot比较，如 `5  2  5  1`，在以2作为pivot时，前面的5就会跑到1的位置，而打乱顺序

### 桶排序 & 计数排序 & 基数排序

-   桶排序

    -   桶排序原理

        ![](http://im.taolius.com/image/sort-bucket-sort.png)

        核心思想：通过把数据分别放到 **有序** 的桶内，每一个桶单独进行排序，然后再依次从有序桶中取出数据，取出的数据即为有序数据

        如上图，已知数据分布为 0 ~ 30 ，设置3个桶，分别为 0~10、11~20、21~30的有序桶，遍历数据依次放入桶内，如图中桶内的数据，然后进行单独排序，然后依次取出，得到有序数据`2 3 9 11 15 23 24 27`

    -   分析

        -   时间复杂度分析：
          n个数据，均匀放到m个桶内，如果每个桶内的数据采用快排来进行排序，那么每个桶内的时间复杂度`O(k*logk)`  总的时间复杂度`O(m*k*logk)`， k=n/m，则时间复杂度`O(m*n/m*log(n/m) => O(nlog(n/m))`当桶的数量趋近于n时，n/m为一个很小常量，桶排序时间复杂度趋近于 O(n）
        
    -   桶排序的局限性
      
      -   需要排序的数据是否能划分为m个桶，每个桶之间是否有序
      -   桶内数据是否均匀，如果m个桶之内只有一个桶有数据，如果采用快排，时间复杂度会退化到 `O(nlogn)`
      
    -   桶排序的应用

        -   桶排序适合用于 **外部磁盘数据的排序**，一般数据很大，且无法一次性加载进内存

            假设有10GB的订单数据需要按订单金额进行排序，并且假设我们内存有限，无法一次性加载，那怎么进行排序呢？

            -   先对10GB数据进行扫描，找出最大值与最小值，假设最大值为1000元，最小值为1元；
            -   根据最小值到最大值范围来设定桶，假设桶的范围设定为1-100元，101-200元，....，901-1000元十个桶，如果10GB数据均匀分配的话，每个桶大约1GB数据；
            -   如果说1GB数据也加载不了，可以分更多的桶，来减少每个桶的数据量。假设桶范围设置为1-10元，11-20元等，则可设定为100个桶，平均每个桶的数据大约也就10GB/100，也就100多MB。
            -   如果不能均匀分布，总有某些范围值较大，假设101-200元的桶数据量很大，而其他桶都较小；我们就可以对101-200范围的桶再进行桶排序，把在101-200元范围的数据，再分10个桶，或者100个桶，直到能达到要求为止

-   计数排序

    -   计数排序原理

        ![](http://im.taolius.com/image/sort-counting-sort.png)

        计数排序其实是一种特别的桶排序，每个桶只放入相同的值，桶的多少依据最大值max为max+1个桶，分别为

        ​		`0 ，1， 2， 3， 4， ...，max`

        ​		每个桶统计了桶对应的值的个数，然后通过一种巧妙方式  计算**小于等于**当前值的个数，来计算桶对应值在有序序列R中的位置，来实现排序

    -   动图

        ![](http://im.taolius.com/image/sort-counting-sort-gif.jpg)

    -   局限性和应用

        -   计算排序只适用于范围不大的情况，如果计数范围大于数据的个数，那就不合适了，因为那样大部分执行时间都花费在无用值的计数上面；原理图中的第三步，计算小于等于当前值的个数；
        -   计数排序只使用正整数，而对于那些小数，负数需要在不改变原书记相对大小情况下转换为正整数；如对于均为保留一位小数的数值1.1需要进行乘10转换为11；对于均为负整数的值，如-1等需要进行 +1 转换为1，正整数之后进行排序

-   基数排序

    -   原理图

        ![](http://im.taolius.com/image/sort-radix-sort.png)

        我们如果需要对类似上图的数据可区分高位，低位，进行排序时，如果a的高位以及比b大了，那么数据就已经有序，不需要再比较低位了，只需要再对于同一位相等的数据进行排序即可；

        这里采用从低位到高位进行排序，因为低位有序后，同一高位相同的数据也就有序了；但是为了保证刚刚前面所说的机制，单个位上的排序方式必须是 **稳定排序**，否则前面的机制就无意义了；

        计数排序方法：

        -   要求数据可分割出 **位**，且位与位之间需存在递进关系

        -   从低位到高位进行排序
        -   排序算法需要是 **稳定排序**

    -   动图

        ![](http://im.taolius.com/image/sort-radix-sort-gif.gif)

    -   分析

        -   时间复杂度

            对于每一位均需要进行n个数据的排序（桶排序。计数排序），如果数据有k位，则时间复杂度为`O(k*n)`，对于类似于手机号码等11位的数据`O(11*n)`，时间复杂度就为 `O(n)`

        -   基数排序每一位的范围不能太大，因为基数排序也需要借助桶排序和计数排序来实现各位上的排序

    -   应用

        -   对于不等长，也就是位数不一样的数据，查看是否可以通过 **补位** 来进行操作；
