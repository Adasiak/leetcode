from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    first = min(strs, key=len)

    for i, ch in enumerate(first):
        for s in strs:
            if s[i] != ch:  # rozbieżność
                return first[:i]
    return first



def longest_common_prefix(list_s):
    if not list_s:
        return ""
    first = min(list_s, key=len)
    for i, char in enumerate(first):
        for string in list_s:
            if string[i] != char[i]:
                return first[:i]
    return first



def lcp(l):
    if not l:
        return ""
    f = min(l, key=len)
    for i, char in enumerate(l):
        for s in l:
            if s[i] != char[i]:
                return f[:i]
    return f