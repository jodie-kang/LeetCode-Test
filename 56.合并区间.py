#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    # 思路 1：排序
    # 设定一个数组 ans 用于表示最终不重叠的区间数组，然后对原始区间先按照区间左端点大小从小到大进行排序。
    # 遍历所有区间。
    # 先将第一个区间加入 ans 数组中。
    # 然后依次考虑后边的区间：
    # 如果第 i 个区间左端点在前一个区间右端点右侧，则这两个区间不会重合，直接将该区间加入 ans 数组中。
    # 否则的话，这两个区间重合，判断一下两个区间的右区间值，更新前一个区间的右区间值为较大值，然后继续考虑下一个区间，以此类推。
    # 最后返回数组 ans。
    # 时间复杂度：O(n log n)，空间复杂度：O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
# @lc code=end

