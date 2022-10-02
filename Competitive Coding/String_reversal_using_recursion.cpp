// Program to reverse a string using recursion
#include<iostream>
using namespace std;

void reverse(int index, int len, string input, string output) {
    // Base case :  
    //if we reach the midpoint of the string then
    // stop the recursion
    if (index >= (len/2)) {
        output = input;
        return;
    }
    
    // swap current character with corresponding mirror index in 2nd half
    swap(output[index], output[len-index-1]);
    
    // call recursively for the next index
    reverse(index+1, len, input, output);
}

int main() {
    string input, output;
    
    // input string
    cin>>input;
    
    // invoke reverse function 
    reverse(0, s.size(), s, output);
    
    // reversed output string
    cout<<output<<"\n";
}
