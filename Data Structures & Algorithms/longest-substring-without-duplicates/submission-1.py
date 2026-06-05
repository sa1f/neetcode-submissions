"""
pwwkew
step - 0
l - 0
r - 0
seen {}
max_len 0

step - 1
l - 0
r - 1
seen {p:0}
max_len 0

step - 2
l - 0
r - 2
seen {p:0, w:1}
max_len 0

step - 3
l - 2
r - 2
seen {p:0}
max_len 2

step - 4
l - 2
r - 3
seen {p:0, w:2}
max_len 2

step - 5
l - 2
r - 4
seen {p:0, w:2, k:3}
max_len 2

step - 6
l - 2
r - 5
seen {p:0, w:2, k:3, e:4}
max_len 2

step - 7
l - 2
r - 5
seen {p:0, w:2, k:3, e:4}
max_len 2
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = {}
        max_len = 0

        for r, char in enumerate(s):
            if char in seen:
                l = max(l, seen[char] + 1)
            seen[char] = r
            max_len = max(max_len, r - l + 1)
        return max_len
