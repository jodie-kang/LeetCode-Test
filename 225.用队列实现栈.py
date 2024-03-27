#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
class MyStack:
    # 思路 1：双队列
    # 使用两个队列。pushQueue 用作入栈，popQueue 用作出栈。
    # push 操作：将新加入的元素压入 pushQueue 队列中，并且将之前保存在 popQueue 队列中的元素从队头开始依次压入 pushQueue 中，此时 pushQueue 队列中头节点存放的是新加入的元素，尾部存放的是之前的元素。 而 popQueue 则为空。再将 pushQueue 和 popQueue 相互交换，保持 pushQueue 为空，popQueue 则用于 pop、top 等操作。
    # pop 操作：直接将 popQueue 队头元素取出。
    # top 操作：返回 popQueue 队头元素。
    # empty：判断 popQueue 是否为空。

    def __init__(self):
        self.pushQueue = deque()
        self.popQueue = deque()

    def push(self, x: int) -> None:
        self.pushQueue.append(x)
        while self.popQueue:
            self.pushQueue.append(self.popQueue.popleft())
        self.pushQueue, self.popQueue = self.popQueue, self.pushQueue

    def pop(self) -> int:
        return self.popQueue.popleft()

    def top(self) -> int:
        return self.popQueue[0]

    def empty(self) -> bool:
        return not self.popQueue



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

