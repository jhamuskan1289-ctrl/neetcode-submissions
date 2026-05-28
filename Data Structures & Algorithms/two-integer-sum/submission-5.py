class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = []
        for i in range(len(nums)):
            x.append([nums[i], i])

        x = sorted(x)

        left = 0
        right = len(nums) - 1
        while left <= right:
            sum = x[left][0] + x[right][0]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                p = x[left][1]
                q = x[right][1]
                return [min(p, q), max(p, q)]

