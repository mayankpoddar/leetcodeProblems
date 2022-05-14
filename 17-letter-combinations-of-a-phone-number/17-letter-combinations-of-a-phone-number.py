class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        key_map = {}
        ord_ch = ord('a')
        for key in range(2, 10):
            num_letters = range(4) if key in [7, 9] else range(3)
            key_map[str(key)] = [chr(ord_ch + i) for i in num_letters]
            ord_ch += len(num_letters)
        possibleDigitLetters = key_map[digits[-1]]
        for digit_ind in range(n-2, -1, -1):
            currentPossibleLetters = key_map[digits[digit_ind]]
            new_strings = set()
            for l in currentPossibleLetters:
                for suffix in possibleDigitLetters:
                    new_strings.add(l + suffix)
            possibleDigitLetters = list(new_strings)
        return possibleDigitLetters
            
        
        