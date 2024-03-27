#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 利用归并排序的思想，具体步骤如下：
    # 使用哑节点 dummy_head 构造一个头节点，并使用 curr 指向 dummy_head 用于遍历。
    # 然后判断 list1 和 list2 头节点的值，将较小的头节点加入到合并后的链表中。并向后移动该链表的头节点指针。
    # 然后重复上一步操作，直到两个链表中出现链表为空的情况。
    # 将剩余链表链接到合并后的链表中。
    # 将哑节点 dummy_dead 的下一个链节点 dummy_head.next 作为合并后有序链表的头节点返回。
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        cur = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 is not None else list2
        return dummy_head.next

# @lc code=end

