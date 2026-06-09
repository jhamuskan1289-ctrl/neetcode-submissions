class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        l1 = r1= 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                l1= max(l1, height[l])
                water += l1 - height[l]
                l += 1
            else:
                r1 = max(r1, height[r])
                water += r1 - height[r]
                r -= 1

        return water