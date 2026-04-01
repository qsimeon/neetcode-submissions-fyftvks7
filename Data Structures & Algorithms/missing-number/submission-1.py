class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S = set(range(0, len(nums)+1)) - set(nums)
        print(S)
        return S.pop()
        