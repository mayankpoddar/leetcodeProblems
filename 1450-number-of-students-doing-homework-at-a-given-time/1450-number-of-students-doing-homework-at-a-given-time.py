class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        times = [0]*1001
        for st, et in zip(startTime, endTime):
            times[st-1] += 1
            times[et] -= 1
        for i in range(1, 1001):
            times[i] = times[i] + times[i-1]
        return times[queryTime-1]
        