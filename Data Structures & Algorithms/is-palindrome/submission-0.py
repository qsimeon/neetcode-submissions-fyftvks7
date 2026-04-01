class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make case insensitve
        s = s.lower()
        # Make alphanumeric only
        mystr = ''
        for _ in s:
            if _.isalnum():
                mystr += _
        return mystr == mystr[::-1]
        