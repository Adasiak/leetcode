from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = range(1, len(nums)+1)
        silnia = 1
        for i in l:
            silnia *= i
        print(silnia)
        return_lists = [["."]*len(nums) for _ in range(silnia)]
        print(return_lists)
        bucket = nums
        tmp = []
        for elem in range(len(return_lists)):
            # for i in range(elem):
            i = 0
            while "." in return_lists[elem]:
                a = bucket.pop(0)
                if a not in tmp:
                    tmp.append(a)
                bucket.append(a)
                if tmp in return_lists:
                    tmp.pop()
        return return_lists

def permute(nums):
    res = []
    def dfs(path, remaining):
        if not remaining:
            res.append(path)
            return
        for i, x in enumerate(remaining):
            dfs(path + [x], remaining[:i] + remaining[i+1:])
    dfs([], nums)
    return res


def permutate(nums):
    res = []
    def dfs(path, rem):
        if not rem:
            res.append(path)
            return
        for i, v in enumerate(rem):
            dfs(path + [v], rem[:i] + rem[i+1:])
            
    dfs([], nums)
    return res


def permutate(nums):
    res = []
    def ss(lis, rest):
        if not rest:
            res.append(lis)
            return
        for i, v in enumerate(rest):
            ss(lis + [v], rest[:i] + rest[i+1:])
    ss([], nums)
    return res