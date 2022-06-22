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

	std :: cout << std :: endl;
}

void insert_element_end(int* stack, int stack_size){
	
	int element;
	std :: cout << "Please specify the element that you want to insert at the end of the stack" << std :: endl;
	std :: cin >> element;
	
	std :: cout << "Stack size is :" << stack_size << std :: endl;
	
	stack[stack_size+1] = element;
	std :: cout << "Element Insertion Successful " << std :: endl;
	
	display_stack(stack, stack_size);
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
	
	std :: cout << std :: endl;
	std :: cout << "This is your initial stack : " << stack << std :: endl;
	std :: cout << "The type of the variable stack is : " << typeid(stack).name() << std :: endl;
	std :: cout << "Printing the stack using a * operator :" << *stack << std :: endl;
	
	std :: cout << "Stack First Element is :" << *stack << std :: endl;
	std :: cout << "Stack second element is : " << *stack+1 << std :: endl;
	std :: cout << "Stack third element is : " << *stack+2 << std :: endl;
	
	std :: cout << "Stack First Element is :" << stack << std :: endl;
	std :: cout << "Stack second element is : " << stack+1 << std :: endl;
	std :: cout << "Stack third element is : " << stack+2 << std :: endl;
	
	std :: cout << "Stack First Element Memory Location is :" << &stack << std :: endl;
	std :: cout << "Stack second element Memory Location is : " << (&stack)+1 << std :: endl;
	std :: cout << "Stack third element Memory Location is : " << (&stack)+2 << std :: endl;
	
	display_stack(stack, stack_size);
	insert_element_end(stack, stack_size);
return 0;
}
