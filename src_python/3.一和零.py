def double(wt,val,W,N):
    
    '''
    首先状态转移方程就是说选或者不选，选的话，
    说明当前质量中，有了当前的物品，所以价值等于
    去掉当前重量的背包能装的最大价值，如果不选，
    那就是说明装这个得不偿失，中间有一些选择可以
    '''
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            if i-wt[j-1]>=0:
                dp[i,j] = max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][W]


print(double([2,1,3],[4,2,3],4,3))