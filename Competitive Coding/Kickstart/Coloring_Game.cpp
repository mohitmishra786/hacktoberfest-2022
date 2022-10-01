#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;


int solve(int n){

    return ceil(n/5.0);
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin>>t;
    int i=1;
    while(i<=t){
        int n;
        cin>>n;
        int ans = solve(n);
        cout<<"Case #"<<i<<": "<<ans<<endl;
        i++;
    }

    return 0;
}