#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # min_str = min(strs, key=len)
        # result = ""
        # for index, char in enumerate(min_str):
        #     for str in strs:
        #         if char != str[index]:
        #             break
        #     result += char
        # return result
        conv_strs = list(zip(*strs))
        result = ""
        for char in conv_strs:
            if len(set(char)) == 1:
                result += char[0]
            else:
                break
        return result

# @lc code=end
