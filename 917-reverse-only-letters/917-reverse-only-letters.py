class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def checkChar(ch):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
                return True
            return False
        n = len(s)
        resultChars = []
        for i in range(n):
            if checkChar(s[i]):
                resultChars.append(s[i])
        result = ""
        for i, ch in enumerate(s):
            if checkChar(s[i]):
                result += resultChars.pop()
            else:
                result += ch
        return result
        