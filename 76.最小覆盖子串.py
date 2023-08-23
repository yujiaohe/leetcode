# @before-stub-for-debug-begin
from python3problem76 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [0, 0], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            # only if, have + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1

                # remove left one from window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r] if resLen != float('inf') else ""


# @lc code=end
