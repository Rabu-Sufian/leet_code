# 1769. Minimum Number of Operations to Move All Balls to Each Box

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        non_empty_box=[]
        result = []
        
        for index, value in enumerate(boxes):
            if value == '1':
                non_empty_box.append(index)
        
        for i in range(len(boxes)):
            counter = 0
            for j in non_empty_box:
                counter += abs(i-j)
            result.append(counter)
        
        return result
                


boxes = '001011'
sol = Solution()
print(sol.minOperations(boxes))