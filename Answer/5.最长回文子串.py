#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # 思路 1：动态规划
    # 主要是定义状态转移方程，以及更新最长回文子串的位置和长度。初始化一个 n * n 大小的布尔类型数组 dp[][] ，dp[i][j] 表示字符串 s 上 从位置 i 到 j 的子串 s[i...j] 是否是一个回文串。
    # 可以很容易的看出来，当子串只有 1 位或 2 位的时候，如果 s[i] == s[j]，该子串为回文子串， dp[i][j] = (s[i] == s[j])。
    # 如果子串大于 2 位，则如果 s[i + 1...j - 1] 是回文串，且 s[i] == s[j]，则 s[i...j] 也是回文串，dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]。
    # 当判断完 s[i: j] 是否为回文串时，判断并更新最长回文子串的起始位置和最大长度。
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        max_start = 0
        max_len = 1
        for j in range(1, size):
            for i in range(j):
                if s[i] == s[j]:
                    if j-i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and (j-i+1) > max_len:
                    max_len = j - i + 1
                    max_start = i
        return s[max_start: max_start + max_len]
# @lc code=end

