import numpy as np
def DL_Distance(a: str, b: str, sigma: int)-> int:
    cost = 0
    da = np.zeros((sigma))
    d = np.zeros((len(a)+2, len(b)+2))

    max_dist = len(a) + len(b)
    d[-1, 1] = max_dist
    for i in range(0, len(a)):
        d[i, -1] = max_dist
        d[i, 0] = i
    for j in range(0, len(b)):
        d[-1, j] = max_dist
        d[0, j] = j
    
    for i in range (1, len(a)):
        db = 0
        for j in range(1, len(b)):
            k = da[b[j]]
            l = db
            if a[i] == b[j]:
                cost = 0
                db = j
            else:
                cost += 1
            d[i, j] = min(d[i-1, j-1] + cost, d[i, j-1] + 1, d[i-1, j] + 1, d[k-1, l-1] + (i-k-1) + 1 + (j - l - 1))
            da[a[i]] = i
    return cost

print(DL_Distance('dog', 'cat', 26))