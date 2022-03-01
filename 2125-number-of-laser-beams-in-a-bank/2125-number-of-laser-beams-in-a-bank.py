class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        currentDevices = sum(map(int, list(bank[0])))
        totalBeams = 0
        for floor in bank[1:]:
            newDevices = sum(map(int, list(floor)))
            if newDevices == 0:
                continue
            totalBeams += currentDevices*newDevices
            currentDevices = newDevices
        return totalBeams
        
        