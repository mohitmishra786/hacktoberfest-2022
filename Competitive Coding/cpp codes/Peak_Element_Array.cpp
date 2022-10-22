#include<bits/stdc++.h>
using namespace std;

int findPeakElement(vector<int>& nums) {
        int lmax = 0,ct=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]>nums[lmax]) lmax = i;
        }
        return max;
    }
int main(){
  int sz;
  cin>>sz;
  vector<int> ls;
  for(int i=0;i<sz;i++)
    {
        int a;    
        cin>>a;
        ls.push_back(a);
    }
  int peak = findPeakElement(ls);
  cout<<peak<<endl;
  return 0;
}
