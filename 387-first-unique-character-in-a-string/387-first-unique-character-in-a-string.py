class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices = [-1]*26
        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            if indices[index] == -1:
                indices[index] = i
            else:
                indices[index] = -5
        indicesList = [element for element in indices if element not in [-1, -5]]
        if len(indicesList) == 0:
            return -1
        else:
            return min(indicesList)
        