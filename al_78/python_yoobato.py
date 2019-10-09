# LeetCode
# 78. Subsets
# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        self.dfs(nums, answer, [])
        return answer

    def dfs(self, nums, answer, subset):
        answer.append(subset)
        for i in range(0, len(nums)):
            self.dfs(nums[i+1:], answer, subset + [nums[i]])

# For test
# print(Solution().subsets([1, 2, 3]))
