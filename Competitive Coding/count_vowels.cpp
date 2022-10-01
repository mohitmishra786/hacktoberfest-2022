#include <iostream>
#include <cctype>

using namespace std;

int main(){
	string s = "adbcjadfdak";
	int vowelsCount = 0;
	for(char i:s){
		i = tolower(i);
		if (i == 'a')
			vowelsCount++;
	}
	cout << "Vowels Count = " << vowelsCount << endl;
}