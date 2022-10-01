#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

int counter(vector<ll> &v, ll k){
    ll count = 0;

    for(ll i=0; i<v.size(); i++){
        if(v[i]>=v[k-1]){
            if(v[k-1]==0 && v[i] != 0)
            count++;
        }
        else{
            break;
        }
    }

    return count;
}

int main() {

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    

    ll n;
    ll k;

    cin>>n>>k;

    vector <ll> v(n);

    for(int i=0; i<n; i++){
        cin>>v[i];
    }

    cout<<counter(v,k);

    return 0;
}