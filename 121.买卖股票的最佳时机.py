# @before-stub-for-debug-begin
from python3problem121 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # 0～i天的最低价格：min_price[i] = min(min_price[i-1], prices[i])
        # min_price = [prices[0]]
        # max_price = 0
        # for price in prices[1:]:
        #     max_price = max(max_price, price - min_price[-1])
        #     min_price.append(min(min_price[-1], price))
        # return max_price
    
        # 用单个变量存储min_price, 节省存储空间
        min_price = prices[0]
        max_price = 0
        for price in prices[1:]:
            max_price = max(max_price, price - min_price)
            min_price = min(min_price, price)
        return max_price

# @lc code=end

