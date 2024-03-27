#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while True:
            # 从左到右: row=up，col=col+1
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
            # 从上到下：row=row+1，col=right
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            # 从右到左：row=down，col=col-1
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down:
                break
            # 从下到上：row=row-1，col=left
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res
# @lc code=end

