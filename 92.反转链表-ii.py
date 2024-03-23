#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 先遍历到需要反转的链表区间的前一个节点，然后对需要反转的链表区间进行迭代反转。最后再返回头节点即可。
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 初始化索引为 1，因为链表的第 1 个节点对应 left = 1
        index = 1
        # 创建哨兵节点，其 next 指针指向原始链表的头节点
        dummy_head = ListNode(0)
        dummy_head.next = head
        # 初始化 pre 指针，指向哨兵节点
        pre = dummy_head

        # 初始化 reverse_start 指针，用于反转链表的起始位置
        reverse_start = dummy_head
        # 找到反转开始位置的节点
        while reverse_start.next and index < left:
            reverse_start = reverse_start.next
            index += 1

        # 将 pre 指针移动到反转开始位置的前一个节点
        pre = reverse_start
        # 初始化 cur 指针，指向要反转的第一个节点
        cur = pre.next
        # 遍历并反转链表段
        while cur and index <= right:
            # 保存 cur 节点的下一个节点
            next = cur.next
            # 反转 cur 节点的 next 指针，让它指向 pre
            cur.next = pre
            # 更新 pre 指针，移动到 cur 的位置
            pre = cur
            # 更新 cur 指针，移动到下一个节点
            cur = next
            # 索引递增，继续处理下一个节点
            index += 1

        # 将反转后的链表的尾节点（pre）的下一个节点设置为 cur
        reverse_start.next.next = cur
        # 更新反转开始位置的节点的 next 指针，让它指向反转后的链表头节点（pre）
        reverse_start.next = pre
        
        # 返回哨兵节点的下一个节点，即新链表的头节点
        return dummy_head.next

# @lc code=end

