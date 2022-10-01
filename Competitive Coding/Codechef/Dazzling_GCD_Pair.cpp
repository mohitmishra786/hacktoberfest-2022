#include <iostream>
#include<vector>
using namespace std;

int gcd(int a, int b){
    if(b==0){
        return a;
    }
    return gcd(b, a%b);
}

pair<int, int> gcdPair(int s, int e){
    pair<int, int> ans;
    ans.first = -1;
    ans.second = -1;
    for(int i=s;i<e;i++){
        for(int j=i+1; j<=e; j++){
            if(gcd(i,j)>1){
                ans.first = i;
                ans.second = j;
                return ans;
            }
        }
    }
    return ans;
}

int main() {

    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int start,end;
        cin>>start>>end;
        pair<int, int> a;
        a = gcdPair(start, end);
        if(a.first == -1){
            cout<<"-1"<<endl;
        }
        else{
            cout<<a.first<<" "<<a.second<<endl;
        }
    }

    return 0;
}