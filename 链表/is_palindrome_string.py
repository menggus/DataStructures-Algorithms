from SingleLinked import Node, Linked
"""
    基于单链表的回文判断
    思路：
        1.采用两个游标cur，一个走一步，一个走二步；
        2.当快的游标走到尾部时，慢游标正好指向中间节点；
        3.慢游标走的时候同时对前段链表进行反序；
        4.进行比较前段链表与后段链表；
"""


class Palindrome:

    def __init__(self):
        self.linked = Linked()

    def generate_linked_str(self, string: str):
        """
            生成链表字符串
        :param string:
        :return:
        """
        strlist = list(string)
        for i in strlist:
            self.linked.insert(i)
        print(self.linked)

    def is_palindrome(self, val: str):
        """
            判断是否是回文
            定位中间节点 n/2 单位时间， 比较耗时 n/2，总耗时 n；时间复杂度 O(n)
        :param val: 需要判断的字符串
        :return: bool
        """
        # 生成链表字符串
        self.generate_linked_str(val)

        # 判断
        head = self.linked.head
        cur_1 = head  # 慢指针
        cur_2 = head  # 快指针
        pre = None  # 反序过程中类似于链表的头
        while cur_2.next is not None and cur_2.next.next is not None:
            cur_2 = cur_2.next.next  # 注意由于这里cur_1 和 cur_2均是执行head，所以cur_2下一个节点指向变化最好放前面

            current = cur_1
            cur_1 = cur_1.next
            current.next = pre
            pre = current

        # 通过判断链表为单数还是双数，构造反序链 和 后部链的头部
        if cur_2.next is None:
            cur_left = pre
            cur_right = cur_1.next
        else:
            cur_right = cur_1.next
            cur_1.next = pre
            cur_left = cur_1

        count = 0  # 记录比较次数
        while cur_left is not None:
            count += 1
            if cur_left.val != cur_right.val:
                print(cur_left.val, cur_right.val, count)
                return False
            cur_left = cur_left.next
            cur_right = cur_right.next
        return True


if __name__ == '__main__':
    links = Palindrome()
    print(links.is_palindrome("cabccbab"))
