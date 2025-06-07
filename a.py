# text = "Mississippi"
# char_to_find = "i"
# indices = [index for index, char in enumerate(text) if char == char_to_find]
#
# print(f"Character '{char_to_find}' found at indices: {indices}")
#
# print(text[0])
#
#
# text = "Mississippi"
# sorted_text = sorted(text)
# print(f"Sorted string: {sorted_text}")
#
# #  iter in dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key, v in my_dict.items():
#     print(f"Key: {key}, Value: {v}")
#
#
# return index of element in list
#
# def find_index(lst, element)
#
# # sort list of strings by length

# s = " "
# def lengthOfLongestSubstring(s: str) -> int:
#     m = []
#     l = ""
#     for i in s:
#         if i not in l:
#             l += i
#         else:
#             m.append(l)
#             l = i
#     if l:
#         m.append(l)
#     print(m)
#     sorted_s = sorted(m, key=len)
#     lenn = len(sorted_s)
#     if lenn >= 1:
#         return len(sorted_s[-1])
#     # elif lenn == 1:
#     #     return 1
#     else:
#         return 0
#
# s1 = "dvdf"
#
# print(lengthOfLongestSubstring(s1))


def lengthOfLongestSubstring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for index, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = index
        max_length = max(max_length, index - start + 1)

    return max_length



def lengthOfLongestSubstring(ss):
    char_index = {}
    start = 0
    max_length = 0

    for index, char in enumerate(ss):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] +1
        char_index[char] = index
        max_length = max(max_length, index - start + 1)
    return max_length




































