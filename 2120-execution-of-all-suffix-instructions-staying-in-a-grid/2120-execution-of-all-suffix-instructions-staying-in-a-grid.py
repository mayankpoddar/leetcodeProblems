class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        results = [0]*m
        for i in range(m):
            currentPos = startPos[:]
            steps = 0
            for j in range(i, m):
                steps += 1
                if s[j] == "L" and currentPos[1] > 0:
                    currentPos[1] -= 1
                elif s[j] == "R" and currentPos[1] < n-1:
                    currentPos[1] += 1
                elif s[j] == "U" and currentPos[0] > 0:
                    currentPos[0] -= 1
                elif s[j] == "D" and currentPos[0] < n-1:
                    currentPos[0] += 1
                else:
                    steps -= 1
                    break
            results[i] = steps
        return results
        