from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        len_list = len(prices)
        # max_max_differ = max(prices) - min(prices)
        min_min = prices[0]
        # max_max = 0
        begin = 0
        if len_list ==1:
            return 0
        elif len_list == 2:
            return max(0,prices[1]-prices[0])
        else:
            if prices[0] > prices[1]:
                begin = 1
            # if prices[-2]
            for i in range(begin, (len_list-1)):
                # if (i + 1) == len_list:
                #     continue
                # for j in range(i, len_list):
                # if prices[j]>prices[i]:
                if prices[i] <= min_min:
                    min_min = prices[i]
                    # if prices[i] > max_max:
                    max_max = max(prices[i:])
                    if max_max > min_min:
                        tmp_prof = max_max - min_min
                        if tmp_prof > max_prof:
                            max_prof = tmp_prof
                # if max_prof >= (len_list-1):
                #     return max_prof
            return max_prof
# prices = [7,1,5,3,6,4]
# print(Solution.maxProfit(prices))

# sol = Solution()
# print(sol.maxProfit(prices=pp))