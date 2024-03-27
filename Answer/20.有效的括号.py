#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = list()
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")":
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ch in "}":
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif ch in "]":
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return False if stack else True
# @lc code=end

