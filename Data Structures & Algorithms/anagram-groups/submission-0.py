class WordHash:
        def __init__(self, word: str):
            self.word = word
            self.hmap = self.hash_map(word)
        
        def hash_map(self, word):
            char2count = dict()
            for char in word:
                char2count[char] = char2count.get(char, 0) + 1
            return char2count

        def __eq__(self, other):
            return self.hmap == other.hmap
        
        def __repr__(self):
            return str(self.hmap)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagrams are strings that are the same if you sort the characters
        # The sorted string is therefore a unique representation or key
        sorted_strs = sorted(strs)
        anagramDict = dict() # map keys to anagrams
        for word in sorted_strs:
            key = tuple(sorted(word))
            anagramDict.setdefault(key, [])
            anagramDict[key].append(word)
        # Return the list of anagrams
        anagrams = []
        for k, v in anagramDict.items():
            anagrams.append(v)
        return anagrams
            
           
        