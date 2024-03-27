#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # reverse 函数通过 pre 和 cur 指针来反转链表中的一段节点，并更新 head 和 first 指针。
    # reverseKGroup 函数使用 cur 指针来遍历整个链表，并在每 k 个节点的链表段的开始处调用 reverse 函数来反转该段。
    # 使用 dummy_head 哨兵节点来简化边界条件，特别是当反转的链表段包括头节点时。
    # index 计数器用于确定何时到达新的 k 个节点的链表段的开始。
    # 时间复杂度：O(n)，其中 n 是链表的节点数。这是因为我们需要遍历链表中的每个节点一次。
    # 空间复杂度：O(1)，我们只使用了有限数量的额外空间（哨兵节点和几个指针）。
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 辅助函数，用于反转链表中的一段节点
        def reverse(head, tail):
            pre = head
            cur = pre.next
            first = cur
            while cur != tail:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            head.next = pre
            first.next = tail
            return first
        # 创建哨兵节点，其 next 指针指向原始链表的头节点
        dummy_head = ListNode(0)
        # 初始化哨兵节点的 next 指针为 head
        dummy_head.next = head
        # 初始化 cur 指针，指向哨兵节点
        cur = dummy_head
        # 初始化 tail 指针，指向当前处理的链表段的尾节点
        tail = dummy_head.next
        # 初始化 index 计数器
        index = 0
        # 遍历链表，当 tail 不为空时，继续处理
        while tail:
            # 每遍历一个节点，index 计数器加 1
            index += 1
            # 当 index 为 k 的倍数时，说明到达了新的 k 个节点的链表段的开始
            if index % k == 0:
                # 反转当前 k 个节点的链表段
                cur = reverse(cur, tail.next)
                # 更新 tail 指针，指向新的 k 个节点链表段的尾节点
                tail = cur.next
            else:
                # 不是 k 的倍数，说明还在当前 k 个节点的链表段中，继续遍历
                tail = tail.next
        # 返回哨兵节点的下一个节点，即新链表的头节点
        return dummy_head.next

# @lc code=end

