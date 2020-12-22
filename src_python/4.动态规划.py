def knapsack(wt, val, W, N):
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(1, W+1):
            if w - wt[i-1] < 0:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w - wt[i-1]] + val[i-1], dp[i-1][w])
    return dp[N][W]


def onelist(wt,val,W,N):
    dp = [0 for _ in range(W+1)]
    for i in range(1,N+1):
        for w in range(W,wt[i-1]-1,-1):
            dp[w] = max(dp[w],dp[w-wt[i-1]]+val[i-1])
    return dp[W]




N = 6
W = 15
wt = [2, 1, 3,4,5,6]
val = [4, 2, 3,1,2,3]
print(knapsack(wt,val,W,N))
print(onelist(wt,val,W,N))