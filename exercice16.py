def word_to_len(words):
    a=[]
    for el in words:
        a=a+[len(el)]
    return a
def filter_long_words(l,n):
    l2=word_to_len(l)
    a=[]
    for i in range(len(l2)):
        if l2[i] > n :
            a=a+[l[i]]
    return a
           
