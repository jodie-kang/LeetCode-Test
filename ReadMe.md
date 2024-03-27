本项目主要参考了DataWhale的LeetCode算法笔记教程：[LeetCode 算法笔记 (datawhalechina.github.io)](https://datawhalechina.github.io/leetcode-notes/#/)

在此基础上，结合自己的理解，整理了一些高频题目的解题思路。

因个人能力有限，难免出现一些错误，欢迎大家批评指正。

传送门：

* [LeetCode 题解](https://datawhalechina.github.io/leetcode-notes/#/keys/solutions/Solutions-List?id=leetcode-%e9%a2%98%e8%a7%a3)
* [LeetCode 题库](https://leetcode.cn/problemset/)

# 数据结构

## 哈希表

| 题目                | 思路                                                                                                                  | 具体做法                                                                                                                                                                                                                                                                                                                                                                                      | 复杂度                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| 1.两数之和          | 哈希表中键值对信息为 `target-nums[i] ：i`，`i` 为下标                                                             | 1. 遍历数组，对于每一个数 `nums[i]`：<br />(1) 先查找字典中是否存在 `target - nums[i]`，存在则输出 `target - nums[i]` 对应的下标和当前数组的下标 `i`。<br />(2)不存在则在字典中存入 `target-nums[i]` 的下标 `i`                                                                                                                                                                   | O(n)，其中 n 是数组 `nums` 的元素数量 |
| 41.缺失的第一个正数 | 将当前数组视为哈希表。一个长度为 `n` 的数组，对应存储的元素值应该为 `[1, n + 1]` 之间，其中还包含一个缺失的元素。 | 1. 遍历一遍数组，将当前元素放到其对应位置上（比如元素值为 `1` 的元素放到数组第 `0` 个位置上、元素值为 `2` 的元素放到数组第 `1` 个位置上，等等）。<br />2. 再次遍历一遍数组。遇到第一个元素值不等于下标 + 1 的元素，就是答案要求的缺失的第一个正数。<br />3. 如果遍历完没有在数组中找到缺失的第一个正数，则缺失的第一个正数是 `n + 1`。<br />4. 最后返回我们找到的缺失的第一个正数。 | O(n)                                    |
| 128.最长连续序列    | 将数组存储到集合中进行去重，然后使用 `curr_streak` 维护当前连续序列长度，使用 `ans` 维护最长连续序列长度          | 1. 遍历集合中的元素，对每个元素进行判断，如果该元素不是序列的开始（即 `num - 1` 在集合中），则跳过。<br />2. 如果 `num - 1` 不在集合中，说明 `num` 是序列的开始，判断 `num + 1` 、`nums + 2`、`...` 是否在哈希表中，并不断更新当前连续序列长度 `curr_streak`。并在遍历结束之后更新最长序列的长度。<br />3. 最后输出最长序列长度。                                               | O(n)                                    |
| 169.多数元素        | 使用哈希表统计每个元素 `num` 出现的次数                                                                             | 1. 遍历数组 `nums`。<br />2. 对于当前元素 `num`，用哈希表统计每个元素 `num` 出现的次数。<br />3. 再遍历一遍哈希表，找出元素个数最多的元素即可                                                                                                                                                                                                                                           | O(n)                                    |

#### 缺失的第一个正数

```
def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 当 nums[i] 在范围内(1 到 size)，并且 nums[i] 不是 nums[nums[i] - 1] 时
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                index1 = i  # 当前元素的索引
                index2 = nums[i] - 1  # nums[i] 所指向的元素的索引
                # 交换 nums[i] 和 nums[nums[i] - 1] 的值
                nums[index1], nums[index2] = nums[index2], nums[index1]
        # 再次遍历数组，找到第一个不符合 nums[i] == i + 1 的情况
        for i in range(size):
            if nums[i] != i + 1:
                # 返回第一个缺失的正整数的索引加 1
                return i + 1
        # 如果所有正整数都存在，则返回 size + 1 作为第一个缺失的正整数
        return size + 1
```

#### 最长连续子序列

```
def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_streak += 1
                ans = max(ans, curr_streak)
        return ans
```

## 字符串

字符串的考点大多是模拟。

| 题目             | 思路                     | 具体做法                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 复杂度分析  |
| ---------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| 8.字符串转换整数 | 模拟                     | 1. 先去除前后空格。<br />2. 检测正负号。<br />3. 读入数字，并用字符串存储数字结果。<br />4. 将数字字符串转为整数，并根据正负号转换整数结果。<br />5. 判断整数范围，并返回最终结果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | O(n)        |
| 14.最长公共前缀  | 模拟                     | 1. 依次遍历所有字符串的每一列，比较相同位置上的字符是否相同。<br />(1)如果相同，则继续对下一列进行比较.<br />(2)如果不相同，则当前列字母不再属于公共前缀，直接返回当前列之前的部分。<br />2. 如果遍历结束，说明字符串数组中的所有字符串都相等，则可将字符串数组中的第一个字符串作为公共前缀进行返回。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | O(m*n)      |
| 415.字符串相加   | 使用字符串来模拟大数加法 | <br />加法的计算方式是：从个位数开始，由低位到高位，按位相加，如果相加之后超过 `10`，就需要向前进位。<br />1. 用一个数组存储按位相加后的结果，每一位对应一位数。<br />2. 然后分别使用一个指针变量，对两个数 `num1`、`num2` 字符串进行反向遍历，将相加后的各个位置上的结果保存在数组中，这样计算完成之后就得到了一个按位反向的结果<br />3. 最后返回结果的时候将数组反向转为字符串即可                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | O(max(m,n)) |
| 43.字符串相乘    | 使用数组来模拟大数乘法   | <br />长度为 `len(num1)` 的整数 `num1` 与长度为 `len(num2)` 的整数 `num2` 相乘的结果长度为 `len(num1) + len(num2) - 1` 或 `len(num1) + len(num2)`。所以我们可以使用长度为 `len(num1) + len(num2)` 的整数数组 `nums` 来存储两个整数相乘之后的结果。<br />1. 从个位数字由低位到高位开始遍历 `num1`，取得每一位数字 `digit1`。从个位数字由低位到高位开始遍历 `num2`，取得每一位数字 `digit2`。<br />2. 将 `digit1 * digit2` 的结果累积存储到 `nums` 对应位置 `i + j + 1` 上<br />3. 计算完毕之后从 `len(num1) + len(num2) - 1` 的位置由低位到高位遍历数组 `nums`。将每个数位上大于等于 `10` 的数字进行进位操作，然后对该位置上的数字进行取余操作<br />4. 最后判断首位是否有进位。如果首位为 `0`，则从第 `1` 个位置开始将答案数组拼接成字符串。如果首位不为 `0`，则从第 `0` 个位置开始将答案数组拼接成字符串。并返回答案字符串 | O(m*n)      |

#### 字符串相加代码

```
def addStrings(self, num1: str, num2: str) -> str:
        # 初始化结果字符串和进位
        result = []
        carry = 0

        # 遍历两个字符串，从最低位开始
        for i in range(max(len(num1), len(num2))):
            # 获取 num1 和 num2 的当前位的值（如果存在）
            digit1 = int(num1[-i-1]) if i < len(num1) else 0
            digit2 = int(num2[-i-1]) if i < len(num2) else 0

            # 计算当前位的和及进位
            total = digit1 + digit2 + carry
            # 更新进位
            carry = total // 10
            # 将当前位的和（模10）添加到结果列表
            result.append(str(total % 10))

        # 如果最后还有进位，添加到结果列表
        if carry:
            result.append(str(carry))

        # 由于我们是从低位到高位添加的，所以需要反转结果列表
        return ''.join(reversed(result))
```

#### 字符串相乘代码

```
def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
        len1, len2 = len(num1), len(num2)
        nums = [0 for _ in range(len1 + len2)]

        for i in range(len1-1, -1, -1):
            digit1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
                nums[i + j + 1] += digit1 * digit2
  
        for i in range(len1 + len2 -1, 0, -1):
            nums[i-1] += nums[i] // 10
            nums[i] %= 10
        if nums[0] == 0:
            ans = "".join(str(digit) for digit in nums[1:])
        else:
            ans = "".join(str(digit) for digit in nums[:])
        return ans
```

## 数组

| 题目                | 思路                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 复杂度                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 48.旋转图像         | 思路1：水平翻转 + 主对角线翻转<br />`matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]`<br />`matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`<br />思路2：主对角线翻转 + 每行翻转                                                                                                                                                                                                                                                                                                                                                                          | O(n^2)                    |
| 240.搜索二维矩阵II  | 矩阵是有序的，可以考虑使用二分查找                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | O(min(m,n) * (logm+logn)) |
| 33.搜索旋转排序数组 | 二分查找<br />`我们使用两个指针 left 和 right 来表示当前搜索范围的边界。在每次迭代中，我们首先检查 nums[mid] 是否等于 target。如果等于，我们找到了目标值并返回它的下标。如果不等于，我们需要确定 target 位于有序的左半部分还是右半部分。我们通过比较 nums[left] 和 nums[mid] 来判断左半部分是否有序。如果是有序的，并且 target 位于 nums[left] 和 nums[mid] 之间，我们将搜索范围移动到左半部分；否则，我们移动到右半部分。如果右半部分是有序的，我们对 target 进行类似的检查，但针对右半部分。如果 target 不在数组中，搜索范围最终会相交，循环结束，我们返回 -1 表示未找到目标值。` | O(logn)                   |
| 54.螺旋矩阵         | 模拟                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | O(m*n)                    |

#### 搜索二维矩阵II

```
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for i in range(len(matrix)):
            if binarySearch(matrix[i], target):
                return True
        return False
```

#### 搜索旋转排序数组

```
def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右半部分有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

#### 螺旋矩阵

```
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while True:
            # 从左到右: row=up，col=col+1
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
            # 从上到下：row=row+1，col=right
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            # 从右到左：row=down，col=col-1
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down:
                break
            # 从下到上：row=row-1，col=left
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res
```

## 链表

| 题目                           | 思路                                                                                                                                                    | 具体做法                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 复杂度                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 143.重排链表                   | 线性表                                                                                                                                                  | 因为链表无法像数组那样直接进行随机访问。所以我们可以先将链表转为线性表，然后直接按照提要要求的排列顺序访问对应数据元素，重新建立链表。                                                                                                                                                                                                                                                                                                                                  | O(n)                                             |
| 2.两数相加                     | 模拟大数加法，按位相加，将结果添加到新链表上。需要注意进位和对 10 取余基本操                                                                            | 1. 初始化一个哑节点dummy_head，它的下一个节点将是结果链表的第一个有效节点。<br />2. 使用一个while循环来遍历两个输入链表，同时处理进位。在每次迭代中，计算两个链表当前节点的值之和，并加上之前的进位。<br />3. 更新进位，并创建一个新的链表节点来存储个位数的和。<br />4. 如果还有剩余的进位，添加一个新的节点到结果链表中。<br />5. 返回哑节点的下一个节点，即结果链表的头节点。                                                                                        | 时间复杂度：O(max(M, N))，<br />空间复杂度：O(1) |
| 24.两两交换链表中的节点        | 迭代                                                                                                                                                    | 1. 创建一个哑节点 `new_head`，令 `new_head.next = head`。<br />2. 遍历链表，并判断当前链表后两位节点是否为空。如果后两个节点不为空，则使用三个指针：`curr` 指向当前节点，`node1` 指向下一个节点，`node2` 指向下面第二个节点。<br />3. 将 `curr` 指向 `node2`，`node1` 指向 `node2` 后边的节点，`node2` 指向 `node1`。则节点关系由 `curr → node1 → node2` 变为了 `curr → node2 → node1`。<br />4. 依次类推，最终返回哑节点连接的后一个节点 | O(n),其中 n 为链表的节点数量。                   |
| 82.删除排序链表中的重复元素-ii | 基本操作                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | O(n)                                             |
| 141.环形链表                   | 快慢指针                                                                                                                                                | 这种方法类似于在操场跑道跑步。两个人从同一位置同时出发，如果跑道有环（环形跑道），那么快的一方总能追上慢的一方。<br />1.用两个指针，一个慢指针（龟）每次前进一步，快指针（兔）指针每次前进两步（两步或多步效果是等价的）。<br />2.如果两个指针在链表头节点以外的某一节点相遇（即相等）了，那么说明链表有环。<br />3.否则，如果（快指针）到达了某个没有后继指针的节点时，那么说明没环                                                                                    | O(n)                                             |
| 142.环形链表II                 | 快慢指针                                                                                                                                                | 同上<br />4. 如果有环，则再定义一个指针 `ans`，和慢指针一起每次移动一步，两个指针相遇的位置即为入口节点。                                                                                                                                                                                                                                                                                                                                                             | O(n)                                             |
| 234.回文链表                   | 数组                                                                                                                                                    | 1. 利用数组，将链表元素依次存入。<br />2. 判断 正序和逆序是否相等 nodes==nodes[::-1]                                                                                                                                                                                                                                                                                                                                                                                    | O(n)                                             |
| 206.反转链表                   | 递归 、迭代                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | O(n)                                             |
| 92.反转链表II                  | 迭代                                                                                                                                                    | 这道题要求对链表的部分区间进行反转。我们可以先遍历到需要反转的链表区间的前一个节点，然后对需要反转的链表区间进行迭代反转。最后再返回头节点即可.<br />如果需要反转的区间包含了链表的第一个节点，那么我们可以事先创建一个哑节点作为链表初始位置开始遍历，这样就能避免找不到需要反转的链表区间的前一个节点。                                                                                                                                                               | O(n)                                             |
| 25.k个一组翻转链表             | 迭代                                                                                                                                                    | 以 `k` 为单位对链表进行切分，然后分别对每个区间部分进行反转。最后再返回头节点即可。                                                                                                                                                                                                                                                                                                                                                                                   | O(n)                                             |
| 160.相交链表                   | 如果两个链表相交，那么从相交位置开始，到结束，必有一段等长且相同的节点。假设链表 `listA` 的长度为 m、链表 `listB` 的长度为 n，他们的相交序列有 k 个 | 1. 将链表 `listA` 的末尾拼接上链表 `listB`，链表 `listB` 的末尾拼接上链表 `listA`。<br />2. 使用两个指针 `pA` 、`pB`，分别从链表 `listA`、链表 `listB` 的头节点开始遍历，如果走到共同的节点，则返回该节点。<br />3. 否则走到两个链表末尾，返回 `None`                                                                                                                                                                                                 | O(m+n)                                           |

#### 两数相加

```
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化结果链表的头节点和当前节点
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0  # 进位变量

        # 遍历两个链表直到其中一个遍历完毕
        while l1 or l2:
            # 计算两个链表当前节点的值，或者0如果已经遍历完毕
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 计算总和和进位
            total = val1 + val2 + carry
            carry = total // 10  # 更新进位
            # 创建新节点，值为个位数总和
            current.next = ListNode(total % 10)
            # 移动当前节点到下一个位置
            current = current.next

            # 移动链表l1和l2的指针
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 如果最后还有进位，添加一个新节点
        if carry > 0:
            current.next = ListNode(carry)

        # 返回结果链表的头节点的下一个节点，因为dummy_head是一个哑节点
        return dummy_head.next
```

#### 反转链表

```
class Solution:
    # 思路 1：迭代
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
    # 思路 2：递归
    # 时间复杂度：O(n)，空间复杂度：O(n)
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None or head.next == None:
    #         return head
    #     new_head = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return new_head
```

#### 反转链表II

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        index = 1
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre = dummy_head

        reverse_start = dummy_head
        while reverse_start.next and index < left:
            reverse_start = reverse_start.next
            index += 1

        pre = reverse_start
        cur = pre.next
        while cur and index <= right:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            index += 1

        reverse_start.next.next = cur
        reverse_start.next = pre
  
        return dummy_head.next
```

#### K 个一组反转链表

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        pre = head
        cur = pre.next
        first = cur
        while cur != tail:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head.next = pre
        first.next = tail
        return first

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        tail = dummy_head.next
        index = 0
        while tail:
            index += 1
            if index % k == 0:
                cur = self.reverse(cur, tail.next)
                tail = cur.next
            else:
                tail = tail.next
        return dummy_head.next
```

#### 两两交换链表中的节点

```
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            node1.next = node2.next
            node2.next = node1
            cur = node1
        return dummy_head.next
```

#### 环形链表II

```
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        ans = head
        while ans != slow:
            ans, slow = ans.next, slow.next
        return ans
```

#### 删除链表中的重复元素II

```
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个哨兵节点，其 next 指针指向原始链表的头节点
        dummy_head = ListNode(-1)
        dummy_head.next = head
        cur = dummy_head        # 使用 cur 指针遍历链表
        # 当 cur 指针和 cur 的下一个节点的下一个节点都存在时，继续循环
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:   # 如果 cur 指针指向的节点和它的下一个节点的值相同
                temp = cur.next                     # 将 temp 指针指向 cur 的下一个节点
                while temp and temp.next and temp.val == temp.next.val: # 遍历连续的重复节点
                    temp = temp.next
                cur.next = temp.next                        # 跳过连续的重复节点，将 cur 的下一个节点指向最后一个非重复节点的下一个节点
            else:
                cur = cur.next
        return dummy_head.next  # 返回哨兵节点的下一个节点，即新链表的头节点
```

#### 相交链表

```
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA
        return pA
```

## 栈和队列

**单调栈（Monotone Stack）** ：一种特殊的栈。在栈的「先进后出」规则基础上，要求「从 **栈顶** 到 **栈底** 的元素是单调递增（或者单调递减）」。其中满足从栈顶到栈底的元素是单调递增的栈，叫做「单调递增栈」。满足从栈顶到栈底的元素是单调递减的栈，叫做「单调递减栈」。注意：这里定义的顺序是从「栈顶」到「栈底」。有的文章里是反过来的。

单调栈可以在时间复杂度为 O(n) 的情况下，求解出某个元素左边或者右边第一个比它大或者小的元素。

所以单调栈一般用于解决一下几种问题：

* 寻找左侧第一个比当前元素大的元素。
* 寻找左侧第一个比当前元素小的元素。
* 寻找右侧第一个比当前元素大的元素。
* 寻找右侧第一个比当前元素小的元素。

简单记为以下几条规则：

1. 无论哪种题型，都建议从左到右遍历元素。
2. 查找**「比当前元素大的元素」** 就用**单调递增栈** ，查找**「比当前元素小的元素」** 就用**单调递减栈** 。
3. 从**「左侧」** 查找就看**「插入栈」** 时的栈顶元素，从**「右侧」** 查找就看**「弹出栈」** 时即将插入的元素

#### 单调递增栈模板

```
def monotoneIncreasingStack(nums):
    stack = []
    for num in nums:
        while stack and num >= stack[-1]:
            stack.pop()
        stack.append(num)
```

#### 单调递减栈模板

```
def monotoneDecreasingStack(nums):
    stack = []
    for num in nums:
        while stack and num <= stack[-1]:
            stack.pop()
        stack.append(num)
```

### 优先队列

> **优先队列（Priority Queue）** ：一种特殊的队列。在优先队列中，元素被赋予优先级，当访问队列元素时，具有最高优先级的元素最先删除。

优先队列与普通队列最大的不同点在于 **出队顺序** 。

* 普通队列的出队顺序跟入队顺序相关，符合「先进先出（First in, First out）」的规则。
* 优先队列的出队顺序跟入队顺序无关，优先队列是按照元素的优先级来决定出队顺序的。优先级高的元素优先出队，优先级低的元素后出队。优先队列符合**「最高级先出（First in, Largest out）」** 的规则。

Python 中可以通过 `heapq` 来实现优先队列。

* 将数组构建为二叉堆`heapify(nums)`
* 入队操作`heappush()`
* 出队操作`heappop()`
  需要注意的是：heapq.heappop() 函数总是返回「最小的」的元素。所以我们在使用 heapq.heappush() 时，将优先级设置为负数，这样就使得元素可以按照优先级从高到低排序， 这个跟普通的按优先级从低到高排序的堆排序恰巧相反。这样做的目的是为了 heapq.heappop() 每次弹出的元素都是优先级最高的元素。

```
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]
```

| 题目                      | 思路                                                                                                                                                                                                                              | 具体做法                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 复杂度分析             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| 20.有效的括号             | 借助一个栈来模拟左括号和右括号。检测最后栈是否为空。                                                                                                                                                                              | 1. 先判断一下字符串的长度是否为偶数。因为括号是成对出现的，所以字符串的长度应为偶数，可以直接判断长度为奇数的字符串不匹配。如果字符串长度为奇数，则说明字符串中的括号不匹配，直接返回False<br />2. 使用栈 stack 来保存未匹配的左括号。然后依次遍历字符串 s 中的每一个字符。左括号入栈，右括号先看栈顶元素是否是与当前右括号相同类型的左括号。如果有，则令其出栈，继续遍历。否则直接返回False。<br />3. 遍历结束之后，再判断一下栈是否为空。如果栈为空，则说明字符串中的括号匹配，返回True。否则返回False。                                                                                                                        | O(n)                   |
| 946.验证栈序列            | 借助一个栈来模拟压入、压出的操作。检测最后栈是否为空                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | O(n)                   |
| 227.基本计算器-ii         | 使用一个栈来保存进行乘除运算后的整数值。正整数直接压入栈中，负整数，则将对应整数取负号，再压入栈中。这样最终计算结果就是栈中所有元素的和                                                                                          | 1. 遍历字符串 `s`，使用变量 `op` 来标记数字之前的运算符，默认为 `+`<br />2. 如果遇到数字，继续向后遍历，将数字进行累积，得到完整的整数 num。判断当前 op 的符号。<br />（1）如果 `op` 为 `+`，则将 `num` 压入栈中<br />（2）如果 `op` 为 `-`，则将 `-num` 压入栈中<br />（3）如果 `op` 为 `*`，则将栈顶元素 `top` 取出，计算 `top * num`，并将计算结果压入栈中<br />（4）如果 `op` 为 `/`，则将栈顶元素 `top` 取出，计算 `int(top / num)`，并将计算结果压入栈中<br />3. 如果遇到 `+`、`-`、`*`、`/` 操作符，则更新 `op`<br />4. 最后将栈中整数进行累加，并返回结果                     | O(n)                   |
| 496.下一个更大元素I       | 因为 `nums1` 是 `nums2` 的子集，所以我们可以先遍历一遍 `nums2`，并构造单调递增栈，求出 `nums2` 中每个元素右侧下一个更大的元素。然后将其存储到哈希表中。然后再遍历一遍 `nums1`，从哈希表中取出对应结果，存放到答案数组中 | 1. 使用数组 `res` 存放答案。使用 `stack` 表示单调递增栈。使用哈希表 `num_map` 用于存储 `nums2` 中下一个比当前元素大的数值，映射关系为 `当前元素值：下一个比当前元素大的数值`<br />2. 遍历数组 `nums2`，对于当前元素：<br />（1）如果当前元素值较小，则直接让当前元素值入栈。<br />（2）如果当前元素值较大，则一直出栈，直到当前元素值小于栈顶元素。出栈时，第一个大于栈顶元素值的元素，就是当前元素。则将其映射到 `num_map` 中<br />3. 遍历完数组 `nums2`，建立好所有元素下一个更大元素的映射关系之后，再遍历数组 `nums1`<br />4. 从 `num_map` 中取出对应的值，将其加入到答案数组中。最终输出答案数组 `res` | O(n)                   |
| 42.接雨水                 | 单调递增栈                                                                                                                                                                                                                        | 1. 遍历高度数组 `height`<br />2. 如果当前柱体高度较小，小于等于栈顶柱体的高度，则将当前柱子高度入栈。如果当前柱体高度较大，大于栈顶柱体的高度，则一直出栈，直到当前柱体小于等于栈顶柱体的高度<br />~~~~                                                                                                                                                                                                                                                                                                                                                                                                                         | O(n)                   |
| 232.用栈实现队列          | 使用两个栈，inStack 用于输入，outStack 用于输出                                                                                                                                                                                   | `push` 操作：将元素压入 `inStack` 中。<br />`pop` 操作：如果 `outStack` 输出栈为空，将 `inStack` 输入栈元素依次取出，按顺序压入 `outStack` 栈。这样 `outStack` 栈的元素顺序和之前 `inStack` 元素顺序相反，`outStack` 顶层元素就是要取出的队头元素，将其移出，并返回该元素。如果 `outStack` 输出栈不为空，则直接取出顶层元素。 操作：和 `pop` 操作类似，只不过最后一步不需要取出顶层元素，直接将其返回即可。 操作：如果 `inStack` 和 `outStack` 都为空，则队列为空，否则队列不为空                                                                                                                       | O(1)                   |
| 394.字符串解码            | 使用两个栈 `stack1`、`stack2`。`stack1` 用来保存左括号前已经解码的字符串，`stack2` 用来存储左括号前的数字                                                                                                                 | 1. 用 `res` 存储待解码的字符串、`num` 存储当前数字<br />2. 遍历字符串: <br />(1) 如果遇到数字，则累加数字到 `num.`<br />(2) 如果遇到左括号，将当前待解码字符串入栈 `stack1`，当前数字入栈 `stack2`，然后将 `res`、`nums` 清空<br />(3) 如果遇到右括号，则从 `stack1` 的取出待解码字符串 `res`，从 `stack2` 中取出当前数字 `num`，将其解码拼合成字符串赋值给 `res`<br />(4) 如果遇到其他情况（遇到字母），则将当前字母加入 `res` 中<br />3. 遍历完输出解码之后的字符串 `res`                                                                                                                           | O(n)                   |
| 225.用队列实现栈          | 使用两个队列，pushQueue 用作入栈，popQueue 用作出栈                                                                                                                                                                               | `push` 操作：将新加入的元素压入 `pushQueue` 队列中，并且将之前保存在 `popQueue` 队列中的元素从队头开始依次压入 `pushQueue` 中，此时 `pushQueue` 队列中头节点存放的是新加入的元素，尾部存放的是之前的元素。 而 `popQueue` 则为空。再将 `pushQueue` 和 `popQueue` 相互交换，保持 `pushQueue` 为空，`popQueue` 则用于 `pop`、`top` 等操作。<br />`pop` 操作：直接将 `popQueue` 队头元素取出。 操作：返回 `popQueue` 队头元素。 <br />`empty`：判断 `popQueue` 是否为空                                                                                                                             | 入栈：O(n)，其他为O(1) |
| 215.数组中的第K个最大元素 | 优先队列，使用最小堆来维护前k个最大值                                                                                                                                                                                             | 1. 遍历数组元素，对于挡圈元素 num:<br />(1) 如果优先队列中的元素个数小于 k 个，则将当前元素 num 放入优先队列中<br />(2) 如果优先队列中的元素个数大于等于 k 个，并且当前元素 num 大于优先队列的队头元素，则弹出队头元素，并将当前元素 num 插入到优先队列中<br />2. 遍历完，此时优先队列的队头元素就是第 k 个最大元素，将其弹出并返回即可                                                                                                                                                                                                                                                                                           | O(n log k)             |

#### 数组中的第K个最大元素——代码

```
def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for n in nums:
            if len((res)) < k:
                heapq.heappush(res, n)
            elif n > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, n)
        return heapq.heappop(res)
```

#### 验证栈序列代码

```
def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for item in pushed:
            stack.append(item)
            while (stack and stack[-1] == popped[index]):
                stack.pop()
                index += 1
        return len(stack) == 0
```

#### 基本计算器II代码

```
def calculate(self, s: str) -> int:
        size = len(s)
        stack = []
        op = '+'
        index = 0
        while index < size:
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                # num = ord(s[index]) - ord('0')
                num = int(s[index])
                while index + 1 < size and s[index + 1].isdigit():
                    index += 1
                    num = 10 * num + ord(s[index]) - ord('0')
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))
            elif s[index] in "+-*/":
                op = s[index]
            index += 1
        return sum(stack)
```

#### 下一个更大元素I代码

```
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num_map = {}
        res = []
        for num in nums2:
            while stack and num > stack[-1]:
                num_map[stack[-1]] = num
                stack.pop()
            stack.append(num)

        for num in nums1:
            res.append(num_map.get(num, -1))
        return res
```

#### 接雨水代码

```
def trap(self, height: List[int]) -> int:
        ans = 0  # 初始化雨水总量为 0
        stack = []  # 初始化栈，用于存储索引
        size = len(height)  # 获取数组的长度

        # 遍历数组的每个元素
        for i in range(size):
            # 当栈不为空且当前高度大于栈顶高度时，处理栈顶元素
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop(-1)  # 弹出栈顶元素的索引
                # 如果栈不为空，说明当前位置左边存在一个更高的柱子
                if stack:
                    left = stack[-1] + 1  # 当前位置左边的柱子索引
                    right = i - 1  # 当前位置右边的柱子索引
                    high = min(height[i], height[stack[-1]]) - height[cur]  # 计算雨水高度
                    ans += high * (right - left + 1)  # 累加雨水总量
                else:
                    # 如果栈为空，说明当前位置是左边的最高点，跳出循环
                    break
            # 将当前索引压入栈中
            stack.append(i)
        # 返回计算的雨水总量
        return ans
```

#### 字符串解码-代码

```
def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack1.append(res)
                stack2.append(num)
                res = ""
                num = 0
            elif ch == ']':
                cur_res = stack1.pop()
                cur_num = stack2.pop()
                res = cur_res + res * cur_num
            else:
                res += ch
        return res
```

## 二叉树

| 题目                               | col2                                                              | col3 |
| ---------------------------------- | ----------------------------------------------------------------- | ---- |
| 104.二叉树的最大深度               | 递归                                                              |      |
| 144.二叉树的前序遍历               |                                                                   |      |
| 94.二叉树的中序遍历                |                                                                   |      |
| 98.验证二叉搜索树                  |                                                                   |      |
| 101.对称二叉树                     |                                                                   |      |
| 102.二叉树的层序遍历               | 宽度优先搜索                                                      |      |
| 103.二叉树的锯齿形层序遍历         | 宽度优先搜索，level合并到order时，逆序：order.append(level[::-1]) |      |
| 105.从前序与中序遍历序列构造二叉树 |                                                                   |      |
| 110.平衡二叉树                     |                                                                   |      |
| 226.翻转二叉树                     |                                                                   |      |
| 236.二叉树的最近公共祖先           |                                                                   |      |
| 199.二叉树的右视图                 |                                                                   |      |
| 297.二叉树的序列化与反序列化       |                                                                   |      |
| 958.二叉树的完全性检验             |                                                                   |      |

# 算法

## 双指针

双指针分为「对撞指针」、「快慢指针」、「分离双指针」。

* **对撞指针** ：两个指针方向相反。适合解决查找有序数组中满足某些约束条件的一组元素问题、字符串反转问题。
* **快慢指针** ：两个指针方向相同。适合解决数组中的移动、删除元素问题，或者链表中的判断是否有环、长度问题。
* **分离双指针** ：两个指针分别属于不同的数组 / 链表。适合解决有序数组合并，求交集、并集问题。

#### 对撞指针伪代码模板

```
left, right = 0, len(nums) - 1

while left < right:
    if 满足要求的特殊条件:
        return 符合条件的值 
    elif 一定条件 1:
        left += 1
    elif 一定条件 2:
        right -= 1

return 没找到 或 找到对应值
```

#### 快慢指针伪代码模板

```
slow = 0
fast = 1
while 没有遍历完：
    if 满足要求的特殊条件:
        slow += 1
    fast += 1
return 合适的值
```

#### 分离双指针伪代码模板

```
left_1 = 0
left_2 = 0

while left_1 < len(nums1) and left_2 < len(nums2):
    if 一定条件 1:
        left_1 += 1
        left_2 += 1
    elif 一定条件 2:
        left_1 += 1
    elif 一定条件 3:
        left_2 += 1
```

| 题目                       | 方法     | 思路                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 复杂度分析 |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 15.三数之和                | 对撞指针 | 先将数组进行排序，以保证按顺序查找 a、b、c 时，元素值为升序，从而保证所找到的三个元素是不重复的。第一重循环遍历 a，对于每个 a 元素，从 a 元素的下一个位置开始，使用对撞指针 left，right。left 指向 a 元素的下一个位置，right 指向末尾位置。先将 left 右移、right 左移去除重复元素，再进行下边的判断。                                                                                                                                                                                                                     | O(n^2)     |
| 33.搜索旋转排序数组        | 对撞指针 | 使用两个指针 left 和 right 来表示当前搜索范围的边界。在每次迭代中，首先检查 nums[mid] 是否等于 target。如果等于，找到目标值并返回它的下标。如果不等于，确定 target 位于有序的左半部分还是右半部分。通过比较 nums[left] 和 nums[mid] 来判断左半部分是否有序。如果是有序的，并且 target 位于 nums[left] 和 nums[mid] 之间，将搜索范围移动到左半部分；否则，移动到右半部分。如果右半部分是有序的，对 target 进行类似的检查，但针对右半部分。如果 target 不在数组中，搜索范围最终会相交，循环结束，返回 -1 表示未找到目标值。 | O(logn)    |
| 88.合并两个有序数组        | 快慢指针 | 将两个指针 index1、index2 分别指向 nums1、nums2 数组的尾部，再用一个指针 index 指向数组 nums1 的尾部。<br />从后向前判断当前指针下 nums1[index1] 和 nums[index2] 的值大小，将较大值存入 num1[index] 中，然后继续向前遍历。<br />最后再将 nums2 中剩余元素赋值到 num1 前面对应位置上。                                                                                                                                                                                                                                     | O(m+n)     |
| 283.移动零                 | 快慢指针 | 使用两个指针 slow，fast。slow 指向处理好的非 0 数字数组的尾部，fast 指针指向当前待处理元素。不断向右移动 fast 指针，每次移动到非零数，则将左右指针对应的数交换，交换同时将 slow 右移。此时，slow 指针左侧均为处理好的非零数，而从 slow 指针指向的位置开始， fast 指针左边为止都为 0。遍历结束之后，则所有 0 都移动到了右侧，且保持了非零数的相对位置                                                                                                                                                                      | O(n)       |
| 19.删除链表的倒数第n个结点 | 快慢指针 | 快指针先走 n 步，然后快慢指针、慢指针再同时走，每次一步，这样等快指针遍历到链表尾部的时候，慢指针就刚好遍历到了倒数第 n 个节点位置。将该位置上的节点删除即可。<br />需要注意的是要删除的节点可能包含了头节点。我们可以考虑在遍历之前，新建一个头节点，让其指向原来的头节点。这样，最终如果删除的是头节点，则删除原头节点即可。返回结果的时候，可以直接返回新建头节点的下一位节点。                                                                                                                                        | O(n)       |
|                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |            |
|                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |            |
|                            |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |            |

#### 三数之和代码

```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        ans = []
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = size - 1
            while left < right:
                while left < right and left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                while left < right and right < size - 1 and nums[right+1] == nums[right]:
                    right -= 1
                if left < right and nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans
```

#### 合并两个有序数组代码

```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        index = m + n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] < nums2[index2]:
                nums1[index] = nums2[index2]
                index2 -= 1
            else:
                nums1[index] = nums1[index1]
                index1 -= 1
            index -= 1

        nums1[:index2+1] = nums2[:index2+1]
```

#### 搜索旋转排序数组代码

```
def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右半部分有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

#### 删除链表倒数第 N 个节点

```
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow, fast = dummy_head, head
        while n:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
```

## 查找和排序

| 题目                                          | 思路                                                               | 具体做法                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 复杂度分析    |
| --------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| 4.寻找两个正序数组的中位数                    | 二分查找                                                           | `通过交换数组，确保在较短的数组上进行二分查找。使用二分查找确定较短数组的分割位置，使得两个数组的左半部分和右半部分元素个数相等或左半部分多一个。根据两个数组的总元素个数是奇数还是偶数，计算中位数。`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | O(log(m+n))   |
| 148.排序链表                                  | 归并排序                                                           | 1.**分割环节** ：找到链表中心链节点，从中心节点将链表断开，并递归进行分割.<br />(1)使用快慢指针 `fast = head.next`、`slow = head`，让 `fast` 每次移动 `2` 步，`slow` 移动 `1` 步，移动到链表末尾，从而找到链表中心链节点，即 `slow`。<br />(2)从中心位置将链表从中心位置分为左右两个链表 `left_head` 和 `right_head`，并从中心位置将其断开，即 `slow.next = None`。<br />(3)对左右两个链表分别进行递归分割，直到每个链表中只包含一个链节点<br />2. **归并环节** ：将递归后的链表进行两两归并，完成一遍后每个子链表长度加倍。重复进行归并操作，直到得到完整的链表.<br />(1)使用哑节点 `dummy_head` 构造一个头节点，并使用 `cur` 指向 `dummy_head` 用于遍历。(2)比较两个链表头节点 `left` 和 `right` 的值大小。将较小的头节点加入到合并后的链表中。并向后移动该链表的头节点指针。(3)然后重复上一步操作，直到两个链表中出现链表为空的情况。(4)将剩余链表插入到合并中的链表中。(5)将哑节点 `dummy_dead` 的下一个链节点 `dummy_head.next` 作为合并后的头节点返回 | O(n*logn)     |
| 21.合并两个有序链表                           | 归并排序，分治法                                                   | 1.使用哑节点 `dummy_head` 构造一个头节点，并使用 `curr` 指向 `dummy_head` 用于遍历。<br />2.然后判断 `list1` 和 `list2` 头节点的值，将较小的头节点加入到合并后的链表中。并向后移动该链表的头节点指针。<br />3.然后重复上一步操作，直到两个链表中出现链表为空的情况。<br />4.将剩余链表链接到合并后的链表中。<br />5.将哑节点 `dummy_dead` 的下一个链节点 `dummy_head.next` 作为合并后有序链表的头节点返回。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | O(n)          |
| 23.合并 k 个升序链表                          | 将链表数组不断二分，转为规模为二分之一的子问题，然后再进行归并排序 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | O(k*n*logk) |
| 56.合并区间                                   | 排序                                                               | 1.设定一个数组 `ans` 用于表示最终不重叠的区间数组，然后对原始区间先按照区间左端点大小从小到大进行排序。<br />2.遍历所有区间，先将第一个区间加入 `ans` 数组中，然后依次考虑后边的区间：<br />（1）如果第 `i` 个区间左端点在前一个区间右端点右侧，则这两个区间不会重合，直接将该区间加入 `ans` 数组中。<br />（2）否则，这两个区间重合，判断一下两个区间的右区间值，更新前一个区间的右区间值为较大值，然后继续考虑下一个区间，以此类推。<br />3.最后返回数组 `ans`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | O(nlogn)      |
| 34.在排序数组中查找元素的第一个和最后一个位置 | 进行两次二分查找，第一次尽量向左搜索。第二次尽量向右搜索           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | O(log n)      |


#### 寻找两个正序数组的中位数

```
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2) 
        if n1 > n2:  # 如果 nums1 较长，交换两个数组
            return self.findMedianSortedArrays(nums2, nums1)

        # 计算中位数的索引
        k = (n1 + n2 + 1) // 2
        left = 0  # 定义 nums1 的左边界
        right = n1  # 定义 nums1 的右边界

        # 二分查找 nums1 中的分割位置
        while left < right:
            m1 = left + (right - left) // 2  # 在 nums1 中取前 m1 个元素的索引
            m2 = k - m1  # 在 nums2 中取前 m2 个元素的索引

            # 检查 nums1 中的 m1 元素是否应该与 nums2 中的 m2 元素配对
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1  # 如果 nums1 中的元素不够多，更新左边界
            else:
                right = m1  # 否则，更新右边界

        # 确定 nums1 的分割位置
        m1 = left
        # 确定 nums2 的分割位置
        m2 = k - m1

        # 计算中位数的左侧边界值
        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1],
                    float('-inf') if m2 <= 0 else nums2[m2 - 1])

        # 如果总元素个数是奇数，中位数是左侧边界值
        if (n1 + n2) % 2 == 1:
            return c1

        # 计算中位数的右侧边界值
        c2 = min(float('inf') if m1 >= n1 else nums1[m1],
                    float('inf') if m2 >= n2 else nums2[m2])

        # 如果总元素个数是偶数，中位数是两个边界值的平均
        return (c1 + c2) / 2
```

#### 排序链表

```
def merge(self, left, right):
        # 归并环节
        dummy_head = ListNode(-1)
        cur = dummy_head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left if left else right
    
        return dummy_head.next
  
    def mergeSort(self, head: ListNode):
        # 分割环节
        if not head or not head.next:
            return head
  
        # 快慢指针找到中心链节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
  
        # 断开左右链节点
        left_head, right_head = head, slow.next 
        slow.next = None
  
        # 归并操作
        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
```

#### 合并两个有序链表

```
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        cur = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 is not None else list2
        return dummy_head.next
```

#### 合并 K 个有序链表

```
# 思路：分而治之的思想。将链表数组不断二分，转为规模为二分之一的子问题，然后再进行归并排序。
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        size = len(lists)
        return self.mergeSort(lists, 0, size-1)
    # 二分环节，将链表数组不断二分，转为规模为二分之一的子问题
    def mergeSort(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        node_left = self.mergeSort(lists, left, mid)
        node_right = self.mergeSort(lists, mid+1, right)
        return self.merge(node_left, node_right)
    # 归并环节
    def merge(self, left, right):
        dummy_head = ListNode(-1)
        cur = dummy_head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left if left else right
        return dummy_head.next
```

#### 在排序数组中查找元素的第一个和最后一个位置

```
def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_leftmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
  
        def find_rightmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
  
        left_index = find_leftmost(nums, target)
        right_index = find_rightmost(nums, target)
        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]
```


## 滑动窗口

### 固定长度模板

```
left = 0
right = 0

while right < len(nums):
    window.append(nums[right])
  
    # 超过窗口大小时，缩小窗口，维护窗口中始终为 window_size 的长度
    if right - left + 1 >= window_size:
        # ... 维护答案
        window.popleft()
        left += 1
  
    # 向右侧增大窗口
    right += 1
```

### 不定长度模板

* 求解最大的满足条件的窗口
* 求解最小的满足条件的窗口

```
left = 0
right = 0

while right < len(nums):
    window.append(nums[right])
  
    while 窗口需要缩小:
        # ... 可维护答案
        window.popleft()
        left += 1
  
    # 向右侧增大窗口
    right += 1
```

| 题目                   | 方法               | 滑动窗口                                                                                                                                                                       | 缩小窗口条件                                                                                                                                                           | 复杂度分析                                                                                                                                 |
| ---------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 3.无重复字符的最长子串 | 不定长度的滑动窗口 | `window 为哈希表类型`，记录 `不重复的字符个数。`<br />一开始，left、right 都指向 0。                                                                                       | 当窗口中字符的频率大于1时，移动左指针,直到窗口中没有重复的字符                                                                                                         | O(n)                                                                                                                                       |
| 209.长度最小的子数组   | 不定长度的滑动窗口 | window为整数类型，记录连续子数组的和。<br />`设定两个指针：left、right，分别指向滑动窗口的左右边界，保证窗口中的和刚好大于等于 target。`<br />一开始，left、right 都指向 0。 | `如果 window_sum >= target，则不断右移 left，缩小滑动窗口长度，并更新窗口和的最小值，直到 window_sum < target`                                                       | O(n)                                                                                                                                       |
| 239.滑动窗口最大值     | 固定长度的滑动窗口 | 利用优先队列来存储窗口中的所有元素，以及对应的索引。因为Python的 `heapq`库默认实现的是最小堆，所以通过将元素取负，可以使得堆顶元素实际上是窗口中的最大值。                   | 在每次迭代中，检查堆顶元素的索引是否仍然在当前窗口范围内（即堆顶元素的索引大于当前元素索引减去 `k`）。如果不在，则循环地从堆中移除堆顶元素，直到堆顶元素的索引有效。 | `O(n * log(k))`，其中 `n`是数组 `nums`的长度。这是因为对每个元素，插入和删除堆的操作需要 `O(log(k))`时间，而整个数组需要遍历一次。 |

### 无重复字符的最长子串代码

```
def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()
        left, right = 0, 0
        ans = 0
        # 遍历字符串
        while right < len(s):
            # 当前字符不在窗口中，将其加入字典，并设置频率为1
            if s[right] not in window:
                window[s[right]] = 1
            else:
                # 当前字符已在窗口中，增加该字符的频率
                window[s[right]] += 1
  
            # 当窗口中字符的频率大于1时，移动左指针,直到窗口中没有重复的字符
            while window[s[right]] > 1:
                window[s[left]] -= 1  # 减少左指针对应的字符频率
                left += 1  # 移动左指针

            # 更新最长子串的长度
            ans = max(ans, right-left+1)
  
            # 移动右指针，向右扩展窗口
            right += 1
        return ans
```

### 滑动窗口最大值代码

```
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        # 初始化一个堆，堆中的元素是(-nums[i], i)的元组，其中i是nums[i]的索引
        q = [(-nums[i], i) for i in range(k)]   # 使用负号是因为heapq默认是最小堆，我们用负号来实现最大堆的功能
        heapq.heapify(q)                        # 将列表转换成堆
        res = [-q[0][0]]                        # 初始化结果列表，存储堆中最大元素的值（取反后）

        for i in range(k, size):                # 从数组的第k个元素开始遍历到最后
            heapq.heappush(q, (-nums[i], i))    # 将当前元素加入堆中
            while q[0][1] <= i - k:             # 移除堆中索引小于当前索引减去k的元素，因为它们已经不在窗口内
                heapq.heappop(q)
            res.append(-q[0][0])                # 将堆顶元素的值（即当前窗口的最大值）取反后加入结果列表
        return res
```

## 回溯

解题步骤：

1. 定义回溯函数，明确其含义和传入参数。
2. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。
3. 书写回溯函数主体（给出选择元素、递归搜索、撤销选择部分）。

## [回溯算法的通用模板](https://datawhalechina.github.io/leetcode-notes/#/ch04/04.03/04.03.01-Backtracking-Algorithm?id=_3-%e5%9b%9e%e6%ba%af%e7%ae%97%e6%b3%95%e7%9a%84%e9%80%9a%e7%94%a8%e6%a8%a1%e6%9d%bf)

```
res = []    # 存放所欲符合条件结果的集合
path = []   # 存放当前符合条件的结果
def backtracking(nums):             # nums 为选择元素列表
    if 遇到边界条件:                  # 说明找到了一组符合条件的结果
        res.append(path[:])         # 将当前符合条件的结果放入集合中
        return

    for i in range(len(nums)):      # 枚举可选元素列表
        path.append(nums[i])        # 选择元素
        backtracking(nums)          # 递归搜索
        path.pop()                  # 撤销选择

backtracking(nums)
```

### 全排列的回溯算法代码

假设nums不存在重复元素

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []    # 存放所有符合条件结果的集合
        path = []   # 存放当前符合条件的结果
        def backtracking(nums):             # nums 为选择元素列表
            if len(path) == len(nums):      # 说明找到了一组符合条件的结果
                res.append(path[:])         # 将当前符合条件的结果放入集合中
                return

            for i in range(len(nums)):      # 枚举可选元素列表
                if nums[i] not in path:     # 从当前路径中没有出现的数字中选择
                    path.append(nums[i])    # 选择元素
                    backtracking(nums)      # 递归搜索
                    path.pop()              # 撤销选择

        backtracking(nums)
        return res
```

如果nums存在重复元素，先对数组 `nums` 进行排序，然后使用一个数组 `visited` 标记该元素在当前排列中是否被访问过。如果未被访问过则将其加入排列中，并在访问后将该元素变为未访问状态。

```
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False for _ in range(len(nums))]
        path = []
        res = []
        def backtrack(nums, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(nums, visited)
                    visited[i] = False
                    path.pop()
        backtrack(nums, visited)
        return res
```

| 题目            | 传入参数                                                                                                                                                                                                                                                                                                                                                   | 回溯函数                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 递归终止条件                                                                                                                                                                                                            | 复杂度分析                                                                                                                                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 78.子集         | 传入参数是 nums （可选数组列表）和 index（当前考虑元素的索引），全局变量是res（所有符合条件的结果）和path（当前符合条件的结果）                                                                                                                                                                                                                            | <br />`backtracking(nums, index)`函数的含义是在选择nums[index]的情况下，递归选择剩下的元素。                                                                                                                                                                                                                                                                                                                                                                                             | 正在考虑的元素位置到达数组末尾时，递归终止                                                                                                                                                                              | O(n*2^n),`其中 n 指的是数组 nums 的元素个数，2^n 指的是所有状态数。每种状态需要 O(n) 的时间来构造子集。`                                                                                                                                                                                                |
| 46.全排列       | 传入参数是 nums （可选数组列表），全局变量是res（所有符合条件的结果）和path（当前符合条件的结果）                                                                                                                                                                                                                                                          | <br />`backtracking(nums)`函数的含义是递归在 `nums` 中选择剩下的元素                                                                                                                                                                                                                                                                                                                                                                                                                   | 存放当前结果的数组 `path` 的长度等于给定数组 `nums` 的长度（即 `len(path) == len(nums)`）时，递归停止。                                                                                                           | O(n*n!),`其中 n 指的是数组 nums 的元素个数`                                                                                                                                                                                                                                                             |
| 47.全排列 II    |                                                                                                                                                                                                                                                                                                                                                            | 这道题跟「[0046. 全排列](https://leetcode.cn/problems/permutations/)」不一样的地方在于增加了序列中的元素可重复这一条件。这就涉及到了**如何去重**。我们可以先对数组 `nums` 进行排序，然后使用一个数组 `visited` 标记该元素在当前排列中是否被访问过。<br />如果未被访问过则将其加入排列中，并在访问后将该元素变为未访问状态。<br />然后再递归遍历下一层元素之前，增加一句语句进行判重：`if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue`。然后再进行回溯遍历。 | 同上，判重                                                                                                                                                                                                              | 同上                                                                                                                                                                                                                                                                                                      |
| 22.括号生成     | 传入参数是 `symbol`（用于表示是否当前组合是否成对匹配），`index`（当前元素下标），全局变量是 `parentheses`（用于保存所有有效的括号组合），`parenthesis`（当前括号组合）                                                                                                                                                                            | `backtracking(symbol, index)` 函数代表的含义是：递归根据 `symbol`，在 `(` 和 `)` 中选择第 `index` 个元素。                                                                                                                                                                                                                                                                                                                                                                       | 当 `index == 2 * n` 时，递归停止。<br />并且在 `symbol == 0` 时，当前组合才是有效的，此时将其加入到最终答案数组中。                                                                                                 | O(2^(2*n) / sqrt(n)),其中n为括号生成的对数                                                                                                                                                                                                                                                                |
| 39.组合总和     | 传入参数是 `total`（当前和）、`start_index`（剩余可选元素开始位置），全局变量是 `res`（存放所有符合条件结果的集合数组）和 `path`（存放当前符合条件的结果）                                                                                                                                                                                         | `backtrack(total, start_index):` 函数代表的含义是：当前组合和为 `total`，递归从 `candidates` 的 `start_index` 位置开始，选择剩下的元素                                                                                                                                                                                                                                                                                                                                             | 当 `total > target`时，就终止了<br />`当total == target`时，将当前结果的数组 `path` 放入答案数组 `res` 中，递归停止                                                                                             | O(n*2^n)                                                                                                                                                                                                                                                                                                  |
| 40.组合总和 II  | 跟「[0039. 组合总和](https://leetcode.cn/problems/combination-sum/)」不一样的地方在于本题不能有重复组合，所以关键步骤在于去重。在回溯遍历的时候，下一层递归的 `start_index` 要从当前节点的后一位开始遍历，即 `i + 1` 位开始。而且统一递归层不能使用相同的元素，即需要增加一句判断 `if i > start_index and candidates[i] == candidates[i - 1]: continue` | 同上，递归从 `candidates` 的 `start_index`+1 位置开始                                                                                                                                                                                                                                                                                                                                                                                                                                  | 判断 `if i > start_index and candidates[i] == candidates[i - 1]: continue`                                                                                                                                            | 同上                                                                                                                                                                                                                                                                                                      |
| 93.复原-ip-地址 | 传入参数是 `index`（剩余字符开始位置），全局变量是 `res`（存放所有符合条件结果的集合数组）和 `path`（存放当前符合条件的结果）                                                                                                                                                                                                                        | `backtracking(index):` 函数代表的含义是：递归从 `index` 位置开始，从剩下字符中，选择当前子段的值                                                                                                                                                                                                                                                                                                                                                                                       | 存放当前结果的数组 `path` 的长度等于 4，并且剩余字符开始位置为字符串结束位置（即 `len(path) == 4 and index == len(s)`）时，递归停止<br />如果回溯过程中，切割次数大于 4（即 `len(path) > 4`），递归停止，直接返回 | O(3^4 * s)，其中s是字符串 s 的长度。由于 IP 地址的每一子段位数不会超过 3，因此在递归时，我们最多只会深入到下一层中的 3 种情况。而 IP 地址由 4 个子段构成，所以递归的最大层数为 4 层，则递归的时间复杂度为 O(3^4) 。而每次将有效的 IP 地址添加到答案数组的时间复杂度为 s，所以总的时间复杂度为 O(3^4 * s ) |
| 51.N皇后        | 传入参数是 `chessboard`（棋盘数组）和 `row`（代表当前正在考虑放置第 `row` 行皇后），全局变量是 `res`（存放所有符合条件结果的集合数组）                                                                                                                                                                                                             | `backtrack(chessboard, row):` 函数代表的含义是：在放置好第 `row` 行皇后的情况下，递归放置剩下行的皇后                                                                                                                                                                                                                                                                                                                                                                                  | 在最后一行放置完皇后（即 `row == n`）时，递归停止                                                                                                                                                                     | O(n！),其中n是皇后数量                                                                                                                                                                                                                                                                                    |

### 括号生成代码

```
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
```

### 组合总和代码

```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(total, start_index):
            if total > target:
                return
  
            if total == target:
                res.append(path[:])
                return
  
            for i in range(start_index, len(candidates)):
                if total + candidates[i] > target:
                    break
  
                total += candidates[i]
                path.append(candidates[i])
                backtrack(total, i)
                total -= candidates[i]
                path.pop()
        candidates.sort()
        backtrack(0, 0)
        return res
```

### 组合总和II代码

```
class Solution:
    res = []
    path = []
    def backtrack(self, candidates: List[int], target: int, sum: int, start_index: int):
        if sum > target:
            return
        if sum == target:
            self.res.append(self.path[:])
            return

        for i in range(start_index, len(candidates)):
            if sum + candidates[i] > target:
                break
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backtrack(candidates, target, sum, i + 1)
            sum -= candidates[i]
            self.path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res.clear()
        self.path.clear()
        candidates.sort()
        self.backtrack(candidates, target, 0, 0)
        return self.res
```

### N皇后代码

```
class Solution:
    res = []
    def backtrack(self, n: int, row: int, chessboard: List[List[str]]):
        if row == n:
            temp_res = []
            for temp in chessboard:
                temp_str = ''.join(temp)
                temp_res.append(temp_str)
            self.res.append(temp_res)
            return
        for col in range(n):
            if self.isValid(n, row, col, chessboard):
                chessboard[row][col] = 'Q'
                self.backtrack(n, row + 1, chessboard)
                chessboard[row][col] = '.'

    def isValid(self, n: int, row: int, col: int, chessboard: List[List[str]]):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res.clear()
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(n, 0, chessboard)
        return self.res
```

## DFS、BFS

遍历到的节点顺序符合「后进先出」的特点，这正是「递归」和「堆栈」所遵循的规律，所以DFS可以通过「递归」或者「堆栈」来实现。

### [基于递归实现的深度优先搜索实现代码](https://datawhalechina.github.io/leetcode-notes/#/ch02/02.03/02.03.01-DFS?id=_32-%e5%9f%ba%e4%ba%8e%e9%80%92%e5%bd%92%e5%ae%9e%e7%8e%b0%e7%9a%84%e6%b7%b1%e5%ba%a6%e4%bc%98%e5%85%88%e6%90%9c%e7%b4%a2%e5%ae%9e%e7%8e%b0%e4%bb%a3%e7%a0%81)

```
class Solution:
    def dfs_recursive(self, graph, u, visited):
        print(u)                        # 访问节点
        visited.add(u)                  # 节点 u 标记其已访问

        for v in graph[u]:
            if v not in visited:        # 节点 v 未访问过
                # 深度优先搜索遍历节点
                self.dfs_recursive(graph, v, visited)
  

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

# 基于递归实现的深度优先搜索
visited = set()
Solution().dfs_recursive(graph, "A", visited)
```

## [基于堆栈实现的深度优先搜索](https://datawhalechina.github.io/leetcode-notes/#/ch02/02.03/02.03.01-DFS?id=_4-%e5%9f%ba%e4%ba%8e%e5%a0%86%e6%a0%88%e5%ae%9e%e7%8e%b0%e7%9a%84%e6%b7%b1%e5%ba%a6%e4%bc%98%e5%85%88%e6%90%9c%e7%b4%a2)

```
class Solution:
    def dfs_stack(self, graph, u):
        print(u)                            # 访问节点 u
        visited, stack = set(), []          # 使用 visited 标记访问过的节点, 使用栈 stack 存放临时节点
  
        stack.append([u, 0])                # 将节点 u，节点 u 的下一个邻接节点下标放入栈中，下次将遍历 graph[u][0]
        visited.add(u)                      # 将起始节点 u 标记为已访问
  
  
        while stack:
            u, i = stack.pop()              # 取出节点 u，以及节点 u 下一个将要访问的邻接节点下标 i
  
            if i < len(graph[u]):
                v = graph[u][i]             # 取出邻接节点 v
                stack.append([u, i + 1])    # 下一次将遍历 graph[u][i + 1]
                if v not in visited:        # 节点 v 未访问过
                    print(v)                # 访问节点 v
                    stack.append([v, 0])    # 下一次将遍历 graph[v][0]
                    visited.add(v)          # 将节点 v 标记为已访问  
  

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D", "G"],
    "G": []
}

# 基于堆栈实现的深度优先搜索
Solution().dfs_stack(graph, "A")
```

因为遍历到的节点顺序符合「先进先出」的特点，所以BFS可以通过「队列」来实现。

### [基于队列实现的广度优先搜索实现代码](https://datawhalechina.github.io/leetcode-notes/#/ch02/02.05/02.05.01-BFS?id=_32-%e5%9f%ba%e4%ba%8e%e9%98%9f%e5%88%97%e5%ae%9e%e7%8e%b0%e7%9a%84%e5%b9%bf%e5%ba%a6%e4%bc%98%e5%85%88%e6%90%9c%e7%b4%a2%e5%ae%9e%e7%8e%b0%e4%bb%a3%e7%a0%81)

```
import collections

class Solution:
    def bfs(self, graph, u):
        visited = set()                     # 使用 visited 标记访问过的节点
        queue = collections.deque([])       # 使用 queue 存放临时节点
  
        visited.add(u)                      # 将起始节点 u 标记为已访问
        queue.append(u)                     # 将起始节点 u 加入队列中
  
        while queue:                        # 队列不为空
            u = queue.popleft()             # 取出队头节点 u
            print(u)                        # 访问节点 u
            for v in graph[u]:              # 遍历节点 u 的所有未访问邻接节点 v
                if v not in visited:        # 节点 v 未被访问
                    visited.add(v)          # 将节点 v 标记为已访问
                    queue.append(v)         # 将节点 v 加入队列中
  

graph = {
    "0": ["1", "2"],
    "1": ["0", "2", "3"],
    "2": ["0", "1", "3", "4"],
    "3": ["1", "2", "4", "5"],
    "4": ["2", "3"],
    "5": ["3", "6"],
    "6": []
}

# 基于队列实现的广度优先搜索
Solution().bfs(graph, "0")
```

### DFS-岛屿数量代码

```
class Solution:
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
```

## DFS-岛屿面积代码

```
class Solution:
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
            return 0
        ans = 1
        grid[i][j] = 0
        ans += self.dfs(grid, i + 1, j)
        ans += self.dfs(grid, i, j + 1)
        ans += self.dfs(grid, i - 1, j)
        ans += self.dfs(grid, i, j - 1)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans
```

| 题目                         | 方法         | 思路                                                                                                                                                                                                                                                                                                                                                                                                                       | 复杂度分析                      |
| ---------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| 124.二叉树中的最大路径和     | DFS-递归遍历 | 1.如果根节点 `root` 为空，则返回 `0`。<br />2.递归计算左子树的最大贡献值为 `left_max`。<br />3.递归计算右子树的最大贡献值为 `right_max`。<br />4.更新维护最大路径和变量，即 `self.max_sum = max(self.max_sum, root.val + left_max + right_max)`。<br />5.返回以当前节点为根节点，并且经过该节点的最大贡献值。即返回「当前节点值」+「左右子节点的最大贡献值中较大的一个」。<br />6.最终 `self.max_sum` 即为答案 | O(n)，n表示二叉树的节点数目     |
| 129.求根节点到叶节点数字之和 | DFS-递归遍历 | 1.记录下路径上所有节点构成的数字，使用变量 `pre_total` 保存下当前路径上构成的数字。<br />2.如果遇到叶节点，则直接返回当前数字<br />3.如果没有遇到叶节点，则递归遍历左右子树，并累加对应结果                                                                                                                                                                                                                              | 同上                            |
| 543.二叉树的直径             | DFS-递归遍历 | 这里的直径并不是简单的「左子树高度」+「右子树高度」。而是 `当前节点的直径 = max{左子树高度+右子树高度，所有子树中最大直径}。`maxDiameter `变量。每次递归都要去判断 当前「左子树高度」+「右子树的高度」是否大于`self.maxDiameter `，如果大于，则更新最大值。`                                                                                                                                                         | 同上                            |
| 200.岛屿数量                 | DFS-递归遍历 | 1. 遍历grid<br />2. 对于每一个字符为‘1’的元素，遍历其上下左右四个方向，并将该字符置为‘0’，保证下次不会重复遍历<br />3. 如果超出边界，返回0<br />4. 统计DFS的次数即为所求                                                                                                                                                                                                                                               | O(m*n),其中m和n分别是行数和列数 |
| 695.岛屿的最大面积           | DFS-递归遍历 | 1. 遍历二维数组的每一个元素，对于每个值为 `1` 的元素：<br />（1）将该位置上的值置为 `0`（防止二次重复计算）。<br />（2）递归搜索该位置上下左右四个位置，并统计搜到值为 `1` 的元素个数。<br />（3）返回值为 `1` 的元素个数（即为该岛的面积）<br />2. 维护并更新最大的岛面积<br />3. 返回最大的岛面积                                                                                                                | 同上                            |
| 662.二叉树最大宽度           | BFS          | 遍历每一层的节点，在向队列中添加节点时，将该节点与该节点对应的编号一同存入队列中。这样在计算每一层节点的宽度时，我们可以通过队列中队尾节点的编号与队头节点的编号，快速计算出当前层的宽度。并计算出所有层宽度的最大值。                                                                                                                                                                                                     | O(n)                            |
|                              |              |                                                                                                                                                                                                                                                                                                                                                                                                                            |                                 |

### DFS——二叉树直径计算代码

```
class Solution:
    def __init__(self):
        # 保存当前最大直径
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height(root)
        return self.maxDiameter

    def height(self, root):
        if root == None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)

        return max(leftHeight, rightHeight) + 1
```

### BFS-计算二叉树宽度计算代码

```
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return False

        queue = collections.deque([[root, 0]])
        ans = 0
        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            size = len(queue)
            for _ in range(size):
                cur, index = queue.popleft()
                if cur.left:
                    queue.append([cur.left, index * 2 + 1])
                if cur.right:
                    queue.append([cur.right, index * 2 + 2])
        return ans
```

## 动态规划

解题步骤：

1. 划分阶段
2. 定义状态
3. 状态转移方程
4. 初始条件
5. 最终结果

| col1                       | 划分阶段                                                                                 | 状态定义                                                                                                                                 | 状态转移方程                                                                                                                                                                                                                                                                                | 初始条件                                                                          | 最终结果                                                                                                                                          | 复杂度分析                                                     |
| -------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 322.零钱兑换               | 按照子串的起始位置                                                                       | `dp[i]` 表示为：凑成总金额为 `i` 的最少硬币数量                                                                                      | for coin in coins:<br />for i in range(coin, amount+1):<br />dp[i]=min(dp[i], dp[i-coin]+1)<br />dp[i]来源于两部分：<br />（1）不使用当前硬币，只使用之前硬币凑成金额i的最少硬币数量。<br />（2）使用当前硬币，凑成金额i-<br />num的最少硬币数量。                                          | dp[0]=0                                                                           | dp[amount]                                                                                                                                        | O(amount * size), amount表示总金额，size表示硬币的种类数       |
| 5.最长回文子串             | 按照区间长度                                                                             | dp[i][j]表示字符串s在区间[i,j]范围内是否是一个回文串                                                                                     | 当子串只有1位或者2位的时候，dp[i][j] = (s[i]==s[j]),如果子串大于2位，dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]                                                                                                                                                                               | dp[i][j] =False                                                                   | s[max_start, max_start+max_len]，<br />max_len=j-i+**1，<br />max_start**=i，<br />max_start表示最长回文子串的起始位置, max_len表示最大长度 | O(n^2)，n表示字符串的长度                                      |
| 32.最长有效括号            | 按照最长有效括号子串的结束位置                                                           | `dp[i]` 表示为：以字符 `s[i]` 为结尾的最长有效括号的长度                                                                             | if `s[i] == '('`, then `dp[i] = 0`if `s[i] == ')'`, if i >= 2: dp[i]=dp[i-2]+2else:dp[i]=2...                                                                                                                                                                                         | `dp[i] = 0`                                                                     | `max(dp[i])`                                                                                                                                    | O(n)，n表示字符串的长度                                        |
| 53.最大子数组和            | 按照连续子数组的结束位置                                                                 | `dp[i]` 表示为：以第i个数为结尾的连续子数组的最大和                                                                                    | if dp[i-1]<0, then dp[i]=nums[i]else:dp[i] = dp[i-1]+nums[i]                                                                                                                                                                                                                                | dp[0]=nums[0]                                                                     | max(dp)                                                                                                                                           | O(n)，n表示数组的元素个数                                      |
| 152.乘积最大子数组         | 乘积有个特殊情况，两个正数、两个负数相乘都会得到正数。所以求解的时候需要考虑负数的情况。 | 定义状态 `dp_max[i]` 为：以第 i 个元素结尾的乘积最大子数组的乘积。定义状态 `dp_min[i]` 为：以第 i 个元素结尾的乘积最小子数组的乘积。 | `dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1]* nums[i])`<br /><br />dp_min[i] = min(dp_min[i-1]**nums[i], nums[i], dp_max[i-1]**nums[i]*)                                                                                                                              | `dp_max[0] = nums[0], dp_min[0] = nums[0]`                                      | **max**(**dp_max**)                                                                                                                   | O(n)，n表示数组的元素个数                                      |
| 300.最长递增子序列         | 按照子序列的结尾位置                                                                     | dp[i]表示为：以 nums[i] 结尾的最长递增子序列长度                                                                                         | **if** nums[**i**] ***>** nums*[**j**]:<br />dp[i]=max(dp[i], dp[j]+1)                                                                                                                                                                                            | dp[i]=1                                                                           | max(dp)                                                                                                                                           | O(n^2)，n表示子序列的长度                                      |
| 72.编辑距离                | 按照两个字符串的结尾位置                                                                 | dp[i][j]表示「以word1 中前 i 个字符组成的子字符串 str1」变为「以 word2 中前 j 个字符组成的子字符串 str2」，所需要的最少操作次数。        | if word1[i-1]==word2[j-1],<br />then dp[i][j] = dp[i-1][j-1]<br />else:<br />dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1                                                                                                                                                       | dp[0][j]=j,<br />dp[i][0]=i                                                       | dp[size1][size2]                                                                                                                                  | T(n)=O(m×n),S(n)=O(m×n)      其中 m，n分别是grid的行数和列数 |
| 1143.最长公共子序列        | 同上                                                                                     | dp[i][j]表示「以text1 中前 i 个字符组成的子字符串 str1」与「以 text2 中前 j 个字符组成的子字符串 str2」的最长公共子序列长度              | if text1[i-1]==text2[j-1],<br />then dp[i][j] = dp[i-1][j-1] + 1<br />else:<br />dp[i][j] = max(dp[i-1][j], dp[i][j-1])                                                                                                                                                                     | dp[0][j]=0,<br />dp[i][0]=0                                                       | 同上                                                                                                                                              | 同上                                                           |
| 718.最长重复子数组         | 按照子数组结尾位置                                                                       | dp[i][j]表示「以nums1 中前 i 个元素为子数组」与「以 nums2 中前 j 个元素为子数组」的最长公共子数组长度                                    | if nums1[i]==nums2[j],<br />then dp[i][j]=dp[i-1][j-1]+1<br />else:<br />dp[i][j]=0                                                                                                                                                                                                         | dp[0][j]=0,<br />dp[i][0]=0                                                       | res=0,<br />res=max(res, dp[i][j])                                                                                                                | 同上                                                           |
| 62.不同路径                | 按照路径的结尾位置（行位置、列位置组成的二维坐标）                                       | dp[i][j]表示从左上角(0,0)到达 (i,j) 位置的路径数量。                                                                                     | dp[i][j] = dp[i-1][j] + dp[i][j-1]                                                                                                                                                                                                                                                          | dp[0][0]=1,<br />dp[0][j]=1,<br />dp[i][0]=1                                      | dp[m-1][n-1]                                                                                                                                      | 同上                                                           |
| 63.不同路径 II             | 同上                                                                                     | 同上                                                                                                                                     | dp[i][j] = dp[i-1][j] + dp[i][j-1],其中obstacleGrid[i][j]=0                                                                                                                                                                                                                                 | 如果在第一行、第一列遇到障碍，则终止赋值，跳出循环。                              | 同上                                                                                                                                              | 同上                                                           |
| 64.最小路径和              | 同上                                                                                     | 同上                                                                                                                                     | dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]                                                                                                                                                                                                                                         | dp[0][0]=grid[0][0],dp[i][0]=dp[i-1][0]+grid[i][0],dp[0][j]=dp[0][j-1]+grid[0][j] | 同上                                                                                                                                              | 同上                                                           |
| 221.最大正方形             | 按照正方形的右下角坐标                                                                   | 以矩阵位置 (i,j) 为右下角，且值包含 1 的正方形的最大边长                                                                                 | 只有当矩阵位置 (i,j) 值为 1 时，才有可能存在正方形。<br />if matrix[**i**]****[**j**]=='1'****: **if** i **==** **0** **or** j **==** **0**:dp[i][j]=1<br />else:<br />dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 | dp[i][j]=0                                                                        | max_size=***max**(**max_size**,* dp[**i**]**[**j**]***)<br />max_size * *max_size*                              | 同上                                                           |
| 198.打家劫舍               | 按照房屋序号                                                                             | dp[i]表示前i间房屋所能偷窃到的最高金额                                                                                                   | dp[i]=nums[0] (i=1)<br /><br />dp[i]=max(dp[i-2]+nums[i-1], dp[i-1]) (i>=2)                                                                                                                                                                                                                 | dp[0]=0<br />dp[1]=nums[0]                                                        | dp[size]                                                                                                                                          | O(n)                                                           |
| 213.打家劫舍 II            | 同上                                                                                     | 同上                                                                                                                                     | 同上                                                                                                                                                                                                                                                                                        | 同上                                                                              | 分别求解[0,size-2]和[1,size-1]范围下首尾不相连的房屋所能偷到的最高金额 ans1，ans2，则最终金额为 max(ans1, ans2)                                   | O(n)                                                           |
| 139.单词拆分               | `按照单词结尾位置`                                                                     | `dp[i] 表示：长度为 i 的字符串 s[0: i] 能否拆分成单词，如果为 True 则表示可以拆分，如果为 False 则表示不能拆分`                        | `如果 s[0: j] 可以拆分为单词（即 dp[j] == True），并且字符串 s[j: i] 出现在字典中，则 dp[i] = True`                                                                                                                                                                                       | `dp[0] = True`                                                                  | `dp[size]`                                                                                                                                      | O(n)                                                           |
| 140.单词拆分 II            | `动态规划和回溯`                                                                       |                                                                                                                                          |                                                                                                                                                                                                                                                                                             |                                                                                   |                                                                                                                                                   |                                                                |
| 123.买卖股票的最佳时机-iii | 三维DP                                                                                   |                                                                                                                                          |                                                                                                                                                                                                                                                                                             |                                                                                   |                                                                                                                                                   |                                                                |
| 494.目标和                 |                                                                                          | `dp[i]` 表示为：填满容量为 `i` 的背包，有 `dp[i]` 种方法                                                                           | `dp[i] = dp[i] + dp[i - num]`                                                                                                                                                                                                                                                             | `dp[0] = 1`                                                                     | `dp[sise]`                                                                                                                                      | O(n)                                                           |

494.目标和

假设数组中所有元素和为 `sum`，数组中所有符号为 `+` 的元素为 `sum_x`，符号为 `-` 的元素和为 `sum_y`。则 `target = sum_x - sum_y`。

而 `sum_x + sum_y = sum`。根据两个式子可以求出 `2 * sum_x = target + sum `，即 `sum_x = (target + sum) / 2`。

那么这道题就变成了，如何在数组中找到一个集合，使集合中元素和为 `(target + sum) / 2`。这就变为了求容量为 `(target + sum) / 2` 的 0-1 背包问题。

填满容量为 `i` 的背包的方法数来源于：

1. 不使用当前`num`：只使用之前元素填满容量为`i` 的背包的方法数。
2. 使用当前`num`：填满容量`i - num` 的包的方法数，再填入`num` 的方法数。

## 贪心

| 题目                      | 思路                                                                                                                                                                                                                                                                                                                                     | 复杂度分析                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| 121.买卖股票的最佳时机    | 设置两个变量 `minprice`（用来记录买入的最小值）、`maxprofit`（用来记录可获取的最大利润），从左到右进行遍历数组 `prices`，如果遇到当前价格比 `minprice` 还要小的，就更新 `minprice。如果遇到当前价格大于或者等于 minprice，则判断一下以当前价格卖出的话能卖多少，如果比 maxprofit 还要大，就更新 maxprofit。最后输出 maxprofit` | O(n)，其中n是数组prices的元素个数 |
| 122.买卖股票的最佳时机-ii | 通过两两相减所得的差值来累加计算波峰和谷底的差值<br />ans = 0<br />for i in range(1, len(prices)):<br />ans += max(0, prices[i]-prices[i-1])                                                                                                                                                                                             | O(n)                              |
|                           |                                                                                                                                                                                                                                                                                                                                          |                                   |

## 位运算

| 题目                 | 思路                                                                    | 复杂度分析 |
| -------------------- | ----------------------------------------------------------------------- | ---------- |
| 136.只出现一次的数字 | 根据异或运算的性质，对 n 个数不断进行异或操作，最终可得到单次出现的元素 | O(n)       |
|                      |                                                                         |            |

#### 只出现一次的数

```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
```
