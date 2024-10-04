import numpy as np
def OSA(a: str, b: str)-> int:
    d = np.zeros((len(a)+1, len(b)+1))
    # return d.shape
    cost = 0
    for i in range (len(a)):
        d[i, 0] = i
    for j in range (len(b)):
        d[0,j] = j

    for i in range (len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                cost = 0
            else:
                cost += 1
            d[i, j] = min(d[i-1, j] + 1, # insertion
                          d[i, j-1] + 1, # substitution
                          d[i-1, j-1] + cost) # deletion
            if i > 1 and j > 1 and a[i] ==  b[j-1] and a[i-1] == b[j]:
                d[i, j] = min(d[i, j], d[i-2, j-2] + 1) # transposition
    return cost 
print(OSA('cd', 'abc'))
