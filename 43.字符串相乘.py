#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    # 思路 1：模拟
    # 我们可以使用数组来模拟大数乘法。长度为 len(num1) 的整数 num1 与长度为 len(num2) 的整数 num2 相乘的结果长度为 len(num1) + len(num2) - 1 或 len(num1) + len(num2)。所以我们可以使用长度为 len(num1) + len(num2) 的整数数组 nums 来存储两个整数相乘之后的结果。
    # 整个计算流程的步骤如下：
    # 从个位数字由低位到高位开始遍历 num1，取得每一位数字 digit1。从个位数字由低位到高位开始遍历 num2，取得每一位数字 digit2。
    # 将 digit1 * digit2 的结果累积存储到 nums 对应位置 i + j + 1 上。
    # 计算完毕之后从 len(num1) + len(num2) - 1 的位置由低位到高位遍历数组 nums。将每个数位上大于等于 10 的数字进行进位操作，然后对该位置上的数字进行取余操作。
    # 最后判断首位是否有进位。如果首位为 0，则从第 1 个位置开始将答案数组拼接成字符串。如果首位不为 0，则从第 0 个位置开始将答案数组拼接成字符串。并返回答案字符串。
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
        len1, len2 = len(num1), len(num2)
        nums = [0 for _ in range(len1 + len2)]

        for i in range(len1-1, -1, -1):
            digit1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
                nums[i + j + 1] += digit1 * digit2
        
        for i in range(len1 + len2 -1, 0, -1):
            nums[i-1] += nums[i] // 10
            nums[i] %= 10
        if nums[0] == 0:
            ans = "".join(str(digit) for digit in nums[1:])
        else:
            ans = "".join(str(digit) for digit in nums[:])
        return ans

# @lc code=end

