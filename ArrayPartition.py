class Solution:
    def arrayPairSum(nums) -> int:
        nums.sort()
        count = 0
        pairs = [(nums[i], nums[i+1]) for i in range(0, len(nums) - 1, 2)]
        for i in pairs:
            count = count + min(i)
        return count
        
        
    arrayPairSum([6,2,6,5,1,2])