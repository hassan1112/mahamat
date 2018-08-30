 //input an array
// call bubble sort algorithm to sort the elements 
//output position of the target element
//Purpose: Binary Search returns the index of the value to find within the array
//Time complexity: O(logn) due to logn comparisons in the worst case
//Space complexity: O(1) since it does not use any auxiliary space


/*
//Recursive algorithm 
algorithm  binarySearch(int arr[], int n, int key)
{
	if(low ==high)
	{
		if(key ==a[low])
		return low;
		else
		return -1;
    }
 else
 {
		mid = (low+hight)/2;
		if(key==arr[mid])
		return mid;
		else 
		if(key <a[mid])
		return binnsearch(a,low,mid-1,key)
		else
		return binsearch(a,mid+1,high,key)
 }
}


*/

/*

//iterative algorithm 
algorithm  binarySearch(int arr[], int n, int key)
{
	low = 0,high = n - 1;

    while (low < high) {
        int   = low + (high - low) / 2;

        if (arr[mid] == key) {
            return mid;
        } else if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return arr[low] == key ? low : -1;
}
*/
#include <iostream>
using namespace std;

//insertion sort method 
 class Binaryseach{

public : void insertion(int a[10]){
for (int i = 0; i < 10; i++)

    {
	for (int j = i; j >= 1; j--)
		{
			if (a[j] < a[j-1])

            {
				int temp = a[j];
				a[j] = a[j-1];
				a[j-1] = temp;
			}
			else
			break;
        }

    }
}
//recursive binary search method
int binary_search(int array[], int key, int low, int high){

    int middle = (low + high)/2;

    if(low > high){
        return -1;
    }
    if(array[middle] == key){
        return middle+1;
    }
    else if(array[middle] < key){
        return binary_search(array, key, middle + 1, high);
    }
    else{ //if(array[middle] > key)
        return binary_search(array, key, low, middle - 1);
    }
}


// A iterative binary search function. 
//It returns location of x in given array arr[l..n] if present,
// otherwise -1
int binarySearch(int arr[], int l, int h, int x)
{
    while (l <= h)
    {
        int m = l + (h-l)/2;
 
        // Check if x is present at mid
        if (arr[m] == x)
            return m+1;
 
        // If x greater, ignore left half
        if (arr[m] < x)
            l = m + 1;
 
        // If x is smaller, ignore right half
        else
            h = m - 1;
    }
}

};

int main()
{
	int array[10];
	int key;
	int low = 0;
	int high = sizeof(array)/ sizeof(array[0]);
	int choice ;
	char confirm;
	
	//creating object to access the member functions of Binaryseach
	Binaryseach  a;
	cout<<"\t Name : MAHAMAT HASSAN \t\t USN:17MSRIT003 \t\t Subject :ADA \n\n";
	cout<<"\t\t C++ program to implement recurisve and iterative Binary Search"<<endl;
	cout<<"Enter 10 array elements "<<endl;
	for(int i =0;i<10;i++)
	{
		cin>>array[i];
	}
	
	cout<<"\nBefore sorting  an array contains\n\n";
	for(int i=0;i<10;i++)
	{
	  cout<<array[i]<<" ";
	}
		
	cout<<"\n\n After calling bubblesort(arr) method\n\n"<<endl;
	a.insertion(array);
	for(int i=0;i<10;i++)
	{
	  cout<<array[i]<<" ";
	}
		
	cout<<"\n\n";
		cout<<"\t\t\t\t MENU ";
	cout<<"\n \t\t\t 1.Recursive method of Binary Search"<<endl;
	cout<<"\t\t\t 2.Iterative method of Binary Search"<<endl;
    cout<<"\t\t\t 3.press 3  to exit\n"<<endl;	
		do
		{
			cout<<"\n Enter your choice"<<endl;
		    cin>>choice;
		
		    switch(choice)
			{
				case 1:
					{
										
							cout<<"\n\n \t\t Implmentation  of recursive Binary search \n";
						cout<<"\t\t Enter the element to be searched "<<endl;
					    cin>>key;
					     int index = a.binary_search(array, key, low, high-1);
					    if(index >0)
					    {
					    cout <<key<<"\t is found at position \t"<<index << endl;
					    cout<<"\t\t Dont panic its humanly correct as  human always starts counting from 1  unlike computer from 0";
						}
						else 
						{
						cout<<"\t Element is not found in the list\n";
						
						}
						break;
					}
		       case 2:
					{   
						
						cout<<"\n\n Implmentation  of iterative Binary Search \n";
					   cout<<"Enter the element to be searched \n"<<endl;
					   cin>>key;
					    int result = a.binarySearch(array, 0,high-1, key);
					    if(result >0)
					    {
					    cout <<key<<"\t is found at position \t"<<result << endl;
					    cout<<"\t\t Dont panic its humanly correct as  human always starts counting from 1  unlike computer from 0";
						}
						else 
						{
						cout<<key<<"\t WElement is not found in the list\n";
						
						}
				    }
							break;
			    default:
						cout<<"\t\t Invalid input";
				 
			}
		cout<<"\n\n Do you want to continue searching [y|n]?";
		cin>>confirm; 
	   }while(confirm=='y');
	
}
	
	    
