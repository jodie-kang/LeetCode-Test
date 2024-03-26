#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # 思路 1：迭代
    # 遍历链表，利用哈希表，以 旧节点: 新节点 为映射关系，将节点关系存储下来。
    # 再次遍历链表，将新链表的 next 和 random 指针设置好。
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_dict = dict()
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            node_dict[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                node_dict[curr].next = node_dict[curr.next]
            if curr.random:
                node_dict[curr].random = node_dict[curr.random]
            curr = curr.next
        return node_dict[head]
# @lc code=end

