#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 2次遍历
        # 先从左往右
        # 再从右往左
        n = len(ratings)
        left = [0] * n
        # 如果left[i] > left[i-1], left[i]=left[i-1]+1, else 1
        for index in range(0, n):
            if index > 0 and ratings[index] > ratings[index-1]:
                left[index] = left[index-1] + 1
            else:
                left[index] = 1

        # 从右便利，直接用常量存储，直接计算并和left相加得到result
        right, result = 0, 0
        for index in range(n-1, -1, -1):
            if index < n-1 and ratings[index] > ratings[index+1]:
                right += 1
            else:
                right = 1
            result += max(left[index], right)

        return result


# @lc code=end
