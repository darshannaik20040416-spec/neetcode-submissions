# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res = []

        while cur:
            res.append(cur.val)
            cur = cur.next

        res.reverse()

        dummy = ListNode()
        tail = dummy
        for num in res:
            tail.next = ListNode(num)
            tail = tail.next

        return dummy.next