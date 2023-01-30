'''
An anagram of a string is another string that contains the same characters, 
only the order of characters can be different. 
For example, “abcd” and “dabc” are an anagram of each other.
'''

s1 = "listen"
s2 = "silent"

def check(s1, s2):
    if(sorted(s1) == sorted(s2)):
        print("The String are anagrams")
    else:
        print("The string aren't anagrams")
check(s1, s2)