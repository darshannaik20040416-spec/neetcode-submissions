# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2
        res1 = ""
        res2 = ""
        string = ""

        while cur1 and cur2:
            res1 = str(cur1.val) + res1 
            res2 = str(cur2.val) + res2
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            res1 = str(cur1.val) + res1
            cur1 = cur1.next
            
        while cur2:
            res2 = str(cur2.val) + res2
            cur2 = cur2.next

        string += str(int(res1) + int(res2))
        dummy = ListNode()
        tail = dummy
        for i in range(len(string)-1,-1,-1):
            tail.next = ListNode(int(string[i]))
            tail = tail.next

        return dummy.next 



        