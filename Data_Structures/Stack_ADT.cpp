// https://www.geeksforgeeks.org/abstract-data-types/
// First study about what is an abstract data type

#include<iostream>
// What is an ADT?

//class StackADT{
//	void display_stack();
//	void insert_element();
//	void push_element();
//	int pop_element(int element);
//	void delete_element();
//};

void display_stack(int* stack, int stack_size){

	std :: cout << "Printing every value of the stack array :" << std :: endl;
	for(int array_index = 0; array_index < stack_size; array_index++)
	{
		std :: cout << stack[array_index];
	}

}

void insert_element_end(int* stack, int stack_size){
	
	int element;
	std :: cout << "Please specify the element that you want to insert at the end of the stack" << std :: endl;
	std :: cin >> element;
	
	std :: cout << "Stack First Element is :" << (int *)stack << std :: endl;
	std :: cout << "Stack second element is : " << (int *)stack+1 << std :: endl;
	
	std :: cout << "Stack size is :" << stack_size << std :: endl;
	std :: cout << "Element Insertion Successful " << std :: endl;
}

int main(){
	int stack[100];
	int input_variable;
	int stack_size;
	
	std :: cout << "To insert elements into your stack" << std :: endl;
	std :: cout << "Please specify your stack size : " << std :: endl;
	std :: cin >> stack_size;
	std :: cout << "This is your stack size : " << stack_size <<std :: endl; 
	
	std :: cout << "Please start entering " << stack_size << " elements into your array" << std :: endl;
	
	for(int array_index = 0; array_index < stack_size; array_index++)
	{
		std :: cout << "This is the index now : " << array_index << std :: endl;
		std :: cin >> input_variable;
		stack[array_index] = input_variable;
	}
	
	std :: cout << "This is your initial stack : " << stack << std :: endl;
	std :: cout << "The type of the variable stack is : " << typeid(stack).name() << std :: endl;
	std :: cout << "Printing the stack using a * operator :" << *stack << std :: endl;
	
	display_stack(stack, stack_size);
	insert_element_end(stack, stack_size);
return 0;
}
