class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        count = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        for key, val in freqMap.items():
            count[val].append(key)

        for i in range(len(count) - 1, 0, -1):     
            if count[i] != []:
                for n in count[i]:
                    res.append(n)

                    if len(res) == k:
                        return res

        return res

        
