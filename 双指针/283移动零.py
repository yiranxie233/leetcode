"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]


示例 2:
输入: nums = [0]
输出: [0]
"""
from typing import List

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         stack_size = 0
#         for num in nums:
#             if num != 0:
#                 nums[stack_size] = num
#                 stack_size += 1
            

#         for i in range(stack_size, len(nums)):
#             nums[i] = 0

#         return nums

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1
        return nums


s = Solution()
print(s.moveZeroes([0,1,0,3,12]))