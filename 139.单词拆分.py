#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    # 1. 划分阶段：按照单词结尾位置进行阶段划分。
    # 2. 定义状态 dp[i] 表示：长度为 i 的字符串 s[0: i] 能否拆分成单词，如果为 True 则表示可以拆分，如果为 False 则表示不能拆分。
    # 3. 状态转移方程
    # 如果 s[0: j] 可以拆分为单词（即 dp[j] == True），并且字符串 s[j: i] 出现在字典中，则 dp[i] = True。
    # 如果 s[0: j] 不可以拆分为单词（即 dp[j] == False），或者字符串 s[j: i] 没有出现在字典中，则 dp[i] = False。
    # 4. 初始条件: 长度为 0 的字符串 s[0: i] 可以拆分为单词，即 dp[0] = True。
    # 5. 最终结果：根据我们之前定义的状态，dp[i] 表示：长度为 i  的字符串 s[0: i] 能否拆分成单词。则最终结果为 dp[size]，size 为字符串长度。
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False for _ in range(size + 1)]
        dp[0] = True
        for i in range(size + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[size]
# @lc code=end

