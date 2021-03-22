def join(lst):
    lsts = [ [i] for i in lst]
    num = 0
    test1 = []
    test2= []
    test3 = []
    test4 = []
    test5 = []
    try:
        for i in range(len(lsts)):
            
            for j in lsts[i]:
                for k in j:
                    if str(test1) in lst[i + 1]:
                        test2.append(j[:num])
                        #print(lst[i + 1])
                    else:
                        num += 1
                        test1 = j[num: ]
        
    
    except IndexError:
        for i in test2:
            if not i in test3:
                test3.append(i)
        lst6 = []
        test5 = lst6
        def test(mini_lst):
            number = 0
            
            try:
                for i in range(len(mini_lst)):
                    base = mini_lst[i]
                    next_one = mini_lst[i + 1]
                    
                    for j in range(len(mini_lst[i])): 
                        if base[-1] == next_one[0]:
                            base_updated = base[:-1]
                            end_updated = next_one
                            if not base_updated in lst6: 
                                lst6.append(base_updated)
                            if not end_updated in lst6:
                                lst6.append(end_updated)
                            else:
                                continue
                            #print(True)
                        else:
                            lst6.append(mini_lst[i])
            except IndexError:
                None


        
        try:
            for i in range(len(test3)):
                test_base = test3[i]
                next_test = test3[i + 1]
                for j in range(len(test3[i])):
                    if test_base[-1] == next_test[0]:
                        update = test(test3)
                        break
                    else:
                        continue
        except IndexError:
            None
        

       
       
        for l in test3:
            for j in range(len(l)):
                None
                    
    
        if len(lst6) > 0:
            string_test = "" 
            for i in lst6: 
                string_test += i
            
            last_string_updated = ""
            for i in range(len(lst[-1])):
                if i != 0:
                    last_string_updated += lst[-1][i]
            
            string_test_updated = string_test + last_string_updated
        else:
            string_test = "" 
            for i in test3: 
                string_test += i
            
            last_string_updated = ""
            for i in range(len(lst[-1])):
                if i != 0:
                    last_string_updated += lst[-1][i]
            
            string_test_updated = string_test + last_string_updated
        
        
        return string_test_updated
        
        
        

    
     
    


    
            
   
    

    
    


print(join(["to", "ops", "psy", "syllable"]))
#print(join(["move", "over", "very"]))