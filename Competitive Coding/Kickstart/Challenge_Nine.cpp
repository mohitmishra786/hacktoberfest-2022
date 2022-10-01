#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

void challengeNine(string &N){
    int rem = 0;
    string ans = "";
    for(auto i:N){
        rem = (rem + (i-'0'))%9;
    }
    if(rem == 0){
        ans += N.substr(0,1);
        ans += '0';
        ans += N.substr(1);
    }
    else{
        for(int i=0; i<N.size(); i++){
            if(N[i] > ('0' - rem)){
                ans += N.substr(0, i);
                ans += '0' + rem;
                ans += N.substr(i+1);
                break;
            }
        }
    }

    cout<<ans<<endl;

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin>>t;

    for(int i=1; i<=t; i++){
        string N;
        cin>>N;
        cout<<"Case #"<<i<<": ";
        challengeNine(N);
    }

    return 0;
}