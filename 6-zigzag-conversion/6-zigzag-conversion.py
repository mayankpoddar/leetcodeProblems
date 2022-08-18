class Solution:
    
    def getJump(self, numRows, i, direction):
        if direction == 0:
            # down
            chars_down = max(numRows - 1 - i, 0)
            chars_diagonal = max(numRows - 2 - i, 0)
            jump = chars_down + chars_diagonal + 1
        else:
            # up
            chars_diagonal = max(i-1, 0)
            chars_up = max(i, 0)
            jump = chars_up + chars_diagonal + 1
        return jump
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        result = ""
        for i in range(numRows):
            direction = 0 # down
            if i == numRows-1:
                direction = 1 # up
            jump = self.getJump(numRows, i, direction)
            ind = i
            while ind < n:
                result += s[ind]
                ind += jump
                if i == 0 or i == numRows - 1:
                    continue
                else:
                    direction = abs(direction - 1)
                    jump = self.getJump(numRows, i, direction)
        return result
        