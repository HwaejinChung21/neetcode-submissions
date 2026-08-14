import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            heap.append([distance, x, y])
        
        heapq.heapify(heap)
        
        for _ in range(k):
            distance, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res