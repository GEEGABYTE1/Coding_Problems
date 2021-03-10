def test(lst):
    dictionary = {}
    for i in range(len(lst)):
        try:
            if lst[i] % 2 == 0 and lst[i + 1] % 2 == 1:
                pass

            elif lst[i] % 2 == 1 and lst[i+ 1] % 2 ==0:
                pass

            elif lst[i] % 2 == 0 and lst[i+1] % 2 == 0:
                current = lst[i + 1]
                string_current = str(current)

                even_checker = []
                for o in string_current:
                    if int(o) % 2 == 0:
                        even_checker.append(o)
                    else:
                        continue
                
                if len(even_checker) == len(string_current):
                    print(-1)
                    break
                else:
                    new_current = None
                    for j in string_current:
                        if int(string_current[-1]) % 2 != 1:
                            end = string_current[-1:]
                            start = string_current[:-1]
                            new_string = end + start 
                            string_current = new_string
                        else:
                            dictionary[str(i + 1)] = int(string_current)
                            lst[i + 1] = int(string_current)
                            break
                
            elif lst[i] % 2 == 1 and lst[i+1] % 2 == 1:
                current = lst[i + 1]
                string_current = str(current)

                odd_checker = []
                for v in string_current:
                    if int(v) % 2 == 1:
                        odd_checker.append(v)
                    else:
                        continue
                
                if len(odd_checker) == len(string_current):
                    print(-1)
                    break
                else:
                    new_current = None 
                    for k in string_current:
                        if int(string_current[-1]) % 2 != 0:
                            end = string_current[-1:]
                            start = string_current[:-1]
                            new_string = end + start 
                            string_current = new_string 
                        else:
                            dictionary[str(i + 1)] = int(string_current)
                            lst[i + 1] = int(string_current)
                            break
        except IndexError:
            return lst

    
    
     
        




print(test([143, 251, 534, 232, 854]))


            
                