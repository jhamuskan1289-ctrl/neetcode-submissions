class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       a = []
       for i , num in enumerate(nums):
        a.append([num,i])

       a.sort()

       l , r = 0 , len(nums)-1
       while l<r:
           cur = a[l][0] + a[r][0]

           if cur == target :
            return[min(a[l][1],a[r][1]), 
            max(a[l][1],a[r][1])]

           elif cur < target :
             l+=1
           else:
            r-=1

       return []
