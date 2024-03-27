#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    # 跟「0039. 组合总和」不一样的地方在于本题不能有重复组合，所以关键步骤在于去重。
    # 在回溯遍历的时候，下一层递归的 start_index 要从当前节点的后一位开始遍历，即 i + 1 位开始。
    # 而且统一递归层不能使用相同的元素，即需要增加一句判断 if i > start_index and candidates[i] == candidates[i - 1]: continue。
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(total, startIndex):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(startIndex, len(candidates)):
                if i> startIndex and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                total += candidates[i]
                path.append(candidates[i])
                backtrack(total, i+1)
                total -= candidates[i]
                path.pop()
        candidates.sort()
        backtrack(0, 0)
        return res

# @lc code=end

