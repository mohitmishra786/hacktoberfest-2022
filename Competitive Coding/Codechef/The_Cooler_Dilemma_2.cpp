#include <iostream>
using namespace std;



int main() {

    int t;
    cin>>t;
    for(int i=0; i<t; i++){
        int rent,price;
        cin>>rent>>price;
        if(price%rent == 0){
            price -= rent;
            cout<<price/rent<<endl;
        }
        else{
            cout<<price/rent<<endl;
        }
    }

    return 0;
}