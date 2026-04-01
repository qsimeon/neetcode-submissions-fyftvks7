class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        # N = len(nums)
        # for i, val in enumerate(nums):
        #     conj = target - val
        #     j = None
        #     # try left
        #     if conj in set(nums[:i]):
        #         j = nums.index(conj, 0, i)
        #     # try right
        #     elif conj in set(nums[i+1:]):
        #         j = nums.index(conj, i+1, N)
        #     if j is not None:
        #         break
        #     else:
        #         continue
        # return [i, j]
        