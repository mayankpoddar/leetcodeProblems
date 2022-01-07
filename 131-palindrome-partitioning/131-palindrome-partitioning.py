class Solution:
    
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        results = []
        if n == 0:
            return results
        elif n == 1:
            results.append([s[0]])
            return results
        else:
            currentString = ""
            for i in range(n):
                currentString += s[i]
                if self.isPalindrome(currentString):
                    for result in self.partition(s[i+1:]):
                        results.append([currentString] + result)
            if self.isPalindrome(s):
                results.append([s])
        return results
        