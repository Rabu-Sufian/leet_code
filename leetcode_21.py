class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output = []
        for l1,l2 in zip(list1, list2):
            if l1 == l2:
                output.append(l1)
                output.append(l2)
            if l1 < l2:
                output.append(l1)
                output.append(l2)
            if l2 < l1:
                output.append(l2)
                output.append(l1)   
        return output

list1 = [1,5,8]
list2 = [0]
sol = Solution()
print(sol.mergeTwoLists(list1, list2))