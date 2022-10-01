#include <iostream>
using namespace std;

int beauty(int colors){
    int b = 1;

    for(int i=2; i<=colors; i++){
        if(i%2==0){
            b ^= i;
        }
        else{
            b &= i;
        }
    }

    return b;
}

int main() {

    int t;
    cin>>t;

    for(int i=0; i<t; i++){
        int colors;
        cin>>colors;
        cout<<beauty(colors)<<endl;
    }

    return 0;
}