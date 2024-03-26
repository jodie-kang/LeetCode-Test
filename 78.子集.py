#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    # 思路：回溯算法
    # 1. 明确所有选择：根据数组中每个位置上的元素选与不选两种选择
    # 2. 明确终止条件：当遍历到决策树的叶子节点时，就终止了。即当前路径搜索到末尾时，递归终止。
    # 3. 将决策树和终止条件翻译成代码：
    #  1、定义回溯函数：
    # backtracking(nums, index): 函数的传入参数是 nums（可选数组列表）和 index（代表当前正在考虑元素是 nums[i] ），全局变量是 res（存放所有符合条件结果的集合数组）和 path（存放当前符合条件的结果）。
    # backtracking(nums, index): 函数代表的含义是：在选择 nums[index] 的情况下，递归选择剩下的元素。
    #  2、书写回溯函数主体（给出选择元素、递归搜索、撤销选择部分）。
    # 从当前正在考虑元素，到数组结束为止，枚举出所有可选的元素。对于每一个可选元素：
    # 约束条件：之前选过的元素不再重复选用。每次从 index 位置开始遍历而不是从 0 位置开始遍历就是为了避免重复。集合跟全排列不一样，子集中 {1, 2} 和 {2, 1} 是等价的。为了避免重复，我们之前考虑过的元素，就不再重复考虑了。
    # 选择元素：将其添加到当前子集数组 path 中。
    # 递归搜索：在选择该元素的情况下，继续递归考虑下一个位置上的元素。
    # 撤销选择：将该元素从当前子集数组 path 中移除。
    #  3、明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。
    # 当遍历到决策树的叶子节点时，就终止了。也就是当正在考虑的元素位置到达数组末尾（即 start >= len(nums)）时，递归停止。
    # 从决策树中也可以看出，子集需要存储的答案集合应该包含决策树上所有的节点，应该需要保存递归搜索的所有状态。所以无论是否达到终止条件，我们都应该将当前符合条件的结果放入到集合中。
    # 时间复杂度：O(n * 2^n)，其中 n 指的是数组 nums 的元素个数，2^n 指的是所有状态数。每种状态需要 O(n) 的时间来构造子集。
    # 空间复杂度：O(n) ，每种状态下构造子集需要使用 O(n) 的空间。
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(nums, index):
            res.append(path[:])
            if index >= len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums, index+1)
                path.pop()
        backtrack(nums, 0)
        return res

# @lc code=end

