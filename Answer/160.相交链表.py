#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 思路 1：双指针
    # 如果两个链表相交，那么从相交位置开始，到结束，必有一段等长且相同的节点。假设链表 listA 的长度为 m、链表 listB 的长度为 n，他们的相交序列有 k 个，
    # 考虑将链表 listA 的末尾拼接上链表 listB，链表 listB 的末尾拼接上链表 listA。
    # 然后使用两个指针 pA 、pB，分别从链表 listA、链表 listB 的头节点开始遍历，如果走到共同的节点，则返回该节点。
    # 否则走到两个链表末尾，返回 None
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA
        return pA
# @lc code=end

