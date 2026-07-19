# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def toInt(node: Optional[ListNode]) -> int:
            cur = node
            num = ""
            leng = 0

            while cur:
                num += str(cur.val)
                cur = cur.next
                leng += 1

            num = num[::-1]
            return int(num)
        
        def toNode(num: int) -> Optional[ListNode]:
            curhead = ListNode(num % 10)
            num = num // 10

            cur = curhead
            while num != 0:
                cur.next = ListNode(num % 10)
                cur = cur.next
                num = num // 10
            
            return curhead

        total = toInt(l1) + toInt(l2)
        return toNode(total)