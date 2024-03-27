#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    # 思路 1：栈
    # 使用两个栈 stack1、stack2。stack1 用来保存左括号前已经解码的字符串，stack2 用来存储左括号前的数字。
    # 用 res 存储待解码的字符串、num 存储当前数字。
    # 遍历字符串。
    # 如果遇到数字，则累加数字到 num。
    # 如果遇到左括号，将当前待解码字符串入栈 stack1，当前数字入栈 stack2，然后将 res、nums 清空。
    # 如果遇到右括号，则从 stack1 的取出待解码字符串 res，从 stack2 中取出当前数字 num，将其解码拼合成字符串赋值给 res。
    # 如果遇到其他情况（遇到字母），则将当前字母加入 res 中。
    # 遍历完输出解码之后的字符串 res。
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack1.append(res)
                stack2.append(num)
                res = ""
                num = 0
            elif ch == ']':
                cur_res = stack1.pop()
                cur_num = stack2.pop()
                res = cur_res + res * cur_num
            else:
                res += ch
        return res
                
# @lc code=end

