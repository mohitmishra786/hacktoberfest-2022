#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin>>t;

    for(int i=1; i<=t; i++){
        ll bags,children;
        ll totalCandies = 0;
        cin>>bags>>children;
        while(bags--){
            ll candy;
            cin>>candy;
            totalCandies+=candy;
        }

        cout<<"Case #"<<i<<": "<<totalCandies % children<<endl;
    }

    return 0;
}