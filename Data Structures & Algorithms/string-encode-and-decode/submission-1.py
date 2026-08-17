"""
strs = ["Hello","World"]

#5#Hello#5#World

idx = 0
count_start_idx = 0
count_end_idx = 0
while idx < len of string:
    while curr char not #:
        increment count_end_idx
    count_str = string[count_start_idx + 1: count_end_idx]
    str_count = int(count_str)
    str = string[count_start_idx + 1: ]
  

---
Edge cases: 
- number of strings = 0
- one empty string
--- 

---
encode

result = ""

for each string
 calculate length
 append '#' + str(length) + '#' + string

 ---
 decode

 left = 0
 right = 0



"""

import secrets

class Solution:
    def encode(self, strs):
        result = ""
        for s in strs:
            result += f"#{len(s)}#{s}"
        return result




    def decode(self, str):
        if len(str) < 2:
            return []
        
        result = []
        count_start_idx = 0
        count_end_idx = 1
        
        while count_start_idx < len(str):
            while str[count_end_idx] != '#':
                count_end_idx += 1
            count_str = str[count_start_idx + 1: count_end_idx]
            count = int(count_str)
            curr_str = str[count_end_idx + 1: count_end_idx + 1 + count]
            result.append(curr_str)
            print(f"start = {count_start_idx} end = {count_end_idx} count_str = {count} curr_str = {curr_str}")
            count_start_idx = count_end_idx + count + 1
            count_end_idx = count_start_idx + 1
            
        
        return result
