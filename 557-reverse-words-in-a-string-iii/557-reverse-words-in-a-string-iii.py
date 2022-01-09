class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        current_word = ""
        for ch in s:
            if ch == " ":
                result += current_word[::-1]
                result += " "
                current_word = ""
            else:
                current_word += ch
        if len(current_word):
            result += current_word[::-1]
        return result