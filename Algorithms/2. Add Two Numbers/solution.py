# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
        return 0 if self.next is None else 1 + len(self.next)


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        pass


if __name__ == '__main__':
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
    print(len(l1))
    Solution().addTwoNumbers(l1=l1, l2=l2)