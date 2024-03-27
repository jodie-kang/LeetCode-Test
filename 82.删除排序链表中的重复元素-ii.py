#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个哨兵节点，其 next 指针指向原始链表的头节点
        dummy_head = ListNode(-1)
        dummy_head.next = head
        cur = dummy_head        # 使用 cur 指针遍历链表
        # 当 cur 指针和 cur 的下一个节点的下一个节点都存在时，继续循环
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:   # 如果 cur 指针指向的节点和它的下一个节点的值相同
                temp = cur.next                     # 将 temp 指针指向 cur 的下一个节点
                while temp and temp.next and temp.val == temp.next.val: # 遍历连续的重复节点
                    temp = temp.next
                cur.next = temp.next                        # 跳过连续的重复节点，将 cur 的下一个节点指向最后一个非重复节点的下一个节点
            else:
                cur = cur.next
        return dummy_head.next  # 返回哨兵节点的下一个节点，即新链表的头节点
# @lc code=end

