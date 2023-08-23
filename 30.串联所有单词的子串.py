# @before-stub-for-debug-begin
from python3problem30 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # from collections import Counter
        # one_word = len(words[0])
        # all_len = one_word * len(words)
        # n = len(str)
        # words = Counter(words) #统计需要匹配的单词和其频率 得到words哈希表
        # result = []

        # for i in range(0, n - all_len + 1):
        #     # 截取words总长度相同的字符串
        #     tmp = s[i:i+all_len]
        #     c_tmp = []
        #     # 计算tmp字符串中可能存在的长度为单个word的单词集合
        #     for j in range(0, all_len, one_word):
        #         c_tmp.append(tmp[j:j+one_word])
        #     if words == Counter(c_tmp):
        #         result.append(i)

        # return result

        # 优化：利用sliding window
        from collections import Counter
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)

        words = Counter(words)  # 统计需要匹配的单词和其频率, 得到words哈希表
        result = []

        for i in range(0, one_word):
            cur_cnt = 0  # 滑动窗口word数量
            left, right = i, i  # 滑动窗口左右边界
            cur_counter = Counter()  # 滑动窗口的哈希表，单词和频次

            while right + one_word <= n:
                w = s[right:right+one_word]  # 从s中截取一个单词
                right += one_word           # 移动滑动窗口右边界到下一个单词的位置
                if w not in words:          # 截取单词不在words中
                    left = right            # 移动滑动窗口左边界
                    cur_counter.clear()     # 滑动窗口哈希表清零
                else:
                    cur_counter[w] += 1     # 截取单词在滑动窗口哈希表中，更新频次
                    while cur_counter[w] > words[w]:  # 更新之后，如果滑动窗口中该单词频次 > words中的频次
                        left_w = s[left:left+one_word]  # 从左边界开始提取单词
                        cur_counter[left_w] -= 1  # 更新滑动窗口左边界单词的频次
                        left += one_word    # 向右移动左边界
                    if (right-left)/one_word == word_num:  # 滑动窗口单词总数=words单词总数
                        result.append(left)
        return result


# @lc code=end
