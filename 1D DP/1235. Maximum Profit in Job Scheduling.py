import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not (startTime or endTime or profit):
            return 0
        
        m, n, b = len(startTime), len(endTime), len(profit)
        if m != n or m != b:
            return 0
        
        
        combined_list = []
        for i in range(m):
            combined_list.append((startTime[i], endTime[i], profit[i]))
        
        combined_list.sort(key=lambda x: x[1])

        sorted_end_times = [job[1] for job in combined_list]
        dp = [0] * (m + 1)
        
        for i in range(n):
            current_start_time = combined_list[i][0]
            current_end_time = combined_list[i][1]
            current_profit = combined_list[i][2]
            
            # Opcja 1: Nie wybieramy bieżącego zlecenia.
            # Maksymalny zysk to ten z poprzedniego kroku.
            # dp[i] odpowiada maksymalnemu zyskowi z pierwszych 'i' zleceń
            # (czyli zleceń o indeksach od 0 do i-1 w liście 'jobs').
            profit_without_current = dp[i]
            
            # Opcja 2: Wybieramy bieżące zlecenie.
            # Musimy znaleźć ostatnie zlecenie, które zakończyło się PRZED
            # lub W MOMENCIE rozpoczęcia bieżącego zlecenia.
            
            # bisect_right() zwraca indeks, gdzie 'current_start_time' mógłby
            # zostać wstawiony, aby lista 'sorted_end_times' pozostała posortowana.
            # Wszystkie elementy na lewo od tego indeksu są mniejsze lub równe
            # 'current_start_time'.
            # Jeśli bisect_right zwróci 'k', to oznacza, że 'k' zleceń kończy się
            # przed lub w momencie rozpoczęcia bieżącego.
            
            # W tablicy DP, dp[k] reprezentuje maksymalny zysk, gdy rozważamy
            # pierwsze 'k' zleceń (od indeksu 0 do k-1 w 'jobs').
            # Dlatego 'prev_job_dp_index' jest równe wartości zwróconej przez bisect_right.
            prev_job_dp_index = bisect.bisect_right(sorted_end_times, current_start_time)
            
            # 'profit_from_previous_non_conflicting_jobs' to maksymalny zysk
            # z zleceń, które zakończyły się przed 'current_start_time'.
            # Ten zysk jest już obliczony i przechowywany w dp[prev_job_dp_index].
            profit_from_previous_non_conflicting_jobs = dp[prev_job_dp_index]
            
            # Całkowity zysk, jeśli wybierzemy bieżące zlecenie.
            profit_with_current = current_profit + profit_from_previous_non_conflicting_jobs
            
            # Zapisz maksymalny zysk dla 'i+1' zleceń.
            # dp[i+1] to maksymalny zysk po rozważeniu (i+1)-tego zlecenia.
            dp[i+1] = max(profit_without_current, profit_with_current)
            
        # 5. Ostatecznym wynikiem jest ostatnia wartość w tablicy DP.
        return dp[-1]
        
        
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not (startTime or endTime or profit):
            return 0
        
        m, n, b = len(startTime), len(endTime), len(profit)
        if m != n or m != b:
            return 0
        
        combined_list = []
        for i in range(m):
            combined_list.append((startTime[i], endTime[i], profit[i]))
        
        combined_list.sort(key=lambda x: x[1])

        sorted_end_times = [job[1] for job in combined_list]
        dp = [0] * (m + 1)
        
        for i in range(n):
            current_start_time = combined_list[i][0]
            current_end_time = combined_list[i][1]
            current_profit = combined_list[i][2]
            
            profit_without_current = dp[i]
            prev_job_dp_index = bisect.bisect_right(sorted_end_times, current_start_time)
            profit_from_previous_non_conflicting_jobs = dp[prev_job_dp_index]
            
            profit_with_current = current_profit + profit_from_previous_non_conflicting_jobs
            dp[i+1] = max(profit_without_current, profit_with_current)
            
        return dp[-1]
    
    
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not (startTime or endTime or profit):
            return 0
        m = len(startTime)
        combined = []
        for i in range(m):
            combined.append((startTime[i], endTime[i], profit[i]))
        
        combined.sort(key=lambda x: x[1])
        sorted_end_times = [jobs[1] for jobs in combined]
        
        dp = [0] * (m + 1)
        
        for i in range(m):
            current_start_time = combined[i][0]
            current_end_time = combined[i][1]
            current_profit = combined[i][2]
            
            profit_without_current = dp[i]
            prev_job_dp_index = bisect.bisect_right(sorted_end_times, current_start_time)
            profit_from_previous_non_conflicting_jobs = dp[prev_job_dp_index]
            
            profit_with_current = current_profit + profit_from_previous_non_conflicting_jobs
            dp[i + 1] = max(profit_without_current, profit_with_current)
        return dp[-1]
    
    
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not (startTime or endTime or profit):
            return 0
        
        m = len(startTime)
        combined = []
        for i in range(m):
            combined.append((startTime[i], endTime[i], profit[i]))
            
        end_time_sorted = [job[1] for job in combined]
        dp = [0] * (m + 1)
        
        for i in range(m):
            current_start_time = combined[i][0]
            current_end_time = combined[i][1]
            current_profit = combined[i][2]
            
            profit_without_current = dp[i]
            prev_job_dp_idnex = bisect.bisect_right(end_time_sorted, current_start_time)
            profit_from_previous_non_conflicting_jobs = dp[prev_job_dp_idnex]
            dp[i + 1] = max(profit_without_current, profit_from_previous_non_conflicting_jobs + current_profit)
        return dp[-1]
    

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not (startTime or endTime or profit):
            return 0
        
        m = len(startTime)
        combined = [(startTime[i], endTime[i], profit[i]) for i in range(m)]
        sorted_end_time = [job[1] for job in combined]
        dp = [0] * (m + 1)
        
        for i in range(m):
            current_start_time = combined[i][0]
            current_end_time = combined[i][1]
            current_profit = combined[i][2]
            
            profit_without_current = dp[i]
            prev_job_dp_index = bisect.bisect_right(sorted_end_time, current_start_time)
            dp[i + 1] = max(profit_without_current, dp[prev_job_dp_index] + current_profit)
        return dp[-1]




class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        m = len(startTime)
        combined = [(startTime[i], endTime[i], profit[i]) for i in range(m)]
        combined.sort(key=lambda x: x[1])
        sorted_end_time = [job[1] for job in combined]
        dp = [0] * (m + 1)
        
        for i in range(m):
            current_start_time = combined[i][0]
            current_profit = combined[i][2]
            
            profit_without_current = dp[i]
            prev_index = bisect.bisect_right(sorted_end_time, current_start_time)
            cc = (dp[prev_index] + current_profit)
            dp[i + 1] = max(profit_without_current, cc)
        return dp[-1]
    








class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        m = len(startTime)
        comb = [(startTime[i], endTime[i], profit[i]) for i in range(m)]
        comb.sort(key=lambda x : x[1])
        end_sorted = [job[1] for job in comb]
        
        dp = [0] * (m + 1)
        
        for i in range(m):
            curr_start = comb[i][0]
            curr_prof = comb[i][2]
            
            prof_without_curr = dp[i]
            prev_index = bisect.bisect_right(end_sorted, curr_start)
            dp[i+1] = max(prof_without_curr, curr_prof + dp[prev_index])
        return dp[-1]