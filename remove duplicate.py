class Solution(object):
   def removeDuplicates(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      if len(nums) == 0:
         return 0
      length = 1
      previous = nums[0]
      index = 1
      for i in range(1,len(nums)):
         if nums[i] != previous:
            length += 1
            previous = nums[i]
            nums[index] = nums[i]
            index+=1
      return length
