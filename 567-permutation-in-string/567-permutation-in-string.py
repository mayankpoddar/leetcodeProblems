class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        chCount_s1 = [0 for i in range(26)]
        for ch in s1:
            chCount_s1[ord(ch) - ord('a')] += 1
        chCount_s2 = [0 for i in range(26)]
        for ch in s2[:n1]:
            chCount_s2[ord(ch) - ord('a')] += 1
        if chCount_s1 == chCount_s2:
                return True
        indexToSubtract = 0
        for ch in s2[n1:]:
            chOld = s2[indexToSubtract]
            chCount_s2[ord(chOld) - ord('a')] -= 1
            chCount_s2[ord(ch) - ord('a')] += 1
            if chCount_s1 == chCount_s2:
                return True
            indexToSubtract += 1
        return False
        