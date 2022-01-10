class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        a = "0"*(maxLen - len(a)) + a
        b = "0"*(maxLen - len(b)) + b
        carry = 0
        result = ""
        for ch1, ch2 in zip(a[::-1], b[::-1]):
            digit = int(ch1) + int(ch2) + carry
            if digit == 0:
                carry = 0
            elif digit == 1:
                carry = 0
            elif digit == 2:
                carry = 1
                digit = 0
            else:
                digit = 1
                carry = 1
            result = str(digit) + result
        if carry:
            result = str(carry) + result
        return result
        