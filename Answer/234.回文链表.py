#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 利用数组，将链表元素依次存入。
    # 然后再使用两个指针，一个指向数组开始位置，一个指向数组结束位置。
    # 依次判断首尾对应元素是否相等，如果都相等，则为回文链表。如果不相等，则不是回文链表。
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        return nodes == nodes[::-1]
# @lc code=end

