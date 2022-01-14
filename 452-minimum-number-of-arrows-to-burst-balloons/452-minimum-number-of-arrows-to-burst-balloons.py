class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: [x[0],x[1]])
        merged_intervals = []
        current_start = points[0][0]
        current_end = points[0][1]
        for point in points[1:]:
            if point[0] <= current_end:
                current_start = point[0]
                current_end = min(current_end, point[1])
            else:
                merged_intervals.append([current_start, current_end])
                current_start = point[0]
                current_end = point[1]
        merged_intervals.append([current_start, current_end])
        return len(merged_intervals)
        
        