#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution:
    # 思路 1：栈
    # 借助一个栈来模拟压入、压出的操作。检测最后是否能模拟成功。
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for item in pushed:
            stack.append(item)
            while (stack and stack[-1] == popped[index]):
                stack.pop()
                index += 1
        return len(stack) == 0
# @lc code=end

