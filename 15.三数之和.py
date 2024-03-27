#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    # 思路 1：对撞指针
    # 先将数组进行排序，以保证按顺序查找 a、b、c 时，元素值为升序，从而保证所找到的三个元素是不重复的。同时也方便下一步使用双指针减少一重遍历。
    # 第一重循环遍历 a，对于每个 a 元素，从 a 元素的下一个位置开始，使用对撞指针 left，right。left 指向 a 元素的下一个位置，right 指向末尾位置。先将 left 右移、right 左移去除重复元素，再进行下边的判断。
    # 如果 nums[a] + nums[left] + nums[right] = 0，则得到一个解，将其加入答案数组中，并继续将 left 右移，right 左移；
    # 如果 nums[a] + nums[left] + nums[right] > 0，说明 nums[right] 值太大，将 right 向左移；
    # 如果 nums[a] + nums[left] + nums[right] < 0，说明 nums[left] 值太小，将 left 右移。
    # 时间复杂度：O(n^2)
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


# @lc code=end

