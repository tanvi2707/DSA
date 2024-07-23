a=[]
n=int(input("Enter the no of elements:"))


for i in range (n):
	m=int(input("Enter the number: "))
	a.append(m)
	

for i in range(d,n):
	temp=a[i]
	j=i
	while(j>=d and a[j-d]>temp):
		a[j]=a[j-d]
		j=j-d
			
	a[j]=temp
d=d/2
	
	
print("The sorted array is")
for i in range(n):
		print(a[i])	
	
		
