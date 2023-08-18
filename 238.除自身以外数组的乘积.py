# @before-stub-for-debug-begin
from python3problem238 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 用left，right数组存在index左边和右边的乘积
        # answer = []
        # n = len(nums)
        # left, right = [1]*n, [1]*n
        # for index in range(1, n):
        #     left[index] = left[index-1]*nums[index-1]
        # for index in range(n-2, -1, -1):
        #     right[index] = right[index+1]*nums[index+1]
        # for index in range(n):
        #     answer.append(left[index]*right[index])
        # return answer

        # 节省存储空间，将left存在answer中
        n = len(nums)
        answer = [1] * n
        for index in range(1, n):
            answer[index] = answer[index-1]*nums[index-1]
        
        right = 1
        for index in range(n-2, -1, -1):
            answer[index] *= right*nums[index+1]
            right *= nums[index+1]
        return answer
        

# @lc code=end

