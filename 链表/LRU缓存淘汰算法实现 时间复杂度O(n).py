"""
    基于链表实现 LRU 缓存淘汰算法
    LRU：最近最少使用原则

    时间复杂度为 O(n)

    1. 维护一个双向链表，链表节点存储均为缓存数据，越靠近链表尾部的数据为最近最少使用的数据；
    2. 当新的数据到来时，先遍历链表，查看新的数据是否在链表中；
        a.在链表中，则删除旧的节点，然后重新插入到头节点
        b.不在链表中，则先判断链表是否已满
            1.没满，则直接插入到头节点
            2.已满，则先删除最后一个节点，然后再把心数据，插入到头节点

"""


class LinkedNode:

    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None

    def __str__(self):

        return str(self.data)


class LRU:

    def __init__(self, capacity: int):
        """
            初始化
        :param capacity: 链表容量
        """
        self.head_sentinel = LinkedNode("|")  # 头哨兵
        self.tail_sentinel = LinkedNode("|")  # 尾哨兵
        self.head_sentinel.next = self.tail_sentinel
        self.tail_sentinel.pre = self.head_sentinel
        self.capacity = capacity  # 链表容量，缓存大小
        self.length = 0  # 链表实际长度
        self.cur = None  # 记录检测到存在节点

    def exitst(self, data: int) -> bool:
        """
            检测data是否存在于 链表中
            需要遍历链表，时间复杂度为 O(n)
        :param data: 被检测数据data
        :return: bool
        """
        if self.length == 0:
            return False
        cursor = self.head_sentinel.next
        while cursor is not self.tail_sentinel:
            if cursor.data == data:
                self.cur = cursor
                return True
            cursor = cursor.next

        return False

    def used_data(self, data) -> bool:
        """
            数据的缓存
        :param data:
        :return:
        """
        # 数据存在时操作
        if self.exitst(data):
            # 删除旧的结点
            self.cur.pre.next = self.cur.next
            self.cur.next = self.cur.pre
            # 把旧的结点插入头节点后
            self.cur.next = self.head_sentinel.next
            self.head_sentinel.next.pre = self.cur
            self.cur.pre = self.head_sentinel
            self.head_sentinel.next = self.cur
            self.cur = None
            return True
        # 数据不存在
        node = LinkedNode(data)

        # 判断链表容量是否已满
        if self.length == self.capacity:
            self.tail_sentinel.pre.pre.next = self.tail_sentinel
            self.tail_sentinel.pre = self.tail_sentinel.pre.pre

        node.next = self.head_sentinel.next
        node.pre = self.head_sentinel
        self.head_sentinel.next = node
        node.next.pre = node

        self.length += 1
        return True

    def __str__(self):
        """
            打印
            实际复杂度 O(n)
        :return:
        """
        if self.length == 0:
            return ""
        cursor = self.head_sentinel.next
        alist = list()
        while cursor is not self.tail_sentinel:
            alist.append(str(cursor.data))
            cursor = cursor.next
        return "<=>".join(alist)


if __name__ == '__main__':
    lru = LRU(10)
    lru.used_data(5)
    lru.used_data(6)
    lru.used_data(3)
    lru.used_data(7)
    lru.used_data(4)
    lru.used_data(5)
    print(lru)
    print(lru.length)




























