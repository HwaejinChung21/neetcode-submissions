class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        res = []

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            freqMap[tuple(count)].append(s)

        for v in freqMap.values():
            res.append(v)

        return res