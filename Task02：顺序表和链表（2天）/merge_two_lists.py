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
            elem = ListNode(i)
            p.next = elem
            p = p.next

    def show(self):
        p = self.header.next
        while p is not None:
            print(p.val, end='->')
            p = p.next
        print('end')

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ln = LinkList()
        p, q, r = l1.header.next, l2.header.next, ln.header
        while (p is not None) and (q is not None):
            if p.val <= q.val:
                r.next = ListNode(p.val)
                p = p.next
            else:
                r.next = ListNode(q.val)
                q = q.next
            r = r.next
        if q is None:
            r.next = p
        else:
            r.next = q
        return ln


if __name__ == '__main__':
    l1, l2, l3 = LinkList(), LinkList(), LinkList()
    l1.create_list([1, 2, 4])
    l1.show()
    l2.create_list([1, 3, 4])
    l2.show()

    s = Solution()
    l3 = s.mergeTwoLists(l1, l2)
    l3.show()



