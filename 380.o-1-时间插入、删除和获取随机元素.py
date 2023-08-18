# @before-stub-for-debug-begin
from python3problem380 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
import random


class RandomizedSet:

    def __init__(self):
        # 变长数组 + 哈希表
        self.nums = []  # 变长数组
        self.hash_index = {}  # val: 数组index

    def insert(self, val: int) -> bool:
        if val in self.hash_index:
            return False
        else:
            self.hash_index[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:

        if val in self.hash_index:
            val_ind = self.hash_index[val]  # 找到删除val对应的index
            n = len(self.nums) - 1
            self.nums[val_ind] = self.nums[n]  # 用数组last element覆盖
            self.hash_index[self.nums[n]] = val_ind  # 更新last在hash table中的index
            # 如果数组只有一个数[1]，调用remove删除1，则要先用1覆盖1，再pop；否则数组为空，用last element覆盖报错
            self.nums.pop(-1)  # 删除数组最后一个元素
            self.hash_index.pop(val)  # delete val in hash table
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
