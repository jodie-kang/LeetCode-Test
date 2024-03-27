# 思路 1：栈
# 借助一个栈来模拟压入、压出的操作。检测最后是否能模拟成功。
def validStackSequence(pushed, poped):
    stack = []
    index = 0
    for item in pushed:
        stack.append(item)
        while (stack and stack[-1] == poped[index]):
            stack.pop()
            index += 1
    return len(stack) == 0

pushed = [1, 2, 3, 4, 5]
poped = [5, 4, 3, 2, 1]
print(validStackSequence(pushed, poped))