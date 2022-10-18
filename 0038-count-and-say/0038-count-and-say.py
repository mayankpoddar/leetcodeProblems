class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n-1))
        
    def say(self, string):
        elements = [[string[0], 1]]
        for ch in string[1:]:
            if ch == elements[-1][0]:
                elements[-1][1] += 1
            else:
                elements.append([ch, 1])
        result = "".join([str(count) + ch for ch, count in elements])
        return result
            
        