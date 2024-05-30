def majority_element(nums):
    # fill in
    freq_count={}
    for i in nums:
      freq_count[i]=freq_count.get(i,0)+1
    l=len(nums)//2
    for num, count in freq_count.items():
      if count > l:
        return num
