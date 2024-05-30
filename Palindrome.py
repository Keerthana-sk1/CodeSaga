def is_palindrome(s):
    # fill in
    #new_string = ''.join(c.lower() if c.isalpha() else c for c in s)
    str1 = ''.join(s.split())
    newstring=str1.lower()
    reversed_str=newstring[::-1]
    if newstring==reversed_str:
      return True
    else:
      return False
