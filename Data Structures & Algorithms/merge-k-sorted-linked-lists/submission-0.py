# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res, reshead = None, None
        considered, idxs = lists.copy(), list(range(len(lists)))

        while idxs:
            minval, idx = math.inf, -1

            for index in idxs:
                l = considered[index]
                if l.val < minval:
                    minval = l.val
                    idx = index

            if res is None:
                res, reshead = considered[idx], considered[idx]
            else:
                res.next = considered[idx]
                res = res.next
            considered[idx] = considered[idx].next
            
            if considered[idx] is None:
                idxs.remove(idx)
        
        return reshead