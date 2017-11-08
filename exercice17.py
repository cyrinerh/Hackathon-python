import string
def super_palindrome(phrase):
    phrase.lower()
    phrase2=''
    for k in phrase :
        if k in string.ascii_lowercase:
            phrase2=phrase2+k

    
    l=list(phrase2)
    j=len(l)-1
    print(l)
    
    for i in range(len(l)//2):
        if (l[i] != l[j]) :
            print (l[i],i,l[j])
            
            return False
        j=j-1
        
    return True
     
