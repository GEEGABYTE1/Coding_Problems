def test(mini_lst):
    number = 0
    lst6 = []
    try:
        for i in range(len(mini_lst)):
            base = mini_lst[i]
            next_one = mini_lst[i + 1]
            
            for j in range(len(mini_lst[i])): 
                if base[-1] == next_one[0]:
                    base_updated = base[:1]
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
        return lst6




print(test(['t', 'op', 'ps']))
