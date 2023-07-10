#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        x, y = len(a) - 1, len(b) - 1
        while x >= 0 and y >= 0:
            total = int(a[x]) + int(b[y]) + carry
            result += str(total % 2)
            carry = total // 2
            x -= 1
            y -= 1

        while x >= 0:
            total = int(a[x]) + carry
            result += str(total % 2)
            carry = total // 2
            x -= 1

        while y >= 0:
            total = int(b[y]) + carry
            result += str(total % 2)
            carry = total // 2
            y -= 1

        result = result[::-1]
        return str(carry) + result if carry else result

# @lc code=end
