#include <iostream>
using namespace std;



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int n;
    cin>>n;

    while(n--){
        char s;
        cin>>s;

        if(s=='B' || s=='b'){
            cout<<"BattleShip"<<endl;
        }else if(s=='C' || s=='c'){
            cout<<"Cruiser"<<endl;
        }else if(s=='D' || s=='d'){
            cout<<"Destroyer"<<endl;
        }else{
            cout<<"Frigate"<<endl;
        }
    }

    return 0;
}