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
        result_list = []
        extra_num = 0
        while True:
            try:
                l1_num = l1.pop()
            except IndexError:
                l1_num = 0
            try:
                l2_num = l2.pop()
            except IndexError:
                l2_num = 0
            num = l1_num + l2_num + extra_num
            extra_num = 1 if num >= 10 else 0
            result_list.append(num%10)
            if not len(l1) and not len(l2):
                if extra_num == 1:
                    result_list.append(1)
                break
        return result_list


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    l1 = [99]
    l2 = [3]
    # l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
    # l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
    # print(len(l1))
    print(Solution().addTwoNumbers(l1=l1, l2=l2))