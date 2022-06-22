//How to Insert an element at a specific position in an Array in C++

//Difficulty Level : Easy
//Last Updated : 21 Jun, 2022

// An array is a collection of items stored at contiguous memory locations. 
// In this article, we will see how to insert an element in an array in C++.
// Given an array arr of size n, this article tells how to insert an element x in this array arr at a specific position.  
// Approach: Here’s how to do it.
// source : https://www.geeksforgeeks.org/how-to-insert-an-element-at-a-specific-position-in-an-array-in-c/

// Algorithm : 
//First get the element to be inserted, say x
//Then get the position at which this element is to be inserted, say position
//Then shift the array elements from this position to one position forward, and do this for all the other elements next to position.
//Insert the element x now at the position position, as this is now empty.
//Below is the implementation of the above approach: 


// C++ Program to Insert an element
// at a specific position in an Array
 
#include <iostream>
using namespace std;
 
// Function to insert element in number_array at position position
int* insertElement(int n, int number_array[], int element, int position)
{
    int i;
 
    // increase the size by 1
    n++;
 
    // shift elements forward
    for (i = n; i >= position; i--)
        number_array[i] = number_array[i - 1];
 
    // insert element at position
    number_array[position - 1] = element;
 
    return number_array;
}
 
// Driver Code
int main()
{
	// Assigning zerores at all the indices of the array
    int number_array[100] = { 0 };
    
    for(int i=0; i<100; i++){
    	cout << number_array[i] << endl;
	}
    
    
    int element, position, array_size = 10;
 
    // initial array of size 10
    for (int i = 0; i < array_size; i++)
        number_array[i] = i + 1;
 
    // print the original array
    for (int i = 0; i < array_size; i++)
        cout << number_array[i] << " ";
    cout << endl;
 
	cout << "Please provide the element that you want to insert into the array : " << endl;
    // element to be inserted
    cin >> element;
 
 	cout << "Please provide the position where you want to insert into the array : " << endl;
    // position at which element is to be inserted
    cin >> position;
 
    // Insert element at position
    insertElement(array_size, number_array, element, position);
 
    // print the updated array
    for (int i = 0; i < array_size + 1; i++)
        cout << number_array[i] << " ";
    cout << endl;
 
    return 0;
}