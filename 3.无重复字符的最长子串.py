#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    # 用滑动窗口 window 来记录不重复的字符个数，window 为哈希表类型。
    # 设定两个指针：left、right，分别指向滑动窗口的左右边界，保证窗口中没有重复字符。
    # 一开始，left、right 都指向 0。
    # 向右移动 right，将最右侧字符 s[right] 加入当前窗口 window 中，记录该字符个数。
    # 如果该窗口中该字符的个数多于 1 个，即 window[s[right]] > 1，则不断右移 left，缩小滑动窗口长度，并更新窗口中对应字符的个数，直到 window[s[right]] <= 1。
    # 维护更新无重复字符的最长子串长度。然后继续右移 right，直到 right >= len(nums) 结束。
    # 输出无重复字符的最长子串长度。
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()
        left, right = 0, 0
        ans = 0
        # 遍历字符串
        while right < len(s):
            # 当前字符不在窗口中，将其加入字典，并设置频率为1
            if s[right] not in window:
                window[s[right]] = 1
            else:
                # 当前字符已在窗口中，增加该字符的频率
                window[s[right]] += 1
            
            # 当窗口中字符的频率大于1时，移动左指针
            # 直到窗口中没有重复的字符
            while window[s[right]] > 1:
                window[s[left]] -= 1  # 减少左指针对应的字符频率
                left += 1  # 移动左指针

            # 更新最长子串的长度
            ans = max(ans, right-left+1)
            
            # 移动右指针，向右扩展窗口
            right += 1
        return ans
# @lc code=end

