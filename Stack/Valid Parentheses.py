class Solution:
    def isValid(self, s: str) -> bool:
        ss = { 
            '(': ')', 
            '{': '}', 
            '[': ']'
        }
        list_of_looking_char = []
        for char in s:
            if char in ss:
                # print(char)
                list_of_looking_char.append(ss[char])
                # print(list_of_looking_char)
            else:
                if len(list_of_looking_char) >= 1 and char == list_of_looking_char[-1]:
                    list_of_looking_char.pop()
                else:
                    return False
        if not list_of_looking_char:
            return True
        return False