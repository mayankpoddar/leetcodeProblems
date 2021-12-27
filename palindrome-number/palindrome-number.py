class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        n = len(str_x)
        if n % 2:
            to = 1 + n//2
        else:
            to = n//2
        for i in range(to):
            if str_x[i] != str_x[n-1-i]:
                return False
        return True