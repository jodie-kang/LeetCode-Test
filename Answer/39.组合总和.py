#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    # 1. 定义回溯函数。backtrack(total, start_index): 函数的传入参数是 total（当前和）、start_index（剩余可选元素开始位置），
    # 当前组合和为 total，递归从 candidates 的 start_index 位置开始，选择剩下的元素。
    # 全局变量是 res（存放所有符合条件结果的集合数组）和 path（存放当前符合条件的结果）。
    # 2. 书写回溯函数主体（给出选择元素、递归搜索、撤销选择部分）。
    # 3. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。
    # 当不可能再出现解（total > target），或者遍历到决策树的叶子节点时（total == target）时，就终止了。
    # 当遍历到决策树的叶子节点时（total == target）时，将当前结果的数组 path 放入答案数组 res 中，递归停止。
    # 时间复杂度：O(2^n * n) ，其中 n 是数组 candidates 的元素个数，2^n 指的是所有状态数。
    # 空间复杂度：O(target)，递归函数需要用到栈空间，栈空间取决于递归深度，最坏情况下递归深度为 O(target) ，所以空间复杂度为 O(target)。
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(total, startIndex):                   # 1. 定义回溯函数
            if total > target:                              # 3. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(startIndex, len(candidates)):    # 2. 书写回溯函数主体（给出选择元素、递归搜索、撤销选择部分）。
                if total + candidates[i] > target:
                    break
                total += candidates[i]
                path.append(candidates[i])
                backtrack(total, i)
                total -= candidates[i]
                path.pop()
        candidates.sort()
        backtrack(0, 0)
        return res

# @lc code=end

