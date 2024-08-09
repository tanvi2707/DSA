#include<iostream>
using namespace std;

struct node
{
	char data;
	struct node *next;
};
struct node *head =NULL;

void insert()
{
	struct node *newnode=new node;
	cout<<"ENTER DATA:";
	cin>>newnode->data;
	newnode->next=NULL;
	if(head==NULL)
	{
		head=newnode;
	}
	else
	{	
		head->next=newnode;
		head=newnode;
	}
}
	

void display() 
{
    node* temp = head;
    if (temp == NULL) 
    {
        cout << "The list is empty." << endl;
        return;
    }
    
    cout << "List contents: ";
    while (temp != NULL) 
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}


void menu() 
{
    int choice;
    bool running = true;

    while (running) 
    {
        cout << "1. Insert" << endl;
        cout << "2. Display" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
            case 1:
                insert();
                break;
            case 2:
                display();
                break;
            case 3:
                cout << "Exiting program." << endl;
                running = false;
                break;
            default:
                cout << "Invalid choice, please enter again." << endl;
                break;
        }
    }
}

int main()
{
	menu();
	return 0;
}

	
	

		
