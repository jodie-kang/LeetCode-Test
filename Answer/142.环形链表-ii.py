#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 假设入环位置为 A，快慢指针在 B 点相遇，则相遇时慢指针走了 a+b 步，快指针走了 a+n(b+c)+b 步。
    # 因为快指针总共走的步数是慢指针走的步数的两倍，即  2(a+b) = a + n(b+c) + b，所以可以推出：a = c + (n-1)(b+c)。
    # 我们可以发现：从相遇点到入环点的距离 c 加上 n-1 圈的环长 b+c 刚好等于从链表头部到入环点的距离。
    def detectCycle(self, head: ListNode) -> ListNode:
        # 初始化快慢两个指针，都从链表头节点开始
        fast, slow = head, head
        
        # 使用 while 循环进行快慢指针的移动
        while True:
            # 如果快指针到达链表尾部或其下一个节点不存在，说明链表中没有环
            if not fast or not fast.next:
                return None
            # 移动快指针两步（fast指针每次跳过两个节点）
            fast = fast.next.next
            # 移动慢指针一步（slow指针每次只移动一个节点）
            slow = slow.next
            # 如果快慢指针相遇，说明链表中存在环
            if fast == slow:
                break
        # 初始化 ans 指针，用于找到环的入口节点，并从链表头开始
        ans = head
        # 当 ans 指针和慢指针不相遇时，继续循环
        while ans != slow:
            # 同时移动 ans 和慢指针一步
            ans, slow = ans.next, slow.next
        # 返回环的入口节点
        return ans
# @lc code=end

