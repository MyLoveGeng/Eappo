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
        print('NULL')

class Solutions:
    def rotateRight(self, header, k):
        # 建立循环链表
        head = deepcopy(header)
        r = head.header
        length = 0
        while r.next is not None:
            length += 1
            r = r.next
        # print(length, r.val)
        r.next = head.header.next
        step = length - k % length
        # print(step, r.val)
        for i in range(step):
            r = r.next
        head.header.next = r.next
        r.next = None
        return head

if __name__ == '__main__':
    # solution 2
    l1, ln = LinkList(), LinkList()
    l1.create_list([1, 2, 3, 4, 5])
    s = Solutions()
    ln = s.rotateRight(l1, 2)
    l1.show()
    ln.show()

    print('--'*20)
    l1.create_list([0, 1, 2])
    ln = s.rotateRight(l1, 4)
    l1.show()
    ln.show()
