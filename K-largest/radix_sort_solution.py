def radix_sort(lst):
    max_value = max(lst)
    max_exponent = len(str(max_value))
    being_sorted = lst[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position 
        digits = [ [] for i in range(10)]

        for number in being_sorted:
            string_number = str(number)
            try:
                digit = string_number[index]
            except IndexError:
                digit = 0 
            
            digit = int(digit)
            digits[digit].append(number)
            being_sorted = []
            for numeral in digits:
                being_sorted.extend(numeral)
            print(digits)
            print()
            print(being_sorted)
            print()
    
    return being_sorted 


def firstKelements(arr, size, k):
    arr = radix_sort(arr)
    if len(arr) > size:
        return None 
    else:
        k_lst = arr[:k]
        return k_lst

lst = [9, 8, 7, 5, 6]

print(firstKelements(lst, len(lst), 2))

