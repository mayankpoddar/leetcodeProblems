class Solution:
    
    def getNum(self, firstDigit, numDigits):
        resStr = str(firstDigit)
        for i in range(numDigits-1):
            digit = str(firstDigit + i + 1)
            if len(digit) == 1:
                resStr += digit
            else:
                break
        return int(resStr)
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lowStr = str(low)
        highStr = str(high)
        n1 = len(lowStr)
        n2 = len(highStr)
        results = []
        for numDigits in range(n1, n2+1):
            for firstDigit in range(1, 10-numDigits+1):
                num = self.getNum(firstDigit, numDigits)
                if num < low:
                    continue
                elif num >= low and num <= high:
                    results.append(num)
                else:
                    break
        return results
                
        