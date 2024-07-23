def insertion(a,n):
	for i in range (n):
		temp=a[i]
		j=i-1
		while(j>=0 and a[j]>temp):
	
			a[j+1]=a[j]
			j=j-1
	
		a[j+1]=temp

	
	for i in range(n):
		print(a[i])
		
def shell(a,n):
	d=n//2
	while d>0:
		for i in range(d,n):
			temp=a[i]
			j=i
			while j>=d and a[j-d]>temp :
				a[j]=a[j-d]
				j=j-d
			
			a[j]=temp
		d//=2	
		
	for i in range(n):
		print(a[i])	
		
a=[]
n=int(input("Enter the no of elements:"))

for i in range (n):
	m=float(input("Enter the number: "))
	a.append(m)

		
while True:
	
	print("Press 1 for Insertion Sort")
	print("Press 2 for Shell Sort")
	print("Press 3 to Exit")
	
	choice=int(input("Enter your choice:"))
	if choice==1:
		print("Sorted array using Insertion Sort is:")
		insertion(a,n)		
	if choice==2:
		print("Sorted array using Shell Sort is:")
		shell(a,n)
	if choice==3:
		print("You have exicted the program")
		break;		
