#include<bits/stdc++.h>
using namespace std;

int speedTyping(string &I, string &P);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    
    int T;
    cin>>T;
    int count = 1;
    while(T--){
        string I,P;
        cin>>I>>P;
        
        int ans = speedTyping(I,P);
        
        if(ans >= 0){
            cout<<"Case #"<<count<<": "<<ans<<endl;
        }
        else{
            cout<<"Case #"<<count<<": "<<"IMPOSSIBLE"<<endl;
        }
        
        count++;
    }
    
    return 0;
}

int speedTyping(string &I, string &P){
    int sizeI = I.size();
    int sizeP = P.size();
    
    int ptrI = 0;
    int ptrP = 0;
    
    
    while(ptrI<sizeI && ptrP<sizeP){
        if(I[ptrI]==P[ptrP]){
            ptrI++;
            ptrP++;
        }
        else{
            ptrP++;
        }
    }
    
    if(ptrI == sizeI){
        return sizeP-sizeI;
    }
    
    return -1;
}