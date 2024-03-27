#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # maxWidth = 0
        # queue = deque([root])
        # while queue:
        #     size = len(queue)
        #     level = []
        #     for _ in range(size):
        #         cur = queue.popleft()
        #         level.append(cur.val)
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        #     maxWidth = max(maxWidth, len(level))
        # return maxWidth
    # 二叉树的宽度是指任意一层上最左边和最右边的非空节点之间的节点数目（包括空节点）。上面的代码实际上只计算了每一层非空节点的数量，而没有考虑到两端非空节点之间的空节点。
    # 为了正确计算二叉树的最大宽度，我们需要跟踪每个节点的位置信息。通常，我们可以将根节点的位置设为 0，然后对于任意一个节点的位置 i，其左子节点的位置是 2*i + 1，右子节点的位置是 2*i + 2。使用这种方法，即使某些节点是空的，我们也可以通过节点位置来准确计算出任一层的宽度。
        if not root:
            return 0
        maxWidth = 0
        queue = deque([(root, 0)])  # 队列中存储节点及其位置信息
        while queue:
            level_length = len(queue)
            _, first_pos = queue[0]  # 当前层第一个节点的位置
            _, last_pos = queue[-1]  # 当前层最后一个节点的位置
            maxWidth = max(maxWidth, last_pos - first_pos + 1)  # 更新最大宽度
            for _ in range(level_length):
                node, pos = queue.popleft()
                # 如果节点存在，则将其子节点及其位置加入队列
                if node.left:
                    queue.append((node.left, 2*pos+1))
                if node.right:
                    queue.append((node.right, 2*pos+2))
        return maxWidth


# @lc code=end

