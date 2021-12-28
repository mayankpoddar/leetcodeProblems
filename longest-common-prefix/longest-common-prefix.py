class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = min([len(s) for s in strs])
        commonPrefix = ""
        for i in range(minLength):
            flag = True
            ch_i = set([s[i] for s in strs])
            if len(ch_i) == 1:
                commonPrefix += ch_i.pop()
            else:
                break
        return commonPrefix
                