class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_table = {}
        for i in range(len(nums)):
            if target - nums[i] in dict_table:
                return [dict_table[target - nums[i]], i]
            dict_table[nums[i]] = i