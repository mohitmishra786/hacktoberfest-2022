#include<bits/stdc++.h>
using namespace std;

int pref(string &b, int start, int end){
    int sum = 0;
    
    if(start<=end){
        for(int i=start; i<=end; i++){
            sum += b[i] - '0';
        }
    }
    
    
    return sum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	// your code goes here
	int t;
	cin>>t;
	
	while(t--){
	    int n;
	    int m;
	    cin>>n;
	    cin>>m;
	    
	    string a;
	    string b = "";
	    
	    cin>>a;
	    
	    while(m--){
	        b += a;
	    }
	    int count = 0;
	    for(int i=0; i<b.size(); i++){
	        int n = pref(b,0,i);
	        int m = pref(b,i+1, b.size()-1);
	        
	        if(n==m){
	            count++;
	        }
	    }
	    
	    cout<<count<<endl;
	    
	}
	
	return 0;
}
