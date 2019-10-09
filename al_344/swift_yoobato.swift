// LeetCode
// 344. Reverse String
// https://leetcode.com/problems/reverse-string/

class Solution {
    func reverseString(_ s: inout [Character]) {
        var left = 0
        var right = s.count - 1
        while left < right {
            // Swap
            (s[left], s[right]) = (s[right], s[left])
            left += 1
            right -= 1
        }
    }
}

// For test
//var s: [Character] = ["h", "e", "l", "l", "o"]
//Solution().reverseString(&s)
//print(s)
