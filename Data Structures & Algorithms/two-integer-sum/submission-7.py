class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i, val in enumerate(nums):
            conj = target - val
            j = None
            # try left
            if conj in set(nums[:i]):
                j = nums.index(conj, 0, i)
            # try right
            elif conj in set(nums[i+1:]):
                j = nums.index(conj, i+1, N)
            if j is not None:
                break
            else:
                continue
        return [i, j]
        # # Iterate through the list. For each value look for target-value in rest of list.
        # inds_vals_sorted = sorted(enumerate(nums), key=lambda x: x[1])
        # print(inds_vals_sorted) # DEBUG 
        # sorted_inds = map(lambda x: x[0], inds_vals_sorted)
        # sorted_vals = map(lambda x: x[1], inds_vals_sorted)
        # print(list(sorted_inds)) # DEBUG 
        # print(list(sorted_vals)) # DEBUG 
        # for i, val_i in enumerate(sorted_vals):
        #     conj = target - val_i
        #     if conj <= val_i: # look in the left half
        #         left = sorted_vals[:i]
        #         for j, val_j in left:
        #             if
        #     else: # look in the right half
        #         right = sorted_vals[i+1:]
        # return None
        
        