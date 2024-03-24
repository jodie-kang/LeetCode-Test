#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    # 单调递增栈
    def trap(self, height: List[int]) -> int:
        ans = 0  # 初始化雨水总量为 0
        stack = []  # 初始化栈，用于存储索引
        size = len(height)  # 获取数组的长度

        # 遍历数组的每个元素
        for i in range(size):
            # 当栈不为空且当前高度大于栈顶高度时，处理栈顶元素
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop(-1)  # 弹出栈顶元素的索引
                # 如果栈不为空，说明当前位置左边存在一个更高的柱子
                if stack:
                    left = stack[-1] + 1  # 当前位置左边的柱子索引
                    right = i - 1  # 当前位置右边的柱子索引
                    high = min(height[i], height[stack[-1]]) - height[cur]  # 计算雨水高度
                    ans += high * (right - left + 1)  # 累加雨水总量
                else:
                    # 如果栈为空，说明当前位置是左边的最高点，跳出循环
                    break
            # 将当前索引压入栈中
            stack.append(i)
        # 返回计算的雨水总量
        return ans
# @lc code=end

