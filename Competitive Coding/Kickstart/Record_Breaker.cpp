#include<bits/stdc++.h>
using namespace std;

int solve(vector<int> &v);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t,i;
    cin>>t;
    i=1;

    while(t--){

        int n;
        cin>>n;
        vector<int> v(n);

        for(int i=0; i<n; i++){
            cin>>v[i];
        }
        int ans = solve(v);

        cout<<"Case #"<<i<<": "<<ans<<endl;
        i++;
    }

    return 0;
}

int solve(vector<int> &v){
    int count = 0;

    int maxi = INT_MIN;
    for(int i = 0; i<v.size(); i++){
        if(i==v.size()-1){
            if(v[i] > maxi){
                count++;
            }
        }else if(v[i]>maxi){
            maxi = v[i];
            if(v[i]>v[i+1]){
                count++;
            }
        }
    }

    return count;
}