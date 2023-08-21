# @before-stub-for-debug-begin
from python3problem134 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # # timeout
        # starts = []
        # n = len(gas)
        # for index in range(n):
        #     if gas[index] >= cost[index]:
        #         starts.append(index)

        # for start in starts:
        #     remain = gas[start]
        #     pos = start
        #     while remain - cost[pos] >= 0:
        #         next = (pos+1) % n
        #         remain = remain - cost[pos] + gas[next]
        #         if next == start:
        #             return start
        #         pos = next

        # return -1

        # 如果从x出发，最远到达y (无法到达y+1)
        # 那么，z∈[x,y] (x,y之间的任意一个站点z)也无法到达y+1
        # 因为从x到z时，肯定有存量的油，都无法到达y+1, 直接从z出发，没有存量的油，更不能到达y+1
        # 首先检查第0个加油站，并试图判断能否环绕一周；如果不能，就从第一个无法到达的加油站开始继续检查
        start, n = 0, len(gas)
        while start < n:
            total_gas, total_cost = 0, 0
            step = 0  # 走的站点数量

            # 计算从start开始，能走的最远站点数
            while step < n:
                next = (start + step) % n
                total_gas += gas[next]
                total_cost += cost[next]
                if total_gas < total_cost:
                    break
                step += 1

            if step == n:  # 走的站点数 == 站点总数
                return start
            else:
                start += step + 1

        return -1


# @lc code=end
