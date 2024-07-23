a=[]
n=int(input("Enter the no of elements:"))

for i in range (n):
	m=int(input("Enter the number: "))
	a.append(m)

for i in range (n):
	min=i
	for j in range (i+1,n):
		if(a[j]<a[min]):
			min=j
	
	temp=a[i]
	a[i]=a[min]
	a[min]=temp
	
print("The sorted array is")
for i in range(n):
		print(a[i])
