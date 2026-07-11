class Solution:
    def alphaDictKey(self, d: Dict[str, int]) -> str:
        res = ""

        keys = sorted(d.keys())

        for key in keys:
            res += key + str(d[key])

        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict({})

        for st in strs:
            curdict = dict({})

            for s in st:
                if s in curdict:
                    curdict[s] += 1
                else:
                    curdict[s] = 1

            key = self.alphaDictKey(curdict)

            if key in groups:
                groups[key].append(st)
            else:
                groups[key] = [st]

        res = []

        for key, val in groups.items():
            res += [val]

        return res