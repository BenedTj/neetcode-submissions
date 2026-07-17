# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        for l in range(0, len(pairs)):
            for prev in range(l - 1, -1, -1):
                if pairs[prev + 1].key < pairs[prev].key:
                    pairs[prev + 1], pairs[prev] = pairs[prev], pairs[prev + 1]
                else:
                    break

            res.append(pairs[:])    

        return res