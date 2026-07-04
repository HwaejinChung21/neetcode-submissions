class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value, timestamp])

        else:
            self.timeMap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        l = 0
        r = len(self.timeMap[key]) - 1
        res = ""

        tArray = self.timeMap[key]
        # {alice: [[happy, 1], [sad, 3]]}

        while l <= r:
            m = (l + r) // 2
            
            if tArray[m][1] <= timestamp:
                res = tArray[m][0]
                l = m + 1

            else: 
                r = m - 1
        
        return res



