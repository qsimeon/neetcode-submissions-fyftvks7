class Solution:
    def isValid(self, s: str) -> bool:
        # make a map of open to close braces: '('->')', '{'->'}', '['->']'
        open2close = {
            '(': ')', 
            '{': '}', 
            '[': ']',
            }
        openings = set(open2close.keys())
        closings = set(open2close.values())

        ## never empty string "" since we are told 1<=len(s)<=1000
        # if len(s) == 0:
        #     return True

        # if length is odd, imposible to close
        if len(s) % 2 == 1: 
            return False

        # the first brace must be an opener
        if s[0] in set(open2close.values()): # closings
            return False
        
        # do a trick of wrapping s in () -> (s)
        s = f'({s})'
        stack = [s[0]]
        for i in range(1, len(s)):
            # print(stack)
            lastOpen = stack[-1]
            currBrace = s[i]
            # found the close for this open
            if currBrace == open2close.get(lastOpen, None):
                # pop off the stack
                stack.pop(-1)
            # it must be another open otherwise invalid
            else:
                if currBrace in closings:
                    return False
                stack.append(currBrace)
        # if the stack is empty then the string was valid
        if len(stack) == 0:
            return True
        return False