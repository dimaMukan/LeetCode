from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        while list2 and list1:
            if list1.val > list2.val:
                cur.next = list1.val
                list1 = list1.next
            else:
                cur.next = list2.val
                list2 = list2.next
            cur = cur.next
            cur.next = list2 or list1
            return head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

a1 = ListNode(2)
b1 = ListNode(1)
c1 = ListNode(7)
a1.next = b1
b1.next = c1

q = Solution()
q.mergeTwoLists(a,a1)
    #         arr = []
    #         while list1:
    #             if list1 is not None:
    #                 arr.append(list1.val)
    #                 list1 = list1.next
    #
    #         while list2:
    #             if list2 is not None:
    #                 arr.append(list2.val)
    #                 list2 = list2.next
    #
    #         arr.sort(reverse=True)
    #         print(arr)
    #
    #
    # a = ListNode(1)
    # b = ListNode(2)
    # c = ListNode(3)
    # a.next = b
    # b.next = c





