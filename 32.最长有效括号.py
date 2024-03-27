#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    # 思路1：动态规划
    # dp[i] 表示为：以字符 s[i] 为结尾的最长有效括号的长度。则最终结果为 max(dp[i])
    def longestValidParentheses(self, s: str) -> int:
        # 初始化动态规划数组 dp，长度与字符串 s 相同
        dp = [0 for _ in range(len(s))]
        # 初始化最大长度 ans 为 0
        ans = 0

        # 从索引 1 开始遍历字符串 s
        for i in range(1, len(s)):
            # 如果当前字符是左括号 '('
            if s[i] == '(':
                # 跳过左括号，不做处理
                continue
            # 如果前一个字符是左括号 '('
            elif s[i - 1] == '(':
                # 如果当前位置至少有两个字符，尝试匹配最近的右括号 ')'
                if i >= 2:
                    # 如果匹配成功，更新 dp[i] 为匹配的最长有效括号长度
                    dp[i] = dp[i - 2] + 2
                else:
                    # 如果是字符串的开始，直接设置 dp[i] 为 2
                    dp[i] = 2
            # 如果前一个字符是右括号 ')'
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                # 如果当前位置减去 dp[i-1] 的值大于 0，说明存在一个匹配的左括号 '('
                if i - dp[i - 1] >= 2:
                    # 尝试匹配更远的右括号 ')'
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    # 如果是字符串的开始，直接设置 dp[i] 为 dp[i-1] + 2
                    dp[i] = dp[i - 1] + 2
            # 更新最长有效括号子串的长度
            ans = max(ans, dp[i])

        # 返回最长有效括号子串的长度
        return ans
            
    # 思路2：栈
    # 定义一个栈用于判定括号对是否匹配（栈中存储的是括号的下标），栈底元素始终保持「最长有效括号子串的开始元素的前一个元素下标」。
    # def longestValidParentheses(self, s: str) -> int:
    #     # 初始化栈，栈底元素为 -1，表示字符串的开始位置之前
    #     stack = [-1]
    #     # 初始化最大长度 ans 为 0
    #     ans = 0
    #     # 遍历字符串中的每个字符
    #     for i in range(len(s)):
    #         # 如果当前字符是左括号 '('
    #         if s[i] == "(":
    #             # 将左括号的下标压入栈中
    #             stack.append(i)
    #         else:
    #             # 如果当前字符是右括号 ')'
    #             # 弹出栈顶元素，即对应的左括号的下标
    #             stack.pop()
    #             # 如果栈不为空，说明找到了一个有效的括号对
    #             if stack:
    #                 # 更新最长有效括号子串的长度
    #                 ans = max(ans, i - stack[-1])
    #             else:
    #                 # 如果栈为空，说明当前右括号没有匹配的左括号
    #                 # 将当前右括号的下标压入栈中，作为新的最长有效括号子串的开始
    #                 stack.append(i)
    #     return ans
# @lc code=end

