#include <iostream>
using namespace std;

int binarySearch(int a[], int l, int r, int e)
{
	while (l <= r) 
    {
		int m = l + (r - l) / 2;

		if (a[m] == e)
        {
            return m;
        }
		if (a[m] < e)
        {
            l = m + 1;
        }
		else
        {
            r = m - 1;
        }
	}

	return -1;
}

int main(void)
{
    int n, e;

    cout<<"Enter number of elements in array:\n";
    cin>>n;

    cout<<"Enter elements in array:\n";

    int a[n];
    for(int i=0; i<n; i++)
    {
        cin>>a[i];
    }
	
    cout<<"Enter element to be found:\n";
    cin>>e;
	
	int found = binarySearch(a, 0, n - 1, e);
	
    if(found == -1)
    {
        cout<<"Element not found!\n";
    }
    else
    {
        cout<<"Element found at position: "<<found+1<<"\n";
    }
	return 0;
}
