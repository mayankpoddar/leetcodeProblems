class Solution:
    
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = n
        for i in range(n-1):
            for j in range(i+1, n):
                if self.isPalindrome(s[i:j+1]):
                    result += 1
        return result
        