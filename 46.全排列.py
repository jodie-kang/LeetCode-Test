#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    # 思路 1：回溯算法
    # 1. 明确所有选择：全排列中每个位置上的元素都可以从剩余可选元素中选出
    # 2. 明确终止条件：当遍历到决策树的叶子节点时，就终止了。即当前路径搜索到末尾时，递归终止。
    # 3. 将决策树和终止条件翻译成代码：
    # 时间复杂度：O(n * n!)，其中 n 为数组 nums 的元素个数。
    # 空间复杂度：O(n)。
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])# 选择元素
                    backtrack(nums)     # 继续递归下一个元素
                    path.pop()          # 撤销选择
        backtrack(nums)
        return res
# @lc code=end

