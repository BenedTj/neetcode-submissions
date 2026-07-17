# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res, tmp = [], pairs

        for l in range(0, len(pairs)):
            for prev in range(l - 1, -1, -1):
                if tmp[prev + 1].key < tmp[prev].key:
                    tmp[prev + 1], tmp[prev] = tmp[prev], tmp[prev + 1]
                else:
                    break

            res.append(tmp[:])    

        return res