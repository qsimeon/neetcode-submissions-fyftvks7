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
            
           
        