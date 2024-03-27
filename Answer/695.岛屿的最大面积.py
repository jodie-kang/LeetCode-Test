#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    # 思路 1：深度优先搜索
    # 遍历二维数组的每一个元素，对于每个值为 1 的元素：
    # 将该位置上的值置为 0（防止二次重复计算）。
    # 递归搜索该位置上下左右四个位置，并统计搜到值为 1 的元素个数。
    # 返回值为 1 的元素个数（即为该岛的面积）。
    # 维护并更新最大的岛面积。
    # 返回最大的到面积。
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    maxArea = max(maxArea, area)
        return maxArea
    
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
            return 0
        area = 1
        grid[i][j] = 0
        area += self.dfs(grid, i+1, j)
        area += self.dfs(grid, i, j+1)
        area += self.dfs(grid, i-1, j)
        area += self.dfs(grid, i, j-1)
        return area
# @lc code=end

