# 169. Majority Element
from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        k = nums[0]
        num = Counter(nums)
        for key, val in num.items():
            if val > max:
                max = val
                k =  key
        return k
           

nums = [2,2,1,1,1,2,2]
sol = Solution()
print(sol.majorityElement(nums)) 