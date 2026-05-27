# [1,2,4,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
#[1,1,1,1]
    
        pref = 1
        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res   
# [1,1,2,8]
# [48,24,12,8]
