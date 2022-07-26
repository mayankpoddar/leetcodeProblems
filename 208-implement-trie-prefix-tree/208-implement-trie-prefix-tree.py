class Node:
    def __init__(self):
        self.children = [None]*26 # Since only lowercase english
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if current.children[index] == None:
                current.children[index] = Node()
            current = current.children[index]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if current.children[index] == None:
                return False
            current = current.children[index]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if current.children[index] == None:
                return False
            current = current.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)