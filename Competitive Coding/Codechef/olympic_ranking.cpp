#include<iostream>
using namespace std;

int main(){
    // #ifndef ONLINE_JUDGE
	// 	freopen("input.txt","r",stdin);
	// 	freopen("output.txt","w",stdout);
    // #endif
    int t;
    for(int i=0;i<t;i++){
        int a[6];
        int m,n;
        for(int j=0;j<6;j++){
            cin>>a[i];
        }
        m = a[0]+a[1]+a[2];
        n = a[3]+a[4]+a[5];

        if(m>n) cout<<"1";
        else cout<<"2";
    }

    return 0;
}