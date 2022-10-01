#include <iostream>
#include <cmath>
using namespace std;



int main() {

    unsigned long long n,m,a;
    cin>>n>>m>>a;

    // long long lr = 0;
    // while(n!=0){
    //     if(n>a){
    //         n = n-a;
    //         lr++;
    //     }
    //     if(n<a && n>0){
    //         n = 0;
    //         lr++;
    //     }
    // }

    // long long lc = 0;
    // while(m!=0){
    //     if(m>a){
    //         m = m-a;
    //         lc++;
    //     }
    //     if(m<a && m>0){
    //         m = 0;
    //         lc++;
    //     }
    // }
    // long long ans = lc*lr;
    // cout<<ans;

    unsigned long long ans = ceil((double)m/a) * ceil((double)n/a);

    cout<<ans;
    return 0;
}