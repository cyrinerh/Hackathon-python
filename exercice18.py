import string
def is_pangram (phrase) :
    phrase.lower()
    l=list(phrase)
    a=[]
    i=0
    for el in l:
        if el in string.ascii_lowercase :
            
            return True
    return False

def sum (l):
    s=0
    for el in l:
        if type(el) == int:
            s = s+ int(el)
    return s


def space(num):
    n=list(num)
    x=[]
    for el in n:
        if el != ' ' :
            x=x+[el]
    return x

def luhn ( num) :
    k=space(num)
    l=[]
    for i in range(len(k)):
        if i%2 == 0 :
            x=(int(k[i])*2)%9
            l.append(x)
        else :
            l.append(int(k[i]))
    print(l)
    for i in range(len(l)):
        s=sum(l)
    print('somme = ',s)
    if s % 2 == 0:
        print('nombre valid avec la formule de luhn')
    else :
        print('nombre invalid')
        














        
        
        
















        
        
            

