class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        result = 0
        lefts = 0
        rights = 0
        for i in range(n):
            if s[i] == "(":
                lefts += 1
            else:
                rights += 1
            if lefts == rights:
                result = max(result, lefts + rights)
            elif rights > lefts:
                lefts = 0
                rights = 0
        lefts = 0
        rights = 0
        for i in range(n-1, -1, -1):
            if s[i] == "(":
                lefts += 1
            else:
                rights += 1
            if lefts == rights:
                result = max(result, lefts + rights)
            elif lefts > rights:
                lefts = 0
                rights = 0
        return result
                
        