# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        st = []
        cur = head

        while cur:
            st.append(cur)
            cur = cur.next

        leng = len(st)
        
        if n == leng:
            if leng >= 2:
                return st[1]
            else:
                return None
        else:
            if n == 1:
                st[leng - n - 1].next = None
            else:
                st[leng - n - 1].next = st[leng - n + 1]
            return head