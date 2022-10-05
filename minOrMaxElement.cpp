#include<iostream>
using namespace std;

int min(int a[], int n)
{
    int s=a[0];

    for(int i=1; i<n; i++)
    {
        if(a[i]<s)
        {
            s = a[i];
        }
    }

    return s;
}

int max(int a[], int n)
{
    int m=a[0];

    for(int i=1; i<n; i++)
    {
        if(a[i]>m)
        {
            m = a[i];
        }
    }

    return m;
}

int main()
{
    int n, c;

    cout<<"Enter size of array:\n";
    cin>>n;

    int a[n];

    cout<<"Enter elements in array:\n";

    for(int i=0; i<n; i++)
    {
        cin>>a[i];
    }

    cout<<"Enter 1 to find max element in array.\nEnter 2 to find min element in array.\n";
    cout<<"Enter your choice:\n";
    
    cin>>c;

    switch(c)
    {
        case 1:
            cout<<"Max element is: "<<max(a, n)<<"\n";
        break;
        case 2:
            cout<<"Min element is: "<<min(a, n)<<"\n";
        break;
        default:
            cout<<"Wrong choice!\n";
        break;
    }
    return 0;
}