from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = head
        st = deque([])
        cur = head.next
        flag = True

        while cur:
            st.append(cur)
            cur = cur.next

        while st:
            if flag:
                newnode = st.pop()
            else:
                newnode = st.popleft()
            
            print(newnode.val)

            res.next = newnode
            res = newnode
            flag = not flag
        
        res.next = None