class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        totalUnits = 0
        for i in range(len(boxTypes)):
            boxesLoaded = min(boxTypes[i][0], truckSize)
            totalUnits += boxesLoaded*boxTypes[i][1]
            truckSize -= boxesLoaded
            if truckSize == 0:
                break
        return totalUnits
        