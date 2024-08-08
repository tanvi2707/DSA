def QuickSort(a,left,right):
	if (left<right):
		pindex=partition(a,left,right)
		QuickSort(a,left,pindex-1)
		QuickSort(a,pindex+1,right)
		
def partition(a,left,right):
		pivot=a[left]
		i=left
		j=right
		
		while(i<j):
			while(a[j]>pivot and i<=right-1):
				i=i+1
				
			while(a[j]>pivot and j>=left+1):
				j=j-1
				
			if(i<j):
				temp=a[i]
				a[i]=a[j]
				a[j]=temp
				
			temp=a[left]
			a[left]=a[j]
			a[j]=temp
			return j
			
a=[]
n=int(input("Enter the number of elemsnts:"))

for i in range(n):
	m=int(input("Enter the number:"))
	a.append(m)
left=0
right=n-1
QuickSort(a,left,right)

print("The Sorted array is:")
for i in range(n):
	print(a[i])