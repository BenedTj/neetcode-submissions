import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amounts = dict({})
        maxheap = []

        for num in nums:
            if num in amounts:
                amounts[num] += 1
            else:
                amounts[num] = 1
        
        for key, val in amounts.items():
            maxheap.append((-val, key))
        
        heapq.heapify(maxheap)

        return [val for _, val in heapq.nsmallest(k, maxheap)]