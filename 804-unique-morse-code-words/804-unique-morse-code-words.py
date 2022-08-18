class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result_set = set()
        for word in words:
            morse = ""
            for ch in word:
                morse += codes[ord(ch)-ord('a')]
            result_set.add(morse)
        return len(result_set)