#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    # 使用两个栈，inStack 用于输入，outStack 用于输出。
    # push 操作：将元素压入 inStack 中。
    # pop 操作：如果 outStack 输出栈为空，将 inStack 输入栈元素依次取出，按顺序压入 outStack 栈。这样 outStack 栈的元素顺序和之前 inStack 元素顺序相反，outStack 顶层元素就是要取出的队头元素，将其移出，并返回该元素。如果 outStack 输出栈不为空，则直接取出顶层元素。
    # peek 操作：和 pop 操作类似，只不过最后一步不需要取出顶层元素，直接将其返回即可。
    # empty 操作：如果 inStack 和 outStack 都为空，则队列为空，否则队列不为空。
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        self.outStack.pop()
        return top

    def peek(self) -> int:
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        return top

    def empty(self) -> bool:
        return len(self.inStack) == 0 and len(self.outStack) == 0
 
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

