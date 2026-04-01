class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Easy cases to return False
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        # >>> APPROACH 2 >>>
        # Since the strings must be same length we can sort and iterate once
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        assert len(s) == len(t), "String should be same length at this point."
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s != char_t: 
                return False
        return True
        # <<< APPROACH 2 <<<
        # # >>> APPROACH 1 >>>
        # # Create a map char->count for both strings and compare their equality
        # char2count_s = dict()
        # for char_s in s:
        #     char2count_s[char_s] = char2count_s.get(char_s, 0) + 1
        # char2count_t = dict()
        # for char_t in t:
        #     char2count_t[char_t] = char2count_t.get(char_t, 0) + 1
        # # If the dicts are equal then it is an anagram
        # return char2count_s == char2count_t
        # # <<< APPROACH 1 <<<
        