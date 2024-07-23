def additionmat(r,c,m,m1):
	for i in range(r):
		for j in range(c):
			print(m[i][j]+m1[i][j],end=" ")
		print()
		
def subtractionmat(r,c,m,m1):
	for i in range(r):
		for j in range(c):
			print(m[i][j]-m1[i][j],end=" ")
		print()
		
def multiplicationmat(r,c,m,m1):
	for i in range(r):
		for j in range(c):
			sum=0
			for k in range(c):
				sum=sum+(m[i][k]*m1[k][j])
			print(sum,end=" ")
		print()
		
def transposemat(r,c,m):
	for i in range(r):
		for j in range(c):
			print(m[j][i],end=" ")
		print()
	
	
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
	
while True:
	print("Press 1 for addition")
	print("Press 2 for subtraction")
	print("Press 3 for multiplication")
	print("Press 4 for transpose")
	print("Press 5 for exit")
	
	choice=int(input("Enter you choice:"))
	if choice==1:
		print("Addition of matrix is:")
		additionmat(r,c,m,m1)
	if choice==2:
		print("subtraction of matrix is:")
		subtractionmat(r,c,m,m1)
	if choice==3:
		print("Multiplication of matrix is:")
		multiplicationmat(r,c,m,m1)
	if choice==4:
		print("Transpose of matrix is:")
		transposemat(r,c,m)
	else:
		break
		






 	
 	

	

	


	

	

























 	
		
