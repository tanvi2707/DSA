a=[]
n=int(input("Enter the no of elements:"))

for i in range (n):
	m=int(input("Enter the number: "))
	a.append(m)

for i in range (n):
	temp=a[i]
	j=i-1
	while(j>=0 and a[j]>temp):
	
		a[j+1]=a[j]
		j=j-1
	
	a[j+1]=temp

print("The sorted array is:")
for i in range(n):
	print(a[i])
