def tree_sum(numbers):
    numbers.sort()
    n = len(numbers)
    list_of_list: list[list[int]] = []
    
    for i in range(n-2):
        if numbers[i] > 0 and numbers[i] == numbers[i-1]:
            continue
        
        target = - numbers[i]
        
        left_site, right_site = i + 1, n-1
        while left_site < right_site:
            sum = numbers[left_site] + numbers[right_site]
            
            if sum == target:
                list_of_list.append([numbers[i], numbers[left_site], numbers[right_site]])
                
                left_value = numbers[left_site]
                while left_site < right_site and numbers[left_site] == left_value:
                    left_site += 1

                right_value = numbers[right_site]
                while left_site < right_site and numbers[right_site] == right_value:
                    right_site -= 1
                    
            elif sum < target:
                left_site +=1
            else:
                right_site -= 1
                
    return list_of_list