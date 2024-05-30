def is_anagram(str1, str2):
    ## fill this in
    str1=str1.lower()
    str2=str2.lower()
    if len(str1)!=len(str2):
      return False
    else:
      char_count={}
      for char in str1:
        char_count[char]=char_count.get(char,0)+1
      for char in str2:
        if char not in char_count or char_count[char]==0:
          return False
        else:
          char_count[char]-=1
    return all(count==0 for count in char_count.values())
