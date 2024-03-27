#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
<<<<<<< HEAD
    # 使用一个栈来保存进行乘除运算后的整数值。正整数直接压入栈中，负整数，则将对应整数取负号，再压入栈中。这样最终计算结果就是栈中所有元素的和。
    # 具体做法：
    # 遍历字符串 s，使用变量 op 来标记数字之前的运算符，默认为 +。
    # 如果遇到数字，继续向后遍历，将数字进行累积，得到完整的整数 num。判断当前 op 的符号。
    # 如果 op 为 +，则将 num 压入栈中。
    # 如果 op 为 -，则将 -num 压入栈中。
    # 如果 op 为 *，则将栈顶元素 top 取出，计算 top * num，并将计算结果压入栈中。
    # 如果 op 为 /，则将栈顶元素 top 取出，计算 int(top / num)，并将计算结果压入栈中。
    # 如果遇到 +、-、*、/ 操作符，则更新 op。
    # 最后将栈中整数进行累加，并返回结果。
    def calculate(self, s: str) -> int:
        size = len(s)
        stack = []
        op = '+'
        index = 0
        while index < size:
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                # num = ord(s[index]) - ord('0')
                num = int(s[index])
                while index + 1 < size and s[index + 1].isdigit():
                    index += 1
                    num = 10 * num + ord(s[index]) - ord('0')
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))
            elif s[index] in "+-*/":
                op = s[index]
            index += 1
        return sum(stack)
        
=======
    def calculate(self, s: str) -> int:
>>>>>>> 1f2eac0a39c64e85d185c7f9f83bc1895a39f103
# @lc code=end

