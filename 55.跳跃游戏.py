#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心算法：尽可能达到最远位置
        # 如果能达到某个位置，那一定能达到它前面的所有位置
        max_dist = 0
        for index, jump in enumerate(nums):  # index为当前位置，jump为当前位置的最大跳数
            # 如果当前位置能达到，且当前位置+跳数>max_dist
            if max_dist >= index:
                max_dist = max(max_dist, index + jump)

        # 最后比较最远距离是否大于数字长度
        return max_dist >= index
# @lc code=end
