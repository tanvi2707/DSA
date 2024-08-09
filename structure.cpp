#include<iostream>
using namespace std;

struct node
{
	char data;
	struct node *next;
};
struct node *head =NULL;
struct node *one=new node;
struct node *two=new node;
struct node *three=new node;

int main()
{
	cout<<"ENTER VALUE:";
	cin>>one->data;
	cin>>two->data;
	cin>>three->data;
	one->next=two;
	two->next=three;
	three->next=NULL;
	head=one;
	
	while(head!=NULL)
	{
		cout<<head->data;
		head=head->next;
	}
	
return 0;
}
		

