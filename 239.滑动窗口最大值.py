#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
import heapq

class Solution:
    # 思路 1：优先队列
    # 初始的时候将前 k 个元素加入优先队列的二叉堆中。存入优先队列的是数组值与索引构成的元组。优先队列将数组值作为优先级。
    # 然后滑动窗口从第 k 个元素开始遍历，将当前数组值和索引的元组插入到二叉堆中。
    # 当二叉堆堆顶元素的索引已经不在滑动窗口的范围中时，即 q[0][1] <= i - k 时，不断删除堆顶元素，直到最大值元素的索引在滑动窗口的范围中。
    # 将最大值加入到答案数组中，继续向右滑动。
    # 滑动结束时，输出答案数组。
    # 时间复杂度：O(n * log(k))，其中n是数组nums的长度。这是因为我们需要遍历数组中的每个元素（O(n)），并且在每次迭代中，我们可能需要在堆中执行插入和删除操作，每个操作的时间复杂度为O(log(k))，因为堆的大小最多为k。
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        # 初始化一个堆，堆中的元素是(-nums[i], i)的元组，其中i是nums[i]的索引
        # 使用负号是因为heapq默认是最小堆，我们用负号来实现最大堆的功能
        q = [(-nums[i], i) for i in range(k)]
        # 将列表转换成堆
        heapq.heapify(q)
        # 初始化结果列表，存储堆中最大元素的值（取反后）
        res = [-q[0][0]]

        # 从数组的第k个元素开始遍历到最后
        for i in range(k, size):
            # 将当前元素加入堆中
            heapq.heappush(q, (-nums[i], i))
            # 移除堆中索引小于当前索引减去k的元素，因为它们已经不在窗口内
            while q[0][1] <= i - k:
                heapq.heappop(q)
            # 将堆顶元素的值（即当前窗口的最大值）取反后加入结果列表
            res.append(-q[0][0])

        return res

# @lc code=end

