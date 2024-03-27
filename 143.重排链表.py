#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 思路 1：线性表
    # 因为链表无法像数组那样直接进行随机访问。所以我们可以先将链表转为线性表，然后直接按照提要要求的排列顺序访问对应数据元素，重新建立链表。
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        vec = []
        cur = head
        while cur:
            vec.append(cur)
            cur = cur.next
        # 初始化左右指针，分别指向数组的开始和结束
        left, right = 0, len(vec) - 1
        # 当左指针小于右指针时，继续重新连接链表
        while left < right:
            # 将左指针指向的节点的 next 指针指向右指针指向的节点
            vec[left].next = vec[right]
            # 左指针向右移动
            left += 1
            # 如果左指针和右指针相遇，跳出循环
            if left == right:
                break
            # 将右指针指向的节点的 next 指针指向左指针指向的节点
            vec[right].next = vec[left]
            # 右指针向左移动
            right -= 1
        # 将链表中最后一个节点的 next 指针设置为 None，完成回文链表的构建
        vec[left].next = None
# @lc code=end

