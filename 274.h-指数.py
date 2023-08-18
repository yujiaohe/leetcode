# @before-stub-for-debug-begin
from python3problem274 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 1. 排序
        # # 先对数组排序
        # citations.sort()
        # h = 0 #初始化h为0
        # # 从后往前遍历数组，如果论文引用次数item > 当前h值，说明这片论文满足H指数条件，h+1
        # for item in citations[::-1]:
        #     if item > h:
        #         h += 1
        # return h
        # # 2. 计数排序
        n = len(citations)
        # 计数器数组: 记录引用次数[0,n]的论文数量。 counter[0]: 表示引用次数为0的论文有几篇
        counter = [0]*(n+1)
        for item in citations:
            if item >= n:  # > n次引用的都映射到n
                counter[n] += 1
            else:
                counter[item] += 1

        total = 0 # 记录>=index的论文总数
        for index in range(n, -1, -1):
            total += counter[index]
            if total >= index:
                return index
        return 0
        # 3. 二分法
        # left, right = 0, len(citations)
        # while left < right:
        #     mid = (left + right + 1) >> 1
        #     cnt = 0
        #     for item in citations:
        #         if item >= mid:
        #             cnt += 1
        #     if cnt >= mid:
        #         left = mid
        #     else:
        #         right = mid - 1

        # return left


# @lc code=end
