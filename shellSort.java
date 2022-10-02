## Shell sort

import java.util.*;  
class ShellSort{  
    public static void main(String[]args){  
  
        Scanner sc = new Scanner(System.in);  
  
  System.out.println("Enter the size of an array: ");  
  int n = sc.nextInt();  
  
  // Taking input elements in array  
  
  int []arr = new int[n];  
  System.out.println("Enter "+n+" element: ");  
  for(int i=0; i<n; i++) {  
            arr[i] = sc.nextInt();  
  }  
  
        shellSort(arr);  
  
  // Printing the elements of the array  
  for (int j : arr) {  
            System.out.print(j + ", ");  
  }  
    }  
    public static void shellSort(int arr[]) {  
        int n = arr.length;  
  // Start with a big gap, then reduce the gap  
  for (int gap = n / 2; gap > 0; gap /= 2) {  
            for (int i = gap; i < n; i++) {  
                int temp = arr[i];  
  int j = i;  
  while (j >= gap && arr[j-gap] > temp) {  
                    arr[j] = arr[j-gap];  
  j -= gap;  
  }  
                arr[j] = temp;  
  }  
        }  
    }  
}
