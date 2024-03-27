#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 思路 1：迭代
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
    # 思路 2：递归
    # 时间复杂度：O(n)，空间复杂度：O(n)
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None or head.next == None:
    #         return head
    #     new_head = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return new_head
        
# @lc code=end

