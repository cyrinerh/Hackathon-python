def overlapping(L,K):
    for i in L:
            for j in K:
                if(i == j):
                    return True
    return False
                
