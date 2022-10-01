#include <iostream>
using namespace std;



int main() {

    int n;
    cin>>n;

    while(n--){
        long long a;
        cin>>a;
        int count = 0;
        while(a>0){
            int rem = a%10;
            a/=10;
            if(rem == 4){
                count++;
            }
        }
        cout<<count<<endl;
    }

    return 0;
}