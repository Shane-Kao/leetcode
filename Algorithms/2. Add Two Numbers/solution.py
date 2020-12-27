# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        result_list = []
        curr_ = self
        while True:
            result_list.append(str(curr_.val))
            if curr_.next is None:
                return ' '.join(result_list)
            curr_ = curr_.next


class Solution(object):
    @staticmethod
    def set_next(l, val):
        l_ = l
        while True:
            next_ = l_.next
            if next_ is None:
                return setattr(l_, 'next', val)
            l_ = l_.next

    def addTwoNumbers(self, l1, l2):
        list_node = None
        extra_val = 0
        while True:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            if l1 is None and l2 is None:
                if extra_val:
                    self.set_next(list_node, ListNode(val=extra_val))
                break
            sum_val = l1_val + l2_val + extra_val
            val_ = sum_val % 10
            extra_val = int(sum_val/10)
            if list_node is None:
                list_node = ListNode(val=val_)
            else:
                self.set_next(list_node, ListNode(val=val_))
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        return list_node


if __name__ == '__main__':
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
    # 342 + 465 = 807, [7, 0, 8]
    result_list = Solution().addTwoNumbers(l1=l1, l2=l2)
    print(result_list)

    l1 = ListNode(val=0, next=None)
    l2 = ListNode(val=0, next=None)
    result_list = Solution().addTwoNumbers(l1=l1, l2=l2)
    print(result_list)

    l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))))))
    l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None))))
    # 9999999 + 9999 = 10009998, [8, 9, 9, 9, 0, 0, 0, 1]
    result_list = Solution().addTwoNumbers(l1=l1, l2=l2)
    print(result_list)

    l1 = ListNode(val=9, next=ListNode(val=2, next=ListNode(val=3, next=None)))
    l2 = ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6, next=None)))
    # 329 + 654 = 983, [3, 8, 9]
    result_list = Solution().addTwoNumbers(l1=l1, l2=l2)
    print(result_list)

    l1 = ListNode(val=1, next=ListNode(val=7, next=ListNode(val=3, next=None)))
    l2 = ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6, next=None)))
    # 371 + 654 = 1025, [5, 2, 0, 1]
    result_list = Solution().addTwoNumbers(l1=l1, l2=l2)
    print(result_list)
    
    l1 = ListNode(val=7, next=ListNode(val=1, next=None))
    l2 = ListNode(val=6, next=None)
    # 17 + 6 = 23, [3, 2]
    result_list = Solution().addTwoNumbers(l1=l1, l2=l2)
    print(result_list)