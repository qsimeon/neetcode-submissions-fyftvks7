class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Easy cases to return False
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        # Create a map char->count for both strings and compare their equality
        char2count_s = dict()
        for char_s in s:
            char2count_s[char_s] = char2count_s.get(char_s, 0) + 1
        char2count_t = dict()
        for char_t in t:
            char2count_t[char_t] = char2count_t.get(char_t, 0) + 1
        # If the dicts are equal then it is an anagram
        return char2count_s == char2count_t
        