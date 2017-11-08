def is_palindrome(text):
    l=list(text)
    j=len(l)-1
    for i in range(len(l)//2):
        if l[i] != l[j] :
            return False
        else :
            j=j-1
    return True
        
    
    
