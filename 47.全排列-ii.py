#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    # 思路 1：回溯算法
    # 这道题跟「0046. 全排列」不一样的地方在于增加了序列中的元素可重复这一条件。这就涉及到了如何去重。
    # 我们可以先对数组 nums 进行排序，然后使用一个数组 visited 标记该元素在当前排列中是否被访问过。
    # 如果未被访问过则将其加入排列中，并在访问后将该元素变为未访问状态。
    # 然后再递归遍历下一层元素之前，增加一句语句进行判重：if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue。
    # 然后再进行回溯遍历。
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False for _ in range(len(nums))]
        path = []
        res = []
        def backtrack(nums, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(nums, visited)
                    visited[i] = False
                    path.pop()
        backtrack(nums, visited)
        return res

# @lc code=end