def pattern_search(text, pattern, case_sensitive=True):
  for index in range(len(text)):
    match_count = 0
    for char in range(len(pattern)): 
      if pattern[char] == text[index + char] and case_sensitive == True or pattern[char].lower() == text[index + char].lower() and case_sensitive==False:
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language")
pattern_search(friends_intro, "pylhon", False)
pattern_search(friends_intro, "idil", False)