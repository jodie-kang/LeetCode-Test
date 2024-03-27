#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
import random
# 各种排序方法参考：https://datawhalechina.github.io/leetcode-notes/#/keys/ch06-keys/06.01.02-Exercises-Key
class Solution:
    # 思路1：冒泡排序（超时）
    # 第 i (i = 1, 2, …) 趟排序时从序列中前 n - i + 1 个元素的第 1 个元素开始，相邻两个元素进行比较，如果前者大于后者，两者交换位置，否则不交换。
    # 时间复杂度：O(n^2)，空间复杂度：O(1)
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(n-i-1):
    #             if nums[j] > nums[j+1]:
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]
    #     return nums
    
    # 思路2：选择排序（超时）
    # 将序列分为两部分：前边 i - 1 个元素为已排序部分，后边 n - i + 1 个元素为未排序部分。
    # 第 i 趟排序从未排序部分 n − i + 1 (i = 1, 2, …, n − 1) 个元素中选择一个值最小的元素与未排序部分最前面那个元素交换位置，即与整个序列的第 i 个位置上的元素交换位置。
    # 如此下去，直到所有元素都变为已排序部分，排序结束。
    # 时间复杂度：O(n^2)，空间复杂度：O(1)
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     for i in range(n - 1):
    #         # 记录未排序部分中最小值的位置
    #         min_i  = i
    #         for j in range(i + 1, n):
    #             if nums[j] < nums[min_i]:
    #                 min_i = j
    #         # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
    #         if i != min_i:
    #             nums[i], nums[min_i] = nums[min_i], nums[i]
    #     return nums

    # 思路3：插入排序（超时）
    # 将整个序列分为两部分：前面 i 个元素为有序序列，后面 n - i 个元素为无序序列。
    # 每一次排序，将无序序列的第 1 个元素，在有序序列中找到相应的位置并插入。
    # 时间复杂度：O(n^2)，空间复杂度：O(1)
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     # 遍历无序序列
    #     for i in range(1, n):
    #         temp = nums[i]
    #         j = i
    #         # 从右至左遍历有序序列
    #         while j > 0 and nums[j - 1] > temp:
    #             # 将有序序列中插入位置右侧的元素依次右移一位
    #             nums[j] = nums[j - 1]
    #             j -= 1
    #         # 将该元素插入到适当位置
    #         nums[j] = temp
    #     return nums
    
    # 思路4：希尔排序（超时）
    # 将整个序列切按照一定的间隔取值划分为若干个子序列，每个子序列分别进行插入排序。
    # 然后逐渐缩小间隔进行下一轮划分子序列和对子序列进行插入排序。
    # 直至最后一轮排序间隔为 1，对整个序列进行插入排序，完成排序。
    # 时间复杂度：O(n log n) ~ O(n^2)，空间复杂度：O(1)
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     gap = n // 2
    #     # 按照 gap 分组
    #     while gap > 0:
    #         # 对每组元素进行插入排序
    #         for i in range(gap, n):
    #             # temp 为每组中无序序列第 1 个元素
    #             temp = nums[i]
    #             j = i
    #             # 从右至左遍历每组中的有序序列元素
    #             while j > 0 and nums[j-1] > temp:
    #                 # 将每组有序序列中插入位置右侧的元素依次在组中右移一位
    #                 nums[j] = nums[j-1]
    #                 j -= 1
    #             # 将该元素插入到适当位置
    #             nums[j] = temp
    #         # 缩小 gap 间隔
    #         gap = gap // 2
    #     return nums
    
    # 思路5：归并排序（通过）
    # 采用经典的分治策略，先递归地将当前序列平均分成两半。
    # 然后将有序序列两两合并，最终合并成一个有序序列。
    # 时间复杂度：O(n log n)，空间复杂度：O(1)
    def merge(self, left_arr, right_arr):
        arr = []
        left_i, right_i = 0, 0
        while left_i < len(left_arr) and right_i < len(right_arr):
            # 将两个有序子序列中较小元素依次插入到结果数组中
            if left_arr[left_i] < right_arr[right_i]:
                arr.append(left_arr[left_i])
                left_i += 1
            else:
                arr.append(right_arr[right_i])
                right_i += 1
        while left_i < len(left_arr):
            # 如果左子序列有剩余元素，则将其插入到结果数组中
            arr.append(left_arr[left_i])
            left_i += 1
            
        while right_i < len(right_arr):
            # 如果右子序列有剩余元素，则将其插入到结果数组中
            arr.append(right_arr[right_i])
            right_i += 1
        return arr    

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_arr = self.mergeSort(arr[0: mid])
        right_arr = self.mergeSort(arr[mid:])
        return self.merge(left_arr, right_arr)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    
    # 思路6：快速排序（通过）
    # 通过一趟排序将无序序列分为独立的两个序列，第一个序列的值均比第二个序列的值小。
    # 然后递归地排列两个子序列，以达到整个序列有序。
    # 时间复杂度：O(n log n)，空间复杂度：O(1)

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

    # def quickSort(self, arr, low, high):
    #     if low < high:
    #         # 按照基准数的位置，将序列划分为左右两个子序列
    #         pi = self.randomPartition(arr, low, high)
    #         # 对左右两个子序列分别进行递归快速排序
    #         self.quickSort(arr, low, pi - 1)
    #         self.quickSort(arr, pi + 1, high)

    #     return arr

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     return self.quickSort(nums, 0, len(nums) - 1)
    
    # # 思路7：堆排序（通过）
    # 借用「堆结构」所设计的排序算法。
    # 将数组转化为大顶堆，重复从大顶堆中取出数值最大的节点，并让剩余的堆结构继续维持大顶堆性质。
    # 时间复杂度：O(n log n)，空间复杂度：O(1)

    # 调整为大顶堆
    # def heapify(self, arr, index, end):
    #     left = index * 2 + 1
    #     right = left + 1
    #     while left <= end:
    #         # 当前节点为非叶子节点
    #         max_index = index
    #         if arr[left] > arr[max_index]:
    #             max_index = left
    #         if right <= end and arr[right] > arr[max_index]:
    #             max_index = right
    #         if index == max_index:
    #             # 如果不用交换，则说明已经交换结束
    #             break
    #         arr[index], arr[max_index] = arr[max_index], arr[index]
    #         # 继续调整子树
    #         index = max_index
    #         left = index * 2 + 1
    #         right = left + 1

    # # 初始化大顶堆
    # def buildMaxHeap(self, arr):
    #     size = len(arr)
    #     # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
    #     for i in range((size - 2) // 2, -1, -1):
    #         self.heapify(arr, i, size - 1)
    #     return arr

    # # 升序堆排序，思路如下：
    # # 1. 先建立大顶堆
    # # 2. 让堆顶最大元素与最后一个交换，然后调整第一个元素到倒数第二个元素，这一步获取最大值
    # # 3. 再交换堆顶元素与倒数第二个元素，然后调整第一个元素到倒数第三个元素，这一步获取第二大值
    # # 4. 以此类推，直到最后一个元素交换之后完毕。
    # def maxHeapSort(self, arr):
    #     self.buildMaxHeap(arr)
    #     size = len(arr)
    #     for i in range(size):
    #         arr[0], arr[size-i-1] = arr[size-i-1], arr[0]
    #         self.heapify(arr, 0, size-i-2)
    #     return arr

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     return self.maxHeapSort(nums)


    # # 思路8：计数排序（通过）
    # 使用一个额外的数组 counts，其中 counts[i] 表示原数组 arr 中值等于 i 的元素个数。
    # 然后根据数组 counts 来将 arr 中的元素排到正确的位置。
    # 时间复杂度：O(n + k)，空间复杂度：O(k)，其中 k 代表待排序序列的值域。
    # def countingSort(self, arr):
    #     # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
    #     arr_min, arr_max = min(arr), max(arr)
    #     # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
    #     size = arr_max - arr_min + 1
    #     counts = [0 for _ in range(size)]
        
    #     # 统计值为 num 的元素出现的次数
    #     for num in arr:
    #         counts[num - arr_min] += 1
        
    #     # 计算元素排名
    #     for j in range(1, size):
    #         counts[j] += counts[j - 1]

    #     # 反向填充目标数组
    #     res = [0 for _ in range(len(arr))]
    #     for i in range(len(arr) - 1, -1, -1):
    #         # 根据排名，将 arr[i] 放在数组对应位置
    #         res[counts[arr[i] - arr_min] - 1] = arr[i]
    #         # 将 arr[i] 的对应排名减 1
    #         counts[arr[i] - arr_min] -= 1

    #     return res

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     return self.countingSort(nums)

    
    # 思路9：桶排序（通过）
    # 将未排序数组分到若干个「桶」中，每个桶的元素再进行单独排序。
    # 时间复杂度：O(n)，空间复杂度：O(n + m)，m 为桶的个数
    # def insertionSort(self, arr):
    #     # 遍历无序序列
    #     for i in range(1, len(arr)):
    #         temp = arr[i]
    #         j = i
    #         # 从右至左遍历有序序列
    #         while j > 0 and arr[j - 1] > temp:
    #             # 将有序序列中插入位置右侧的元素依次右移一位
    #             arr[j] = arr[j - 1]
    #             j -= 1
    #         # 将该元素插入到适当位置
    #         arr[j] = temp

    #     return arr

    # def bucketSort(self, arr, bucket_size=5):
    #     # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
    #     arr_min, arr_max = min(arr), max(arr)
    #     # 定义桶的个数为 (最大值元素 - 最小值元素) // 每个桶的大小 + 1
    #     bucket_count = (arr_max - arr_min) // bucket_size + 1
    #     # 定义桶数组 buckets
    #     buckets = [[] for _ in range(bucket_count)]

    #     # 遍历原始数组元素，将每个元素装入对应区间的桶中
    #     for num in arr:
    #         buckets[(num - arr_min) // bucket_size].append(num)

    #     # 对每个桶内的元素单独排序，并合并到 res 数组中
    #     res = []
    #     for bucket in buckets:
    #         self.insertionSort(bucket)
    #         res.extend(bucket)

    #     return res

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     return self.bucketSort(nums)

# @lc code=end

