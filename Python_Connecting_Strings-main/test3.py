def join(lst):
    count = 0
    while count != len(lst):
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
                num = 0
                num1 = 0
                try:
                    for i in range(len(mini_lst)):
                        base = mini_lst[i]
                        next_one = mini_lst[i + 1]
                        number = 0
                        number1 = 0
                        
                        for j in range(len(mini_lst[i])): 
                            if base[num:] == next_one[:num1]:
                                base_updated = base[num:]
                                end_updated = next_one
                                if not base_updated in lst6: 
                                    lst6.append(base_updated)
                                if not end_updated in lst6:
                                    lst6.append(end_updated)
                                else:
                                    num -= 1
                                    num1 += 1
                                    continue
                                #print(True)
                            else:
                                lst6.append(mini_lst[i])
                except IndexError:
                    None


            
            try:
                number = 0
                number1 = 0
                test7 = []
                lst_updated = []
                for i in range(len(test3)):
                    number = 0
                    number1 = 0
                    test_base = test3[i]
                    next_test = test3[i + 1]
                    for j in range(len(test3[i])):
                        if test_base[number:] == next_test[:number1]:
                            print(True)
                            for k in test3:
                                if k == next_test:
                                    lst_updated.append(next_test[number1:])
                                else:
                                    lst_updated.append(k)
                            #update = test(test3)
                            
                            
                            
                        else:
                            number -= 1
                            number1 += 1
                            continue
                        print(test7)
            except IndexError:
                string = ""
                for i in lst_updated:
                    string += i 
                print(string)
                count += 1
                

print(join(["abcde", "bcdefghi", "efghi", "fghij", "ghijklmnop"]))
print(join(["happy", "python", "honey", "yelp", "plank", "lanky"]))