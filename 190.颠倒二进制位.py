# @before-stub-for-debug-begin
from python3problem190 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start


class Solution:
    def __init__(self):
        self._m1 = 0x55555555  # 0x01010101010101010101010101010101
        self._m2 = 0x33333333  # 0x00110011001100110011001100110011
        self._m3 = 0x0f0f0f0f  # 0x00001111000011110000111100001111
        self._m4 = 0x00ff00ff  # 0x00000000111111110000000011111111
        self._m5 = 0x0000ffff  # 0x00000000000000001111111111111111

    def reverseBits(self, n: int) -> int:
        # 1: int -> str -> int
        # 转换为32位,不足左侧补0,并用二进制(b)表示
        # n_str = '{:032b}'.format(n)
        # return int(n_str[::-1], base=2)

        # 2: 分治
        # 第一轮: 交换奇数位和偶数位的bit
        # n >> 1 & self._m1: n右移一位之后, 与self._m1与运算, 取出原来n的偶数位bit, 放到现在n的奇数位
        # 同理,(n & self._m1) << 1: n直接与self._m1与运算, 取出原来n奇数位bit, 放到现在n的偶数位
        # 将上述结果或运算, 合并起来实现奇数偶数位交换
        # 后续同理, 每2/4/8/16位一组
        n = n >> 1 & self._m1 | (n & self._m1) << 1
        n = n >> 2 & self._m2 | (n & self._m2) << 2
        n = n >> 4 & self._m3 | (n & self._m3) << 4
        n = n >> 8 & self._m4 | (n & self._m4) << 8
        n = n >> 16 | (n & self._m5) << 16
        return n


# @lc code=end
