# 26. Remove Duplicates from Sorted Array


class Solution(object):
    def removeDuplicates(self, nums):
        p1 = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[p1]:
                p1 += 1
                nums[p1] = nums[i]
        return p1 +1, nums
                
        
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))