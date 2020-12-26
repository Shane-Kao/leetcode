# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
# Definition for singly-linked list.
import functools


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
    def carry_digit(l):
        while any([i >= 10 for i in l]):
            for i, j in enumerate(l):
                if j >= 10:
                    l[i] = j - 10
                    try:
                        l[i + 1] += 1
                    except IndexError:
                        l.append(1)
                    break
        return l

    def addTwoNumbers(self, l1, l2):
        result_list = []
        while True:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            if l1 is None and l2 is None:
                break
            sum_val = l1_val + l2_val
            result_list.append(sum_val)
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        result_list = self.carry_digit(result_list)
        list_node_ = None
        for i in reversed(result_list):
            list_node_ = ListNode(val=i, next=list_node_)
        return list_node_


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