def is_anagram(s1, s2):
    """check if anagrams

    s1: first word
    s2: second word

    returns: True if anagrams
    """
    if len(s1) != len(s2):
        print("Not anagrams")
    else:
        t1 = list(s1).sort()
        t2 = list(s2).sort()
        print(t1 == t2)
        return t1 == t2
    
#is_anagram("tap", "")
