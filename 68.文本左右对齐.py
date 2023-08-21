# @before-stub-for-debug-begin
from python3problem68 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i, result = 0, []
        while i < len(words):
            line = ''  # 每行生成的字符串
            j = i + 1  # 从i开始往后便利
            len_sum = len(words[i])  # 统计每行字符串的总长度
            # word之间至少1个空格，所以计算len_sum时+1
            while j < len(words) and len_sum + 1 + len(words[j]) <= maxWidth:
                len_sum += 1 + len(words[j])
                j += 1
            numWords = j - i
            # 减去上述计算过程中每个word之间的1个空格之后，再计算总的应该补的空格数
            numSpaces = maxWidth - len_sum + numWords - 1
            if j == len(words):  # last word
                line = ' '.join(words[i:j])
                line = line + ' '*(numSpaces - numWords + 1)
            elif numWords > 1:
                # 计算word之间avgSpaces
                avgSpaces = numSpaces // (numWords - 1)
                # 如果extraSpaces表示要在extraSpaces个words后面多+1个空格
                extraSpaces = numSpaces - avgSpaces * (numWords - 1)
                first = ' '*(avgSpaces+1)
                line = first.join(words[i:i+extraSpaces+1]) + ' '*avgSpaces + \
                    (' '*avgSpaces).join(words[i+extraSpaces+1:j])
            else:  # numWords = 1, 在右边补齐空格数
                line = words[i] + ' '*(numSpaces)
            result.append(line)
            i = j
        return result


# @lc code=end
