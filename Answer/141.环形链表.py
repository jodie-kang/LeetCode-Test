#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 思路 2：快慢指针（Floyd 判圈算法）
    # 这种方法类似于在操场跑道跑步。两个人从同一位置同时出发，如果跑道有环（环形跑道），那么快的一方总能追上慢的一方。
    # 基于上边的想法，Floyd 用两个指针，一个慢指针（龟）每次前进一步，快指针（兔）指针每次前进两步（两步或多步效果是等价的）。
    # 如果两个指针在链表头节点以外的某一节点相遇（即相等）了，那么说明链表有环。
    # 否则，如果（快指针）到达了某个没有后继指针的节点时，那么说明没环。
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
# @lc code=end

