class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = s.split()
        if len(pattern) != len(tokens):
            return False
        chWordMap = {}
        for ch, word in zip(pattern, tokens):
            if chWordMap.get("ch|" + ch , word) != word:
                return False
            if chWordMap.get("word|" + word, ch) != ch:
                return False
            chWordMap["ch|" + ch] = word
            chWordMap["word|" + word] = ch
        return True
        