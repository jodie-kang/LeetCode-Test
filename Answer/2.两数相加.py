#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 首先初始化一个哑节点dummy_head，它的下一个节点将是结果链表的第一个有效节点。然后，我们使用一个while循环来遍历两个输入链表，同时处理进位。在每次迭代中，我们计算两个链表当前节点的值之和，并加上之前的进位。然后，我们更新进位，并创建一个新的链表节点来存储个位数的和。最后，如果还有剩余的进位，我们添加一个新的节点到结果链表中。最终，我们返回哑节点的下一个节点，即结果链表的头节点。
    # 时间复杂度：O(max(M, N))，空间复杂度：O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化结果链表的头节点和当前节点
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0  # 进位变量

        # 遍历两个链表直到其中一个遍历完毕
        while l1 or l2:
            # 计算两个链表当前节点的值，或者0如果已经遍历完毕
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 计算总和和进位
            total = val1 + val2 + carry
            carry = total // 10  # 更新进位
            # 创建新节点，值为个位数总和
            current.next = ListNode(total % 10)
            # 移动当前节点到下一个位置
            current = current.next

            # 移动链表l1和l2的指针
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 如果最后还有进位，添加一个新节点
        if carry > 0:
            current.next = ListNode(carry)

        # 返回结果链表的头节点的下一个节点，因为dummy_head是一个哑节点
        return dummy_head.next

# @lc code=end

