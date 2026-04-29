#Q2. Student percentage + average

n = int(input("Enter number of students: "))
total_percent = 0

for i in range(n):
    print(f"/nStudent {i+1}")
    total = 0
    for j in range(5):
        marks = int(input(f"Enter marks of subject {j+1}: "))
        total += marks
    
    percent = total / 5
    total_percent += percent
    print("Percentage:", percent)

avg = total_percent / n
print("\nAverage Percentage:", avg)