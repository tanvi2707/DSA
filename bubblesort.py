a=[]
n=int(input("Enter the no of elements:"))

for i in range (n):
	m=int(input("Enter the number: "))
	a.append(m)

for i in range (n):
	for j in range (0,n-i-1):
		if(a[j]>a[j+1]):
			temp=a[j]
			a[j]=a[j+1]
			a[j+1]=temp
		

print("The sorted array is")
for i in range(n):
		print(a[i])
