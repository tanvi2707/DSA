m=[]
r=int(input("Enter no of rows:"))
c=int(input("Enter no of columns:"))
for i in range(r):
	a=[]
	for j in range(c):
		ele=int(input("Enter the elements:"))
		a.append(ele)
	m.append(a)
	
print("1st Matrix is:")
for i in range(r):
	for j in range(c):
 		print(m[i][j],end=" ")
	print()
 	
 		
m1=[] 	

for i in range(r):
	a=[]
	for j in range(c):
		ele=int(input("Enter the elements:"))
		a.append(ele)
	m1.append(a)
	
print("2nd Matrix is:")
for i in range(r):
	for j in range(c):
 		print(m1[i][j],end=" ")
	print()
 	
 	
print("Addition of matrix is:")
for i in range(r):
	for j in range(c):
		print(m[i][j]+m1[i][j],end=" ")
	print()
	
print("subtraction of matrix is:")
for i in range(r):
	for j in range(c):
		print(m[i][j]-m1[i][j],end=" ")
	print()
	
print("Transpose of matrix is:")
for i in range(r):
	for j in range(c):
		print(m[j][i],end=" ")
	print()
	
print("Multiplication of matrix is:")
for i in range(r):
	for j in range(c):
		sum=0
		for k in range(c):
			sum=sum+(m[i][k]*m1[k][j])
		print(sum,end=" ")
	print()
	

	

























 	
		
