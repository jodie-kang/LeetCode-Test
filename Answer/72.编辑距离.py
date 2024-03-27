#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#


# @lc code=start
class Solution:
    # 1. 划分阶段：按照两个字符串的结尾位置进行阶段划分。
    # 2. 定义状态 dp[i][j] 表示为：以 i - 1 为结尾的字符串 word1 变为以 j - 1 字结尾的字符串 word2 ，所使用的最少操作次数。
    # 3. 状态转移方程
    # 如果 word1[i - 1] == word2[j - 1]，无需插入、删除、替换。dp[i][j] 取源于以 i - 2 结尾结尾的字符串 word1 变为 j - 1 结尾的字符串 word2，即 dp[i][j] = dp[i - 1][j - 1]。
    # 如果 word1[i - 1] != word2[j - 1]，dp[i][j] 取源于以下三种情况中的最小情况：
    # word1 在 i - 1 位置上插入一个元素（等价于 word2 删除一个元素），最少操作次数依赖于以 i - 2 结尾的字符串 word1 变为以 j - 1 结尾的字符串 word2，再加上插入需要的操作数 1，即：dp[i - 1][j] + 1。
    # word2 在 j - 1 位置上插入一个元素（等价于 word1 删除一个元素），最少操作次数依赖于以 i - 1 结尾的字符串 word1 变为以 j - 2 结尾的字符串 word2，再加上插入需要的操作数 1，即：dp[i][j - 1] + 1。
    # word1[i - 1] 替换为 word2[j - 1]，最少操作次数依赖于以 i - 2 结尾的字符串 word1 变为以 j - 2 结尾的字符串 word2，再加上替换的操作数 1，即：dp[i - 1][j - 1] + 1。
    # 4. 初始条件
    # 当 word1 为空字符串，以 j - 1 结尾的字符串 word2 要删除 j 个字符才能和 word1 相同，即 dp[0][j] = j。
    # 当 word2 为空字符串，以 i - 1 结尾的字符串 word1 要删除 i 个字符才能和 word2 相同，即 dp[i][0] = i。
    # 5. 最终结果
    # 根据状态定义，最后输出 dp[sise1][size2]（即 word1 变为 word2 所使用的最少操作数）即可。其中 size1、size2 分别为 word1、word2 的字符串长度。
    def minDistance(self, word1: str, word2: str) -> int:
        size1, size2 = len(word1), len(word2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]
        for i in range(size1 + 1):
            dp[i][0] = i
        for j in range(size2 + 1):
            dp[0][j] = j

        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[size1][size2]

# @lc code=end
