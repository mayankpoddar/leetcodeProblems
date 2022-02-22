class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, ch in enumerate(columnTitle[::-1]):
            key = ord(ch) - ord('A') + 1
            result += (26**i)*key
        return result