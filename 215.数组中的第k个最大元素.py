#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import random
import heapq

class Solution:
    # 思路1：快速排序
    # 使用快速排序在每次调整时，都会确定一个元素的最终位置，且以该元素为界限，将数组分成了左右两个子数组，左子数组中的元素都比该元素小，右子树组中的元素都比该元素大。
    # 这样，只要某次划分的元素恰好是第 k 个下标就找到了答案。并且我们只需关注第 k 个最大元素所在区间的排序情况，与第 k 个最大元素无关的区间排序都可以忽略。这样进一步减少了执行步骤。
    # 时间复杂度：O(n)，空间复杂度：O(log n)

    # 从 arr[low: high + 1] 中随机挑选一个基准数，并进行移动排序
    # def randomPartition(self, arr: [int], low: int, high: int):
    #     # 随机挑选一个基准数
    #     i = random.randint(low, high)
    #     # 将基准数与最低位互换
    #     arr[i], arr[low] = arr[low], arr[i]
    #     # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
    #     return self.partition(arr, low, high)

    # # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
    # def partition(self, arr: [int], low: int, high: int):
    #     pivot = arr[low]            # 以第 1 为为基准数
    #     i = low + 1                 # 从基准数后 1 位开始遍历，保证位置 i 之前的元素都小于基准数
        
    #     for j in range(i, high + 1):
    #         # 发现一个小于基准数的元素
    #         if arr[j] < pivot:
    #             # 将小于基准数的元素 arr[j] 与当前 arr[i] 进行换位，保证位置 i 之前的元素都小于基准数
    #             arr[i], arr[j] = arr[j], arr[i]
    #             # i 之前的元素都小于基准数，所以 i 向右移动一位
    #             i += 1
    #     # 将基准节点放到正确位置上
    #     arr[i - 1], arr[low] = arr[low], arr[i - 1]
    #     # 返回基准数位置
    #     return i - 1

    # def quickSort(self, arr, low, high, k):
    #     size = len(arr)
    #     if low < high:
    #         # 按照基准位置，将序列划分为左右两个子序列
    #         pivot = self.randomPartition(arr, low, high)
    #         if pivot == size - k:
    #             return arr[size - k]
    #         if pivot > size - k:
    #             # 对左子序列递归进行快速排序
    #             self.quickSort(arr, low, pivot - 1, k)
    #         if pivot < size - k:
    #             # 对右子序列递归进行快速排序
    #             self.quickSort(arr, pivot + 1, high, k)
    #     return arr[size - k]

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return self.quickSort(nums, 0, len(nums) - 1, k)

    # 思路2：堆排序，
    # 这段代码的解题思路是使用最小堆来维护前k个最大值。具体步骤如下：
    # 1. 初始化一个空列表res，用于存储前k个最大值。
    # 2. 遍历输入的整数列表nums。
    # 3. 如果当前列表长度小于k，直接将元素加入列表并调整堆结构。
    # 4. 如果当前元素大于列表中最小值（堆顶元素），则弹出堆顶元素并将新元素加入堆中。
    # 5. 最后返回堆顶元素，即第k大的元素。
    # 时间复杂度：O(n log n)， 空间复杂度：O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for n in nums:
            if len((res)) < k:
                heapq.heappush(res, n)
            elif n > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, n)
        return heapq.heappop(res)

# @lc code=end

