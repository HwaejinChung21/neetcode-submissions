class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        freq = {}
        res = []

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        print(freq)

        for key, val in freq.items():
            count[val].append(key)

        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                if count[i] != []:
                    res.append(n)

                    if len(res) == k:
                        return res

