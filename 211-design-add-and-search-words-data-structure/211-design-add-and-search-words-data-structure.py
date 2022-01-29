class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.endOfWord = True        

    def search(self, word: str) -> bool:
        current = self.root
        return self.searchFromNode(word, current)
    
    def searchFromNode(self, word, node):
        n = len(word)
        if n == 0:
            return node.endOfWord
        char = word[0]
        if char == ".":
            currentChars = [child for child in node.children if child]
            if len(currentChars) == 0:
                return False
            else:
                flag = any([self.searchFromNode(word[1:], possible) for possible in currentChars])
                return flag
        else:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            else:
                return self.searchFromNode(word[1:], node.children[index])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)