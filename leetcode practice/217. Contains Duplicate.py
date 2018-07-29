"""

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Subscribe to see which companies asked this question.

"""
"""利用hash table，别忘了判断空数组的情况.其实更麻烦"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        dic = dict()
        for num in nums:
            if num in dic:
                return True
            dic[num] = 1
        return False

"""直接利用set的性质反而更简单"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

"""利用列表自带的方法"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in nums:
            if nums.count(i) >= 2:
                return True
        return False