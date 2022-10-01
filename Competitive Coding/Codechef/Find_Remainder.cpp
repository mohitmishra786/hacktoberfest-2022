#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;



int main() {
ios_base::sync_with_stdio(0);
cin.tie(0);

    int n;
    cin>>n;
    while(n--){
        pair<ll,ll> rem;
        
        cin>>rem.first>>rem.second;

        cout<<rem.first % rem.second<<endl;
    }

    return 0;
}