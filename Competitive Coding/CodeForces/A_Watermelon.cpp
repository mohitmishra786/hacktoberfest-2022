#include <iostream>
using namespace std;

string check(int n){
    if(n>2 && n%2==0) return "YES";

    return "NO";
}

int main() {

    int n;
    cin>>n;

    cout<<check(n);

    return 0;
}