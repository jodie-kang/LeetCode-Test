# 给定 n 和 k，求n的全排列中字典序第k个排列.
# 思路1：数学问题
# 算法的基本思想是利用全排列的性质和“字典序”的概念。对于n个不同的元素，它们的全排列总数是n!。如果我们固定第一个元素，后面的n-1个元素的排列总数是(n-1)!。这个性质可以用来确定每个位置上的元素。
# 从最高位开始，确定每一位的数字。比如，知道第一位数字后，剩下的n-1位有(n-1)!种排列方式。
# 用k除以(n-1)!可以确定字典序中的第一个数字是什么。因为如果k小于(n-1)!，那么第一个数字就是序列中的第一个数字。如果k在1*(n-1)!到2*(n-1)!之间，那么第一个数字是序列中的第二个数字，依此类推。
# 确定第一位数字后，更新k值（减去前面已经确定的部分），然后对剩下的n-1个数字重复上述过程，直到所有位都确定下来。
# def getPermutation(n, k):
#     import math
#     nums = list(range(1, n+1))
#     permutations = ""
#      # 由于索引从0开始，我们将k减1使其对应内部的0-based索引
#     k -= 1
    
#     while n > 0:
#         n -= 1
#         # 计算当前位的索引
#         index, k = divmod(k, math.factorial(n))
#         # 添加对应的数字到结果字符串
#         permutation += str(nums[index])
#         # 从列表中移除已经使用的数字
#         nums.pop(index)
#     return permutations

# 思路2：回溯
# 使用回溯算法来求解给定整数n的全排列中字典序第k个排列的问题，需要生成所有可能的排列，然后排序这些排列并找到第k个排列。不过，实际上，通过优化回溯过程，我们可以在找到第k个排列时立即停止，而不是生成所有排列。
def getPermutation(n, k):
    res = []
    visited = [False] * (n+1)
    def backtrack(path):
        if len(path) == n:
            res.append("".join(path))
            return
        for i in range(1, n+1):
            if visited[i]:
                continue
            if len(res) == k:
                return
            path.append(str(i))
            visited[i] = True
            backtrack(path)
            path.pop()
            visited[i] = False
    backtrack([])
    return res[-1] if res else ""


n = 3
k = 3
print(getPermutation(n, k))