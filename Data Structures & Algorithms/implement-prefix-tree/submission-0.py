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
        