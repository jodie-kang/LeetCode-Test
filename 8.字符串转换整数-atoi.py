#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    # 思路 1：模拟
    # 先去除前后空格。
    # 检测正负号。
    # 读入数字，并用字符串存储数字结果。
    # 将数字字符串转为整数，并根据正负号转换整数结果。
    # 判断整数范围，并返回最终结果。
    def myAtoi(self, s: str) -> int:
        ans = ""
        positive = True
        start = 0
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            positive = False
            start = 1
        elif s[0] == '+':
            positive = True
            start = 1
        elif not s[0].isdigit():
            return 0
        for i in range(start, len(s)):
            if s[i].isdigit():
                ans += s[i]
            else:
                break
        if not ans:
            return 0
        
        num = int(ans)
        if not positive:
            num = -num
            return max(num, -2 ** 31)
        else:
            return min(num, 2 ** 31 - 1) 

# @lc code=end

