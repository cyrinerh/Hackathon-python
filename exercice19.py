def test (dna):
    list_dna=list(dna)
    for i in range(len(list_dna)):
        if list_dna[i] in ['A','C','G','T','a','c','g','t']:
            t=True
        else :
            t=False
    return t


def check (dna):
    list_dna=list(dna)
    list_rna=[]
    for i in range(len(list_dna)) :
        if list_dna[i] == 'A' :
            list_rna = list_rna+[ 'U']
        elif list_dna[i] == 'C' :
            list_rna = list_rna+['G']
        elif list_dna[i] == 'G' :
            list_rna = list_rna +['C']
        else :
            list_rna = list_rna+['A']
    return list_rna
            

def dna_to_rna (dna) :
    if test(dna)==True:
        return check(dna)
    else:
        print('error')
        return ([])
        
    
    
    
    
