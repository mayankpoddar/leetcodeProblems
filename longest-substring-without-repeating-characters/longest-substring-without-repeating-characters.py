class Solution:
    
    def arraySubtract(self, arr1, arr2):
        return [arr1[i] - arr2[i] for i in range(26)]
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        maxLen = 1
        i = 0
        while i < n-1:
            chSet = {}
            chSet[s[i]] = 1
            currentLen = 1
            j = i+1
            while j < n:
                if not chSet.get(s[j], None):
                    currentLen += 1
                    chSet[s[j]] = 1
                    maxLen = max(maxLen, currentLen)
                else:
                    j = n
                j += 1
            i += 1
        return maxLen
        