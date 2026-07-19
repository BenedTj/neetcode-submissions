# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curhead, cur = None, None
        cur1, cur2 = list1, list2

        def assign(node: ListNode) -> None:
            nonlocal curhead
            nonlocal cur

            if curhead is None:
                curhead = node
            
            if cur is None:
                cur = node
            else:
                cur.next = node
                cur = node

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                assign(cur1)
                cur1 = cur1.next
            else:
                assign(cur2)
                cur2 = cur2.next
        
        while cur1:
            assign(cur1)
            cur1 = cur1.next
        
        while cur2:
            assign(cur2)
            cur2 = cur2.next
        
        return curhead