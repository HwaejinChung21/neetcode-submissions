import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        res = []

        for x, y in points:
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            distances[(x, y)] = distance

        heap = []

        for point, distance in distances.items():
            heapq.heappush(heap, (distance, point))

        for _ in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])

        return res
