#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路 1：广度优先搜索
    # 判断二叉树是否为空，为空则直接返回。
    # 令根节点入队。
    # 当队列不为空时，求出当前队列长度 si。
    # 依次从队列中取出这 si 个元素，并对这 si 个元素依次进行访问。然后将其左右孩子节点入队，然后继续遍历下一层节点。
    # 当队列为空时，结束遍历。
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        order = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level:
                order.append(level)
        return order


# @lc code=end

