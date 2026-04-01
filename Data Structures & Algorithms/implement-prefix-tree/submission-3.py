# class TrieNode:
#     def __init__(self):
#         self.children = dict()
#         self.endOfWord = False

# class PrefixTree:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         cur = self.root

#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
        
#         cur.endOfWord = True

#     def search(self, word: str) -> bool:
#         cur = self.root

#         for c in word:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
        
#         return cur.endOfWord

#     def startsWith(self, prefix: str) -> bool:
#         cur = self.root

#         for c in prefix:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         return True
        
class PrefixTree:

    def __init__(self):
        self.tree = set()

    def insert(self, word: str) -> None:
        self.tree.add(word)

    def search(self, word: str) -> bool:
        return word in self.tree

    def startsWith(self, prefix: str) -> bool:
        boolean = False
        for s in self.tree:
            boolean = boolean or s.startswith(prefix)
        return boolean