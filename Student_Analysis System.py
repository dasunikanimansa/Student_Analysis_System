n = int(input("Enter number of students: "))

with open("student_record.txt","w") as file:
    for i in range(n):
        name = input("Enter name: ")
        mark = int(input("Enter mark: "))
        file.write(name+":"+str(mark)+"\n")

highest = 0
Sum = 0 
count = 0 
pass_count = 0 


with open("student_record.txt","r") as file:
    for line in file:
        name,mark = line.strip().split(":")
        name = name.strip()
        mark = int(mark.strip())

        if mark > highest:
            highest = mark

        Sum += mark
        count += 1

        if mark > 50:
            pass_count += 1

students=[]
with open("student_record.txt","r") as file:
    for line in file:
        name,mark = line.strip().split(":")
        student = {
            "name":name.strip(),
            "mark":int(mark.strip())
        }
        students.append(student)
students.sort(key = lambda x:x["mark"])        
        
             


print("Highest mark: "+ str(highest))
print("Lowest_mark: "+ str(students[0]["mark"]))
print("Average: "+ str(Sum/count))
print("Pass Count: "+str(pass_count))
print("Top student: "+ students[n-1]["name"])


