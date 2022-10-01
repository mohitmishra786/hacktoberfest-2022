//70. Climbing Stairs
//Leetcode Easy DP
class Solution {
public:
    //Top down approach
    int totalWays(int n,vector<int>&dp){
        if(n==0){
            return 1;
        }
        if(dp[n]!=0){
            return dp[n];
        }
        int ways=0;
        for(int i=1;i<=2;i++){
            if(n-i>=0){
                ways +=totalWays(n-i,dp);
            }
        }
        return dp[n]= ways;
    }
    
    //Bottom Up approach
    int totalWaysBU(int n){
        vector<int>dp(n+1,0);
        dp[0]=1;
        for(int i=1;i<=n;i++){
            int ways=0;
            for(int steps =1;steps<=2;steps++){
                //we can take atmost 2 steps back
                if(i-steps>=0){
                    ways+=dp[i-steps];
                }
            }
            dp[i]= ways;
        }
        return dp[n];
    }
    
    int climbStairs(int n) {
        vector<int>dp(n+1,0);
        return totalWaysBU(n);
    }
};