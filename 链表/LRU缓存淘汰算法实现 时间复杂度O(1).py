"""
    基于链表实现 LRU 缓存淘汰算法
    LRU：最近最少使用原则
    双向链表 + 哈希表

    时间复杂度为 O(1)

    1. 维护一个双向链表，链表节点存储均为缓存数据，越靠近链表尾部的数据为最近最少使用的数据；
    2. 当新的数据到来时，先遍历链表，查看新的数据是否在链表中；
        a.在链表中，则删除旧的节点，然后重新插入到头节点
        b.不在链表中，则先判断链表是否已满
            1.没满，则直接插入到头节点
            2.已满，则先删除最后一个节点，然后再把心数据，插入到头节点


    重点知识：
        1. 链表的遍历，添加，删除节点等操作
        2. 哈希表读取值的时间复杂度 O(1)

"""


class LinkedNode:

    def __init__(self, key=None, value=None):
        """
            "key & value":
        :param key:
        :param value:
        """
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRU:

    def __init__(self, capacity: int):
        """
            初始化
        :param capacity: 链表容量
        """
        self.head_sentinel = LinkedNode()  # 头哨兵
        self.tail_sentinel = LinkedNode()  # 尾哨兵
        self.head_sentinel.next = self.tail_sentinel
        self.tail_sentinel.pre = self.head_sentinel
        self.capacity = capacity  # 链表容量，缓存大小
        self.hkeys = {}  # 链表实际长度
        self.cur = None  # 记录检测到存在节点

    def exitst(self, key: int) -> bool:
        """
            检测data是否存在于 链表中
            需要遍历链表，时间复杂度为 O(1)
        :param key:  哈希表的key
        :param data: 被检测数据data
        :return: bool
        """
        if len(self.hkeys) != 0:
            if key in self.hkeys.keys():
                return True
        return False

    def used_data(self, key: int, value: int) -> bool:
        """
            输入数据的进行缓存
        :param value: 数据值
        :param key: 数据key
        :return:
        """
        # 数据存在时操作
        if self.exitst(key):
            # 删除旧的结点
            self.hkeys[key].pre.next = self.hkeys[key].next
            self.hkeys[key].next = self.hkeys[key].pre
            # 把旧的结点插入头节点后
            self.hkeys[key].next = self.head_sentinel.next
            self.head_sentinel.next.pre = self.hkeys[key]
            self.hkeys[key].pre = self.head_sentinel
            self.head_sentinel.next = self.hkeys[key]
            return True

        # 数据不存在
        node = LinkedNode(key, value)

        # 判断链表容量是否已满
        if len(self.hkeys) == self.capacity:
            self.hkeys.pop(self.tail_sentinel.pre.key)
            self.tail_sentinel.pre.pre.next = self.tail_sentinel
            self.tail_sentinel.pre = self.tail_sentinel.pre.pre
        node.next = self.head_sentinel.next
        node.pre = self.head_sentinel
        self.head_sentinel.next = node
        node.next.pre = node

        # 添加新数据到哈希表
        self.hkeys[key] = node
        return True

    def __str__(self):
        """
            打印输出字符串
        :return: 输出字符串
        """
        cursor = self.head_sentinel.next
        alist = list()
        while cursor is not self.tail_sentinel:
            alist.append(str(cursor.value))
            cursor = cursor.next
        return "<=>".join(alist)


if __name__ == '__main__':
    lru = LRU(5)
    lru.used_data(5, 5)
    lru.used_data(6, 6)
    lru.used_data(3, 3)
    lru.used_data(7, 7)
    lru.used_data(8, 8)
    lru.used_data(9, 9)
    lru.used_data(3, 3)
    print(lru)
