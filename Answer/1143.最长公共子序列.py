#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#


# @lc code=start
class Solution:
    # 动态规划
    # 定义状态 dp[i][j] 表示为：前 i 个字符组成的字符串 str1 与前 j 个字符组成的字符串 str2 的最长公共子序列长度为 dp[i][j]。
    # 双重循环遍历字符串 text1 和 text2，则状态转移方程为：
    # 如果 text1[i - 1] == text2[j - 1]，则说明找到了一个公共字符，此时 dp[i][j] = dp[i - 1][j - 1] + 1。
    # 如果 text1[i - 1] != text2[j - 1]，则 dp[i][j] 需要考虑以下两种情况，取两种情况中最大的那种：dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])。
    # text1 前 i - 1 个字符组成的字符串 str1 与 text2 前 j 个字符组成的 str2 的最长公共子序列长度，即 dp[i - 1][j]。
    # text1 前 i 个字符组成的字符串 str1 与 text2 前 j - 1 个字符组成的 str2 的最长公共子序列长度，即 dp[i][j - 1]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]
        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[size1][size2]


# @lc code=end
