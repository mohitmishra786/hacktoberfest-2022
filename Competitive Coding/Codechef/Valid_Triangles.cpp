#include <iostream>
#include <vector>
using namespace std;



int main() {

    int n;
    cin>>n;

    while(n--){
        int angleA,angleB,angleC;
        cin>>angleA>>angleB>>angleC;
        int sum = angleA + angleB + angleC;
        if(sum >180 || sum<180){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
        }
    }

    return 0;
}