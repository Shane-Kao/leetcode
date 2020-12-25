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
    def list_node_length(self, l):
        return 0 if l.next is None else 1 + self.list_node_length(l.next)

    def addTwoNumbers(self, l1, l2):
        result_list = []
        l1_len = self.list_node_length(l1)
        l2_len = self.list_node_length(l2)
        len_diff = l1_len - l2_len
        while True:
            l1_val = l1.val if len_diff >= 0 else 0
            l2_val = l2.val if len_diff <= 0 else 0
            sum_val = l1_val + l2_val
            # if len_diff < 0:
            #     len_diff += 1
            # if len_diff > 0:
            #     len_diff -= 1
            # print(len_diff)
            print(sum_val)
            if l1.next is None and l2.next is None:
                break
            l1 = l1.next if len_diff >= 0 else l1
            l2 = l2.next if len_diff <= 0 else l2




if __name__ == '__main__':
    # l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
    # l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
    # Solution().addTwoNumbers(l1=l1, l2=l2)
    #
    # l1 = ListNode(val=0, next=None)
    # l2 = ListNode(val=0, next=None)
    # Solution().addTwoNumbers(l1=l1, l2=l2)

    l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))))))
    l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None))))
    Solution().addTwoNumbers(l1=l1, l2=l2)