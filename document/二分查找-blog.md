### 二分查找

### 二分查找的原理

-   原理图

    ![](http://im.taolius.com/image/bsearch.png)

    -   首先二分查找依赖于有序数据，例如图中的有序数组
    -   在查找开始前需要确认 最小索引与最大索引，也就是查找范围
    -   然后查找中间值与需要查找匹配，判断中间值是否为查找值
        -   中间值索引计算方式
            -   `mid=(low+high)/2 `，当low与high很大时，可能会溢出
            -   `mid=low+(high-low)/2`，解决溢出问题，但是效率还可以提升
            -   `mid=low+(high-low)>>1`，由于对于计算机来说，位操作比除法效率更高
    -   当中间值不是查找值时，如果中间值小于查找值，则`low=mid+1`，如果中间值大于查找值，则`high=mid-1`
    -   改变low或者high后，重新查找中间值，并与查找值进行比较，重复进行
    -   当low = high=mid后，还是无法查找到，则查找值不在数据中

### 简单实现

-   二分查找的终止条件：`low>high`，也就是说low=high=mid时，还需要进行一次判断

-   每次进行判断后，需要变换low与high的值，`low=mid+1 or high=mid-1`

    ```python
    # 简单的二分查找
    def bsearch(a: list[int], val: int):
        low = 0
        high = len(a) - 1
        while low <= high:
            mid = low + (high - low)>>1
            if a[mid] == val:
                return mid
            elif a[mid] < val: 
                low = mid + 1
            else: 
                high = mid - 1
        return -1
    ```

### 复杂度分析

-   二分查找的本质：不断的缩小[low，high]的区间来查找目标值，每次均缩小为原始数据的1/2，如果原始数据为n，查找次数为k，则 2^k=n, k=$\log_2{n}$，则可知时间复杂度为 `O(T)=O(logn)`

### 局限性

-   二分查找依赖顺序表结构

    因为在获取值时，顺序表随机访问时间为O(1)

-   二分查找目标数据为有序

    对于无序的目标数据，需要先进行排序，例如先用快速排序来排序，然后再进行查找，

    所以对于目标数据一次排序，多次查找的场景适合二分查找，

    而目标数据需频繁插入或删除操作场景，不推荐使用二分查找

-   数据量很小，遍历查找比二分查找更快

    如果在比较值的过程中非常耗时(存储的值比较复杂或者特别大)，为了减小比较过程耗时，推荐使用二分查找

-   数据量太大，也不推荐二分查找

    二分查找依赖数组，而数据对内存空间要求为连续的内存空间，所以对于大量的数据的场景也不使用二分查找

### 二分查找的变形问题

-   a. 查找 第一个，值等于给定值的元素；

    在数据中`1 2 3 4 5 5 5 6 7 8 9`查找第一个值等于 5  的元素

    从数据中可看出查找的就是   顺序的第一个 5

    ```python
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
    ```

-   b. 查找 最后一个，值等于给定值的元素；

    在数据中`1 2 3 4 5 5 5 6 7 8 9`查找第一个值等于 5  的元素

    从数据中可看出查找的就是   顺序的最后一个 5

    ```python
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
    ```

-   c. 查找 第一个，值大于等于给定值的元素；

     在数据中`1 2 3 4 6 7 8 9`查找第一个值大于等于 5 的元素

     从数据中可看出查找的就是   顺序的 6

    ```python
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
    ```

-   d. 查找 最后一个，值小于等于给定值的元素；

     在数据中`1 2 3 4 6 7 8 9`查找第一个值小于等于 5 的元素

     从数据中可看出查找的就是   顺序的 4

    ```python
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
    ```

### 二分查找思考题

-   如果有1000万条数据，每条数据占用8字节，实现在内存限制为100MB的情况下，实现查找某一整数；

    1000万条数据，每个字节占用8字节，用数组存储大约占用80MB，再使用二分查找即可

-   怎样通过二分查找，实现ip地址来查找到归属地，假设ip地址区间与归属地对应关系数据有12万条

    如果ip区间与归属地的对应关系不经常更新，我们可以先预处理者12万条数据，按照区间的起始值来进行排序，先将起始ip转换为32位整数，然后按照整数从小到大进行排序；

    然后通过二分查找 最后一个小于等于给定ip的起始ip，从而找到一个区间范围，然后判断给定ip地址是否存在于查找到的起始ip的区间范围内，如果存在则，同归对应关系，返回归属的；如果不存在，则返回未找到；