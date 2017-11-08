def max_in_list(l):
    l.sort()
    return l[len(l)-1]

def word_to_len(words):
    a=[]
    for el in words:
        a=a+[len(el)]
    return a
def find_longest_word(words):
    l=word_to_len(words)
    s=max_in_list(l)
    return s
    
