"""
okay so the problem with sorting is that

the time complexity is o(m * (n log n)) where m len(arr), n avg len of string in arr

we can get this down to ( m * n * 26) by having the key in the hash map be the 

character count of the word

hat -> h:1, a:1, t:1



"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            seen[tuple(count)].append(word)

        return list(seen.values())