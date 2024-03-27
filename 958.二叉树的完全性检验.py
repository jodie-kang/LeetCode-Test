#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # 对于一个完全二叉树，按照「层序遍历」的顺序进行广度优先搜索，在遇到第一个空节点之后，整个完全二叉树的遍历就已结束了。不应该在后续遍历过程中再次出现非空节点。
    # 如果在遍历过程中在遇到第一个空节点之后，又出现了非空节点，则该二叉树不是完全二叉树。
    # 利用这一点，我们可以在广度优先搜索的过程中，维护一个布尔变量 is_empty 用于标记是否遇见了空节点。
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = deque([root])
        is_empty = False
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    is_empty = True
                else:
                    if is_empty:
                        return False
                    queue.append(cur.left)
                    queue.append(cur.right)
        return True

# @lc code=end

