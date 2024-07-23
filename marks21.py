def average(marks, n):
    sum = 0
    for i in range(n):
        sum += marks[i]
    avg = sum / n
    return avg

def maximum(marks, n):
    max = 0
    for i in range(n):
        if marks[i] > max:
            max = marks[i]
    return max

def minimum(marks, n):
    min = 999
    for i in range(n):
        if marks[i] < min and marks[i] != -1:
            min = marks[i]
    return min

def absent(marks, n):
    cnt = 0
    for i in range(n):
        if marks[i] == -1:
            cnt += 1
    return cnt

def maxfreq(marks, n):
    max = maximum(marks, n)
    cnt = marks.count(max)
    return cnt


marks = []
n = int(input("Enter the number of students: "))

for i in range(n):
    m = int(input("Enter marks of student {}: ".format(i+1)))
    marks.append(m)

print("\n")
while True:
    print("Press 1: For calculating average.")
    print("Press 2: For calculating max marks.")
    print("Press 3: For calculating min marks.")
    print("Press 4: For calculating absent students.")
    print("Press 5: For calculating max marks freq.")
    print("Press 6: For Exiting.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Average:", average(marks, n))
    elif choice == 2:
        print("Maximum marks:", maximum(marks, n))
    elif choice == 3:
        print("Minimum marks:", minimum(marks, n))
    elif choice == 4:
        print("No. of absent students:", absent(marks, n))
    elif choice == 5:
        print("Maximum marks frequency:", maxfreq(marks, n))
    elif choice == 6:
        break
    else:
        print("Invalid Input")


