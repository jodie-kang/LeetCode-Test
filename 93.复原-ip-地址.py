#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def check(self, ip_lst):
        for ch in ip_lst:
            if int(ch) < 0 and int(ch) > 255:
                return False
        return True

    # 1. 定义回溯函数：
    # backtracking(index): 函数的传入参数是 index（剩余字符开始位置），全局变量是 res（存放所有符合条件结果的集合数组）和 path（存放当前符合条件的结果）。
    # backtracking(index): 函数代表的含义是：递归从 index 位置开始，从剩下字符中，选择当前子段的值
    # 2. 书写回溯函数主体（给出选择元素、递归搜索、撤销选择部分）。
    # 3. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。
    # 当遍历到决策树的叶子节点时，就终止了。也就是存放当前结果的数组 path 的长度等于 4，并且剩余字符开始位置为字符串结束位置（即 len(path) == 4 and index == len(s)）时，递归停止。
    # 如果回溯过程中，切割次数大于 4（即 len(path) > 4），递归停止，直接返回。
    # 时间复杂度：O(3^4 * |s|)，其中 |s| 是字符串 s 的长度。由于 IP 地址的每一子段位数不会超过 3，因此在递归时，我们最多只会深入到下一层中的 3 种情况。
    # 而 IP 地址由 4 个子段构成，所以递归的最大层数为 4 层，则递归的时间复杂度为 O(3^4) 
    # 。而每次将有效的 IP 地址添加到答案数组的时间复杂度为 |s|)，所以总的时间复杂度为 O(3^4 * |s|) 。
    # 空间复杂度：O(|s|)，只记录除了用来存储答案数组之外的空间复杂度。
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def backtrack(index):
            if len(path) > 4:                       # 如果切割次数大于 4，直接返回
                return
            if len(path) == 4 and index == len(s):  # 切割完成，将当前结果加入答案结果数组中
                res.append(".".join(path))
                return
            
            for i in range(index, len(s)):
                sub = s[index: i+1]
                if int(sub) > 255:                     # 如果当前值不在 0 ~ 255 之间，直接跳过
                    continue
                if int(sub) == 0 and i != index:       # 如果当前值为 0，但不是单个 0（"00..."），直接跳过
                    continue
                if int(sub) > 0 and s[index] == '0':   # 如果当前值大于 0，但是以 0 开头（"0XX..."），直接跳过
                    continue
                path.append(sub)
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res

# @lc code=end

