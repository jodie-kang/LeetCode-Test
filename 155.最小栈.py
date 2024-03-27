#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:
    # 使用辅助栈保存当前栈中的最小值。在元素入栈出栈时，两个栈同步保持插入和删除。具体做法如下：
    # push 操作：当一个元素入栈时，取辅助栈的栈顶存储的最小值，与当前元素进行比较得出最小值，将最小值插入到辅助栈中；该元素也插入到正常栈中。
    # pop 操作：当一个元素要出栈时，将辅助栈的栈顶元素一起弹出。
    # top 操作：返回正常栈的栈顶元素值。
    # getMin 操作：返回辅助栈的栈顶元素值。

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

