# LeetCode
# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        self.backtracking(answer, n)
        return answer
      
    def backtracking(self, answer, n, cur = '', left = 0, right = 0):
      if len(cur) == n * 2:
        answer.append(cur)
        return

      if left < n:
        self.backtracking(answer, n, cur + '(', left + 1, right)
      if right < left:
        self.backtracking(answer, n, cur + ')', left, right + 1)

# For test
# print(Solution().generateParenthesis(3))
