class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minFrom = 1000
        maxTo = 0
        for trip in trips:
            minFrom = min(minFrom, trip[1])
            maxTo = max(maxTo, trip[2])
        path = [0]*(maxTo-minFrom+1)
        n = len(path)
        for trip in trips:
            path[trip[1]-minFrom] += trip[0]
            path[trip[2]-minFrom] -= trip[0]
        currentSum = 0
        for passengers in path:
            currentSum += passengers
            if currentSum > capacity:
                return False
        return True