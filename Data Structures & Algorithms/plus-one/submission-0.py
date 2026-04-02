class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(map(str, digits)))
        # print(integer)
        plusOne = integer + 1
        # print(plusOne)
        asListStr = list(str(plusOne))
        # print(asListStr)
        asListInt = list(map(int, asListStr))
        # print(asListInt)
        return asListInt
        