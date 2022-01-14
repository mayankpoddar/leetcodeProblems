class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        lowerbound = -2**31
        upperbound = 2**31 - 1
        digits = []
        sign = 0
        i = 0
        # Remove Leading Whitespaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        # Capture Sign
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = 1
            i += 1
        # Remove Leading Zeroes
        while i < n and s[i] == '0':
            i += 1
        if i == n:
            return 0
        # Capture digits
        while i < n and s[i] >= '0' and s[i] <= '9':
            digits.append(int(s[i]))
            i += 1
        result = 0
        n = len(digits)
        if n >= 32:
            # clamp the result
            if sign:
                return lowerbound
            else:
                return upperbound
        for i in range(n):
            result += digits[i]*(10**(n-i-1))
        if sign:
            result *= -1
        if result <= lowerbound:
            return lowerbound
        elif result >= upperbound:
            return upperbound
        else:
            return result
        