class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0

        while maxHeap or q:
            time += 1
            
            if maxHeap:
                popped = 1 + heapq.heappop(maxHeap)
                
                if popped:
                    q.append((popped, time + n))

            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time




