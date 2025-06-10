from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        
        clone = nums
        list_of_index_to_remove = []
        list_to_print = []
        for i in range(len(nums)):
            if nums[0] >= nums[-1]:
                list_of_index_to_remove.append(0)
            elif i == 0 or i +1 == len(nums):
                continue
            elif nums[i - 1] <= nums[i] and nums[i] >= nums[i + 1] and nums[i - 1] <= nums[i + 1]:
                list_of_index_to_remove.append(i)
            elif nums[i - 1] >= nums[i] >= nums[i + 1]:
                list_of_index_to_remove.append(i - 1)
                list_of_index_to_remove.append(i)
        
            
            # else:
                
        print(list_of_index_to_remove)
        list_of_index_to_remove.reverse()
        for i in list_of_index_to_remove:
            nums.pop(i)
        return len(nums)
    
from bisect import bisect_left
from typing import List

# ─────────────────────────────────────────────────────────────
# 1. DP O(n²)  – długość + opcjonalna rekonstrukcja sekwencji
# ─────────────────────────────────────────────────────────────
def lis_quadratic(nums: List[int]) -> int:
    """
    Zwraca długość najdłuższej rosnącej podsekwencji (LIS) w czasie O(n²).

    Jeśli chcesz pełną sekwencję, odkomentuj blok 'prev' + rekonstrukcję.
    """
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n          # dp[i] = długość LIS kończącej się na i
    # prev = [-1] * n     # do odtworzenia ścieżki (opcjonalnie)

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                # prev[i] = j

    # --- jeśli potrzebujesz samej długości ---
    return max(dp)

    # # --- jeśli chcesz też sekwencję ---      (odkomentuj)
    # best_end = max(range(n), key=dp.__getitem__)
    # lis = []
    # while best_end != -1:
    #     lis.append(nums[best_end])
    #     best_end = prev[best_end]
    # return list(reversed(lis))  # pełna sekwencja


# ─────────────────────────────────────────────────────────────
# 2. Patience-sorting O(n log n) – tylko długość
# ─────────────────────────────────────────────────────────────
def lis_binary(nums: List[int]) -> int:
    """
    Zwraca długość LIS w O(n log n) przy użyciu tablicy `tails`.
    Nie rekonstruuje sekwencji, za to działa szybko dla dużych n.
    """
    tails: List[int] = []            # tails[len] = minimalny ogon sekwencji o danej długości

    for x in nums:
        pos = bisect_left(tails, x)  # pierwsza pozycja >= x
        if pos == len(tails):
            tails.append(x)          # wydłużamy najdłuższą sekwencję
        else:
            tails[pos] = x           # poprawiamy (zmniejszamy) ogon
    return len(tails)


# ─────────────────────────────────────────────────────────────
# 3. Krótki test obu funkcji
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sample = [10, 9, 2, 5, 3, 7, 101, 18]

    print("O(n²)  LIS length:", lis_quadratic(sample))   # 4
    print("O(nlogn) LIS length:", lis_binary(sample))    # 4




def lis_quadratic(nums: List[int]) -> int:
    """
    Zwraca długość najdłuższej rosnącej podsekwencji (LIS) w czasie O(n²).

    Jeśli chcesz pełną sekwencję, odkomentuj blok 'prev' + rekonstrukcję.
    """
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n          # dp[i] = długość LIS kończącej się na i
    # prev = [-1] * n     # do odtworzenia ścieżki (opcjonalnie)

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                # prev[i] = j

    # --- jeśli potrzebujesz samej długości ---
    return max(dp)


def lis_quadratic(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp)


def lis(nums):
    if not nums:
        return 0
    l = len(nums)
    dp = [1]*l
    for i in range(l):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return max(dp)


def lis(nums):
    if not nums:
        return 0
    l = len(nums)
    dp = [1]*l
    for i in range(l):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] +1
    return max(dp)


def lis(nums):
    if not nums:
        return 0
    l = len(nums)
    dp = [1]*l
    for i in range(l):
        for j in range(i):
            if nums[j] < nums[i] and dp[j]+1>dp[i]:
                dp[i] = dp[j]+1
    return max(dp)



def lis(nums):
    if not nums:
        return 0
    l = len(nums)
    dp = [1]*l
    for i in range(l):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1 
    return max(dp)