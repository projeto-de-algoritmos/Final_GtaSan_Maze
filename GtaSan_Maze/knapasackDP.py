def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
wt = [1, 3, 4,2,5,6,7]
val = [1,15,25,16,9,3,7]
W = 23
n = len(val)
print(knapSack(W, wt, val, n))
 