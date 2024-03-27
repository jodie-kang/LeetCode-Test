#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 思路：分而治之的思想。将链表数组不断二分，转为规模为二分之一的子问题，然后再进行归并排序。
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        size = len(lists)
        return self.mergeSort(lists, 0, size-1)
    # 二分环节，将链表数组不断二分，转为规模为二分之一的子问题
    def mergeSort(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        node_left = self.mergeSort(lists, left, mid)
        node_right = self.mergeSort(lists, mid+1, right)
        return self.merge(node_left, node_right)
    # 归并环节
    def merge(self, left, right):
        dummy_head = ListNode(-1)
        cur = dummy_head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left if left else right
        return dummy_head.next
# @lc code=end

