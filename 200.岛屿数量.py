#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    # 思路 1：深度优先搜索
    # 遍历 grid 。
    # 对于每一个字符为 '1' 的元素，遍历其上下左右四个方向，并将该字符置为 0，保证下次不会被重复遍历。
    # 如果超出边界，则返回 0。
    # 对于 (i, j) 位置的元素来说，递归遍历的位置就是 (i - 1, j)、(i, j - 1)、(i + 1, j)、(i, j + 1) 四个方向。每次遍历到底，统计数记录一次。
    # 最终统计出深度优先搜索的次数就是我们要求的岛屿数量。
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        
# @lc code=end

