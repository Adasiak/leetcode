class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        start = 0

        for index, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = index
            max_length = max(max_length, index - start + 1)

        return max_length
    
    


def length_of_longest_substring(s):
    max_length = 0 
    char_index_map = {}
    start = 0 
    
    for i, v in enumerate(s):
        if v in char_index_map and char_index_map >= start:
            start = char_index_map[v] +1
        char_index_map[v] = i
        max_length = max_length(max_length, i - start +1)
    return max_length



def length_od_longest_sub(s):
    max_l = 0
    map_I = {}
    s1 = 0
    
    for i, v in enumerate(s):
        if v in map_I and map_I[v] >= s1:
            s1 = map_I[v] +1
        map_I[v] = i
        max_l = max(max_l, i - s1 +1)
    return max_l