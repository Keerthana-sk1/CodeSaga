#code to find a number with a single occurence where all other numbers have double occurence in a list
def lonely_number(numbers):
    # fill in
    d={}
    for x in numbers:
      if x not in d:
        d[x]=1
      else:
        d[x]+=1
    for key,value in d.items():
      if value==1:
        return key
