#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心算法：每次在上次能跳到的范围(end)内选择一个能跳的最远的位置（cur_max）作为下次起跳点
        # cur_max: 当前能跳的最远位置
        # count: 跳跃次数
        # end: 跳跃可达范围的右边界
        cur_max, count, end = 0, 0, 0
        for index, value in enumerate(nums[:-1]):
            if cur_max >= index:
                cur_max = max(cur_max, index+value)
                if index == end:
                    end = cur_max
                    count += 1
        return count


# @lc code=end

