from copy import deepcopy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.header = ListNode(None)

    def create_list(self, v):
        p = self.header
        for i in v:
            p.next = ListNode(i)
            p = p.next

    def show(self):
        p = self.header.next
        while p is not None:
            print(p.val, end='->')
            p = p.next
        print('end')

class Solution:
    def removeNthFromEnd(self, header, n):
        # 快慢指针实现
        head = deepcopy(header)
        first = head.header.next
        for i in range(n):
            first = first.next
        second = head.header   # 这里指向头，以为需要找到待删除元素前一个元素
        while first is not None:
            first = first.next
            second = second.next
        r = second.next
        second.next = r.next
        del r
        return head

if __name__ == '__main__':
    # solution 1
    l, ln = LinkList(), LinkList()
    l.create_list([1, 2, 3, 4, 5])

    s = Solution()
    ln = s.removeNthFromEnd(l, 2)
    l.show()
    ln.show()


