class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S = set(range(0, len(nums)+1)) - set(nums)
        return S.pop()
        