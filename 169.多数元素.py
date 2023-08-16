#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1: hash tabel
        # count_dict = {}
        # for item in nums:
        #     count_dict[item] = count_dict.get(item, 0) + 1
        #     if count_dict[item] > len(nums) // 2:
        #         return item

        # 2: Boyer-Moore投票算法: 如果我们把众数记为 +1，把其他数记为 −1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。
        candidate, count = nums[0], 0
        for item in nums:
            if item == candidate:
                count += 1
            elif count == 0:
                candidate, count = item, 1
            else:
                count -= 1
        return candidate


# @lc code=end
