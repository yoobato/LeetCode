// LeetCode
// 344. Reverse String
// https://leetcode.com/problems/reverse-string/

class Solution {
    func reverseString(s: String) -> String {
        var reversedString: String = ""
        for r in s.characters {
            reversedString = "\(r)" + reversedString
        }
        return reversedString
    }
}

// For test
//print(Solution().reverseString("hello"))
