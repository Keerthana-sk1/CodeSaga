def reverse_only_alpha(s):
    s = list(s)
    newchars = [c for c in s if c.isalpha()]
    #newchars.reverse()
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = newchars.pop()
    return ''.join(s)
