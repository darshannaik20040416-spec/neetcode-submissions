# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
            
                
        res.pop(-n)

        dummy = ListNode()
        tail = dummy
        for num in res:
            tail.next = ListNode(num)
            tail = tail.next



        return dummy.next
        