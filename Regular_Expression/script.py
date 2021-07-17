class Solution:
    def isMatch(self, s, p):
        new_string = ""
        updated_string = ""
        for i in s:
            updated_string += i + " "

        s_split = updated_string.split(" ")
        s_split = s_split[:-1]
        new_character = None

        updated_p_string = ""
        for i in p:
            updated_p_string += i + " "
        
        updated_p_string_split = updated_p_string.split(" ")
        updated_p_string_split = updated_p_string_split[:-1]

        if len(s) < len(p):
            ref_counter = len(s) 
        
        counter = 0
        
        if len(p) < len(s):
            return False 
        else:
            for i in range(len(p)):
                
                if len(s) < len(p):
                    if counter == len(s):
                        break
                
                if new_character == True and p[i] == '*':
                    new_character = None 
                    continue 
                else:
                    counter += 1
                

                if i == 0 and p[i] == s[i]:
                    new_string += p[i]
        
                
                elif not p[i] in s_split and p[i] != '*' and p[i] != '.':
                    try:
                        if p[i + 1] == "*":
                            new_string += p[i]
                            new_string += "*"
                            new_character = True
                        else:
                            continue
                    except IndexError:
                        continue
                
                elif p[i] in s_split and p[i] != '*' and p[i] != '.':
                    try:
                        if p[i + 1] == "*":
                            letter_count = 0
                            letters = []
                            checker = False

                            for letter in s_split:
                                if letter == p[i]:
                                    letters.append(letter)
                            
                            if len(letters) > 0:
                                for idx in range(len(letters)):
                                    try:
                                        if letters[idx] == letters[idx + 1]:
                                            checker = True 
                                        else:
                                            continue 
                                    except IndexError:
                                        break
                            
                            if checker >= True:
                                new_string += p[i]
                                new_string += '*'
                                new_character = True 
                            else:
                                new_string += p[i]
                    except IndexError:
                        new_string += p[i]
                    


                elif p[i] == '*':
                    try:
                        if s[counter] == s[counter - 1]:
                            new_string += "*"
                        elif not s[counter] in updated_p_string_split:
                            new_string += '*'
                        else:
                            continue
                    except IndexError:
                        if s[counter - 1] == s[counter - 2]:
                            new_string += '*'
                        elif not s[counter - 1] in updated_p_string_split:
                            new_string += '*'
                        else:
                            continue 

                elif p[i] == '.':
                    new_string += '.'
                    
        if new_string == p:
            return True 
        else:
            return False
                    
            



# Test Cases

test = Solution()


