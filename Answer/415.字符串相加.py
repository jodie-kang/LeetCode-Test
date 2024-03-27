#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    # 初始化一个空列表result用于存储结果的每一位，以及一个变量carry用于存储进位。
    # 使用一个for循环遍历两个字符串中的每一位，从最低位开始。如果当前位超出了某一个字符串的长度，我们将其视为0。
    # 在每次迭代中，计算两个字符串当前位的数字之和加上进位carry。
    # 更新进位carry为当前总和除以10的商。
    # 将当前总和除以10的余数（即当前位的和）添加到result列表中。
    # 遍历完成后，如果还有剩余的进位，将其添加到结果列表中。
    # 由于我们是从低位到高位添加的数字，所以需要反转result列表，然后将其连接成一个字符串作为最终结果返回。
    # 时间复杂度：O(max(m, n))，其中m和n分别是num1和num2的长度。这是因为我们需要遍历两个字符串中的每一位，而最长的字符串决定了循环的次数。
    def addStrings(self, num1: str, num2: str) -> str:
        # 初始化结果字符串和进位
        result = []
        carry = 0

        # 遍历两个字符串，从最低位开始
        for i in range(max(len(num1), len(num2))):
            # 获取 num1 和 num2 的当前位的值（如果存在）
            digit1 = int(num1[-i-1]) if i < len(num1) else 0
            digit2 = int(num2[-i-1]) if i < len(num2) else 0

            # 计算当前位的和及进位
            total = digit1 + digit2 + carry
            # 更新进位
            carry = total // 10
            # 将当前位的和（模10）添加到结果列表
            result.append(str(total % 10))

        # 如果最后还有进位，添加到结果列表
        if carry:
            result.append(str(carry))

        # 由于我们是从低位到高位添加的，所以需要反转结果列表
        return ''.join(reversed(result))# @lc code=end

