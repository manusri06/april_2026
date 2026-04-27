class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return [dict[diff],i]
            dict[n]=i
        