def gcd(a, b, lst=None):
  if a == 1 or b == 1:
    return 1 
  elif lst == None:
    summation_one = str(a / b)
    summation_two = str(b / a)
    lst = [summation_one, summation_two]
  elif len(lst) == 0:
    return 1
  
  k = lst.pop()
    #summation_split = k.split(".")
  index = 0
  for i in range(len(k)):
    if k[i] == ".":
      index = i 
      break 
  actual_summation = k[index: ]
  counter = 0
  for j in actual_summation:
    if j == "0":
      counter += 1

  if counter == len(actual_summation) - 1:
    try:
      if k == summation_two:
        return a
    except UnboundLocalError:
        return b

  return gcd(a, b, lst)
  

print(gcd(4, 2))




