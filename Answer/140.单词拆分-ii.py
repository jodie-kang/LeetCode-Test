#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    # 这个问题可以通过使用动态规划和回溯来解决。首先，使用动态规划确定字符串 s 的哪些部分可以被成功分割成词典中的单词，然后使用回溯法来构建所有可能的句子。
    # 步骤 1: 动态规划（DP）
    # 初始化一个布尔型数组 dp，长度为 s.length + 1，dp[i] 表示字符串 s 的前 i 个字符是否可以被分割成 wordDict 中的单词。dp[0] = true，因为空字符串总是词典的一部分。
    # 对于字符串 s 的每个子字符串（从第 i 个字符到第 j 个字符），如果 dp[i] 为真，并且子字符串 s[i:j] 在词典 wordDict 中，那么将 dp[j+1] 设置为真。这表示从 s 的开始到第 j 个字符，字符串都可以被分割成词典中的单词。
    # 步骤 2: 回溯
    # 一旦我们通过动态规划确定了字符串 s 可以被分割成词典中的单词，我们使用回溯来构建所有可能的句子。
    # 从字符串 s 的开头开始，对于每个可能的单词结束索引（即 dp[j] == true），如果子字符串 s[i:j] 在词典中，则将其作为一个单词添加到当前句子中，并递归地继续寻找下一个单词的结束索引。
    # 如果到达字符串的末尾，将当前构建的句子添加到结果集中。
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        def backtrack(start, path):
            if start == len(s):
                res.append(' '.join(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                if dp[end] and s[start:end] in wordSet:
                    backtrack(end, path + [s[start:end]])
        
        res = []
        backtrack(0, [])
        return res

# @lc code=end

