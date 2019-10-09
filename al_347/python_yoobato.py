# LeetCode
# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer = []

        # 1. Make Dictionary
        numDic = {}
        for num in nums:
            if num in numDic:
                numDic[num] += 1
            else:
                numDic[num] = 1
        
        # 2. Sort dictinoary by value
        numDic = sorted(numDic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

        # 3 Find k-most
        i = 0
        for num in numDic:
            if i >= k:
                break
            
            answer.append(num[0])
            i += 1
        
        return answer

# For test
# print(Solution().topKFrequent([1,1,1,2,2,3], 2))
