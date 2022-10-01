//509. Fibonacci Number
//Leetcode Easy DP

class Solution {
public:

    int fibRec(int n){
        if(n==0 || n==1){
            return n;
        }
        return fibRec(n-1)+fibRec(n-2);
    }

    int fibTopDown(int n,vector<int>&dp){
        if(n==0 || n==1){
            return n;
        }
        if(dp[n]!=0){
            return dp[n];
        }
        return dp[n]= fibTopDown(n-1,dp)+ fibTopDown(n-2,dp);
    }

    int fibBottomUp(int n){
        if(n==1 || n==0){
            return n;
        }
        vector<int>dp(n+1,0);
        dp[1]=1;
        for(int i=2;i<=n;i++){
            dp[i]= dp[i-1]+dp[i-2];
        }
        return dp[n];
    }

    int fibSpaceOpt(int n){
        if(n==0 || n==1){
            return n;
        }
        int a = 0;
        int b = 1;
        int c = a+b;
        for(int i=2;i<=n;i++){
            c= a+b;
            a = b;
            b = c;
        }
        return c;
    }

    
    int fib(int n) {
        return fibSpaceOpt(n);
    }
};