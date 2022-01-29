class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        firstLetter = word[0]
        firstFlag = False
        numCaps = 0
        if firstLetter >= 'A' and firstLetter <= 'Z':
            firstFlag = True
            numCaps += 1
        for char in word[1:]:
            if char >= 'A' and char <= 'Z':
                numCaps += 1
        if numCaps == 0 or numCaps == n:
            return True
        if numCaps == 1 and firstFlag:
            return True
        return False