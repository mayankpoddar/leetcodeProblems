class Solution:
    
    def divider(self, s, startIndex, parts):
        cases = []
        if parts == 1:
            currString = s[startIndex:].strip()
            if not currString:
                return []
            if currString.startswith("0") and len(currString) != 1:
                return []
            if int(currString) > 255:
                return []
            return [currString]
        currString = ""
        for i in range(startIndex, min(len(s), startIndex+3)):
            currString += s[i]
            if currString == "0":
                further = self.divider(s, i+1, parts-1)
                for possible in further:
                    if len(possible.split(".")) == parts-1:
                        cases.append("0." + possible)
                break
            elif int(currString) <= 255:
                further = self.divider(s, i+1, parts-1)
                for possible in further:
                    if len(possible.split(".")) == parts-1:
                        cases.append(currString + "." + possible)
            else:
                break
        return cases
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.divider(s, 0, 4)
        