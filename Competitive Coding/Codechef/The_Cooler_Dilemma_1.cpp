#include <iostream>
using namespace std;



int main() {

    int t;
    cin>>t;
    for(int i=0; i<t; i++){
        int rent,price,month;
        cin>>rent>>price>>month;
        int rentPrice = rent*month;

        if(rentPrice < price){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }

    return 0;
}