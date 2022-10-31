#include<bits/stdc++.h>
using namespace std;
int minOf3(int x,int y,int z)
{
	return min(x,min(y,z));
}
int editDistance(string s1,string s2,int m,int n,vector<vector<int> >& dp)
{
	if(n==0)
	return m;
	if(m==0)
	return n;
	if(dp[m][n]!=-1)
	return dp[m][n];
	if(s1[m-1]==s2[n-1])
	{
		if(dp[m-1][n-1]==-1)
		return editDistance(s1,s2,m-1,n-1,dp);
		else 
		dp[m][n]=dp[m-1][n-1];
	}
	else 
	{
		int m1,m2,m3;
		if(dp[m][n-1]==-1)
		m1=editDistance(s1,s2,m,n-1,dp);//insert
		else
		m1=dp[m][n-1];
		if(dp[m-1][n]==-1)
		m2=editDistance(s1,s2,m-1,n,dp);//remove
		else 
		m2=dp[m-1][n];
		if(dp[m-1][n-1]==-1)
		m3=editDistance(s1,s2,m-1,n-1,dp);//replace
		else
		m3=dp[m-1][n-1];
		return 1+minOf3(m1,m2,m3);
	}
}
int main()
{
	string s1,s2;
	cin>>s1>>s2;
	int m=s1.size();
	int n=s2.size();
	vector<vector<int> >dp(m+1,vector<int>(n+1,-1));
int ans=editDistance(s1,s2,m,n,dp);
	cout<<ans<<" ";
	return 0;
}
