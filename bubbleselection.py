def bubble(a,n):
	for i in range (n):
		for j in range (0,n-i-1):
			if(a[j]>a[j+1]):
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
				
	
	for i in range(n):
			print(a[i])			
				
	
def selection(a,n):
	for i in range (n):
		min=i
		for j in range (i+1,n):
			if(a[j]<a[min]):
				min=j
		temp=a[i]
		a[i]=a[min]
		a[min]=temp
		
	
	for i in range(n):
			print(a[i])	
			
a=[]
n=int(input("Enter the no of elements:"))

for i in range (n):
	m=float(input("Enter the number: "))
	a.append(m)

		
while True:
	print("Press 1 for Bubble Sort")		
	print("Press 2 for Selection Sort")
	print("Press 3 to Exit")
	
	
	choice=int(input("Enter your choice:"))
	if choice==1:
		print("Sorted array using Bubble Sort is:")
		bubble(a,n)	
	if choice==2:
		print("Sorted array using Selection Sort is:")
		selection(a,n)
	if choice==3:
		print("You have exited the program")
		break;					
