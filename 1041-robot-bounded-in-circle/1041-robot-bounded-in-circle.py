class Solution:
    
    def traverse(self, start, direction, instructions):
        current = start[:]
        for inst in instructions:
            if inst == "G":
                if direction == 1:
                    current[1] += 1
                elif direction == -1:
                    current[1] -= 1
                elif direction == 2:
                    current[0] -= 1
                else:
                    current[0] += 1
            elif inst == "L":
                if direction == 1:
                    direction = 2
                elif direction == -1:
                    direction = -2
                elif direction == 2:
                    direction = -1
                else:
                    direction = 1
            else:
                if direction == 1:
                    direction = -2
                elif direction == -1:
                    direction = 2
                elif direction == 2:
                    direction = 1
                else:
                    direction = -1
        return current, direction
    
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0, 0]
        current = [0, 0]
        initial_direction = 1
        direction = 1
        count = 0
        while count < 4:
            current, direction = self.traverse(current, direction, instructions)
            if current == start and direction == initial_direction:
                return True
            count += 1
        return False