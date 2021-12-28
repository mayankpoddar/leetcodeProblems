class Solution:
    def reverse(self, x: int) -> int:
        n = len(str(x))
        minValue = -2**31
        maxValue = 2**31 - 1
        num = 0
        negative = 0
        if x < 0:
            negative = 1
            x *= -1
            n -= 1
        exp = 0
        while x >= 1:
            digit = x % 10
            if negative:
                num -= digit * (10**(n - 1 - exp))
            else:
                num += digit * (10**(n - 1 - exp))
            exp += 1
            x = x//10
            if num > maxValue or num < minValue:
                return 0
        return num
        