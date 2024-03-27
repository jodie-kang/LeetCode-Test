#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import defaultdict
# @lc code=start
class Solution:
    # 使用两个字典 need 和 window 分别记录目标字符串 t 和当前窗口中各字符的计数。
    # 使用左右指针 left 和 right 遍历字符串 s，扩展窗口直到包含 t 中所有字符。
    # 当窗口有效（包含 t 中所有字符）时，尝试收缩左边界来寻找最小子串。
    # 更新记录的最小子串的起始位置 start 和长度 size。
    # 如果最终没有找到满足条件的子串，返回空字符串 ""；否则，返回找到的最小子串。
    # 时间复杂度：O(n)，其中 n 是字符串 s 的长度。这是因为每个字符最多被访问两次（一次扩展窗口，一次收缩窗口）。字典操作（插入和删除）的时间复杂度为 O(1)，因此总的时间复杂度线性依赖于字符串 s 的长度。
    def minWindow(self, s: str, t: str) -> str:
        # 初始化目标字符集need和当前窗口字符集window
        need = defaultdict(int)
        window = defaultdict(int)
        # 遍历目标字符串t，记录每个字符及其出现次数
        for ch in t:
            need[ch] += 1

        # 初始化左右指针、有效字符计数、最小子串的起始位置和长度
        left, right = 0, 0
        valid = 0  # 有效字符计数，表示当前窗口中包含的t中的字符数量
        start = 0  # 最小子串的起始位置
        size = len(s) + 1  # 最小子串的长度，初始化为一个较大的值

        # 遍历字符串s，寻找涵盖t所有字符的最小子串
        while right < len(s):
            # 扩展窗口，将右指针指向的字符加入到当前窗口
            insert_ch = s[right]
            right += 1

            # 如果该字符是目标字符，则更新窗口字典中的计数
            if insert_ch in need:
                window[insert_ch] += 1
                # 如果当前字符的计数达到目标字符的计数，则有效字符计数加一
                if window[insert_ch] == need[insert_ch]:
                    valid += 1

            # 当有效字符计数等于目标字符串的长度时，尝试收缩窗口
            while valid == len(need):
                # 如果当前窗口的长度小于已记录的最小子串长度，则更新最小子串的起始位置和长度
                if right - left < size:
                    start = left
                    size = right - left
                # 收缩窗口，将左指针指向的字符从当前窗口中移除
                remove_ch = s[left]
                left += 1
                # 如果该字符是目标字符，并且移除后计数仍等于目标计数，则有效字符计数减一
                if remove_ch in need:
                    if window[remove_ch] == need[remove_ch]:
                        valid -= 1
                    window[remove_ch] -= 1
        # 如果最终没有找到涵盖t所有字符的子串，返回空字符串
        if size == len(s) + 1:
            return ''
        # 返回找到的最小子串
        return s[start:start+size]

# @lc code=end

