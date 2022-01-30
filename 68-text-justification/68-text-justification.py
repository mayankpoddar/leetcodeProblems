class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        results = []
        currentArray = []
        currentLength = -1
        for word in words:
            l = currentLength + 1 + len(word)
            if l <= maxWidth:
                currentArray.append(word)
                currentLength = l
            else:
                spacesToFill = maxWidth - currentLength
                n = len(currentArray)
                if n == 1:
                    text = currentArray[0]
                    text += " "*(maxWidth - len(text))
                else:
                    text = ""
                    extraSpaces = spacesToFill // (n-1)
                    remainder = spacesToFill % (n-1)
                    for x in currentArray:
                        text += x + " " + " "*(extraSpaces) 
                        if remainder:
                            text += " "
                            remainder -= 1
                    text = text.strip()
                results.append(text)
                currentArray = [word]
                currentLength = len(word)
        text = " ".join(currentArray)
        text += " "*(maxWidth - len(text))
        results.append(text)
        return results
        