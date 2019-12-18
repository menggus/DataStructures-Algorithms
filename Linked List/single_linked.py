"""
    基于单链表的回文判断

"""


class Node:

    def __init__(self, value: str):
        self.val = value
        self.next = None


class Linked:

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
            头部插入数据
        :param value:
        :return:
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def __str__(self) -> str:
        """
            打印链表
        :return:
        """
        alist = list()
        cur = self.head
        while cur is not None:
            alist.append(cur.val)
            cur = cur.next

        return "=>".join(alist)


if __name__ == '__main__':
    link = Linked()
    link.insert("a")
    link.insert("b")
    link.insert("c")
    link.insert("c")
    link.insert("b")
    link.insert("a")
    print(link)

