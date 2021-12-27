class Solution:
    def findComplement(self, num: int) -> int:
        complementNum = 0
        n = len(str(num))
        i = 0
        while num > 0:
            digit = num % 2
            reverse_digit = 0 if digit else 1
            complementNum += reverse_digit*(2**i)
            num = num // 2
            i += 1
        return complementNum