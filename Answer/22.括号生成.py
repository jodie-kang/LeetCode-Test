#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    # 为了生成的括号组合是有效的，回溯的时候，使用一个标记变量 symbol 来表示是否当前组合是否成对匹配。
    # 如果在当前组合中增加一个 (，则令 symbol 加 1，如果增加一个 )，则令 symbol 减 1。
    # 显然只有在 symbol < n 的时候，才能增加 (，在 symbol > 0 的时候，才能增加 )。
    # 如果最终生成 2*n 的括号组合，并且 symbol == 0，则说明当前组合是有效的，将其加入到最终答案数组中。
    def generateParenthesis(self, n: int) -> List[str]:
        res = []        # 存放所有括号组合
        path = []       # 存放当前括号组合
        def backtrack(symbol, index):
            if n*2 == index:
                if symbol == 0:
                    res.append("".join(path))
            else:
                if symbol < n:
                    path.append("(")
                    backtrack(symbol+1, index+1)
                    path.pop()
                if symbol > 0:
                    path.append(")")
                    backtrack(symbol-1, index+1)
                    path.pop()
        backtrack(0, 0)
        return res
# @lc code=end

