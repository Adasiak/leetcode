def tree_sum(list_of_number):
    list_of_number.sort()
    n = len(list_of_number)
    list_of_list_to_response: list[list[int]]
    
    for i in range(n -2):
        if list_of_number[i] > 0 and list_of_number[i] == list_of_number[i-1]:
            continue
        
        target = - list_of_number[i]
        
        left, right = i +1, n-1
        while left < right:
            s = list_of_number[left] + list_of_number[right] 
            if s == target:
                list_of_list_to_response.append([list_of_number[i], list_of_number[left], list_of_number[right]])
            
                left_value = list_of_number[left]
                if left < right and left_value == list_of_number[left]:
                    left +=1
                
                right_value = list_of_number[right]
                if left < right and right_value == list_of_number[right]:
                    right -=1
            elif s < target:
                left +=1
            else:
                right -= 1
    return list_of_list_to_response    
            