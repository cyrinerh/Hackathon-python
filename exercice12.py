def generate_n_chars(n,c):
    a=''
    for i in range(int(n)):
        a=a+c
    return a
    
def histogram(list):
    for el in list:
        l=generate_n_chars(el,'*')
        print (l)
    
