# @before-stub-for-debug-begin
from python3problem122 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # n = len(prices)
        # if n < 2:
        #     return 0

        # profit = [[], []]
        # profit[0].append(0)
        # profit[1].append(-prices[0])
        # for index in range(1, n):
        #     profit[0].append(max(profit[0][index-1], profit[1][index-1]+prices[index]))
        #     profit[1].append(max(profit[1][index-1], profit[0][index-1]-prices[index]))

        # return profit[0][n-1]

        # 优化存储空间
        profit0, profit1 = 0, -prices[0]
        for price in prices[1:]:
            profit0, profit1 = max(
                profit0, profit1+price), max(profit1, profit0-price)

        return profit0


# @lc code=end
