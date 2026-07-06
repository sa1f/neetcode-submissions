"""
requirements
- given two strings, s & t, return true if the two strings are anagrams of each other
  an anagram is a string that contains the exact same characters as another string 
  but order can be different


ideas:

- easy compare length, if not same, then false
- one option is to sort both strings, compare them and if they're the same, then
  return true O(nlogn) time complexity, O(1) space complexity

- Another option is to keep a dict with a map of character and count
  walk through first string to build character count
  walk through second string build character count
  compare character count, if we spot a difference then it's false, otherwise true
  O(n) space and time complexity
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.first(s,t)

    def first(self, s, t):
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t
    
    def second(self, s, t):
        seen_s = {}
        seen_t = {}

        for char in s:
            seen_s[char] = seen_s.get(char, 0) + 1
        for char in t:
            seen_t[char] = seen_t.get(char, 0) + 1

        for char, val in seen_s:
            if seen_t[char] != val:
                return False
        return True

        