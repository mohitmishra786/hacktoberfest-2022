#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;


int whichElevator(int firstPosition, int secondLeaving, int secondDestination);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll t;
    cin>>t;
    while(t--){
        ll a,b,c;
        cin>>a>>b>>c;

        cout<<whichElevator(a,b,c)<<endl;
    }

    return 0;
}


int whichElevator(int firstPosition, int secondLeaving, int secondDestination){
    int t1 = 0;
    int t2 = 0;

    if(firstPosition != 1){
        t1 = firstPosition-1;
    }

    if(secondLeaving<secondDestination && secondLeaving!=secondDestination){
        t2 = (secondDestination-secondLeaving) + (secondDestination-1);
    }
    else{
        t2 = secondDestination-1;
    }
    
    
    if(t1 == t2){
        return 3;
    }
    else if(t1<t2){
        return 1;
    }else{
        return 2;
    }
}