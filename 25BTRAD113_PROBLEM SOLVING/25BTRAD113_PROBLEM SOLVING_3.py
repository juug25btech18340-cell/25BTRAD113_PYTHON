#ATTENDENCE TRACKER
students = {} 
total_classes = 0 
def add_student(): 
name = input("Enter student name: ") 
if name in students: 
print("Student already exists!") 
else: 
students [name] = 0 
print("Student added successfully!") 
def mark attendance(): 
global total classes. 
total classes += 1 
print("\nMark Attendance (P = Present, A = Absent)") 
for name in students: 
status = input (name + ": ").upper() 
while status not in ["P", "A"]: 
print("Enter only P or A") 
status input (name + ": ").upper() 
if status == "p": 
students [name] += 1 
print("Attendance updated successfully!") 
def display_attendance(): 
print("\n- ATTENDANCE DETAILS 
if not students: 
print("No students available.") return 
----- 
for name, present in students.items(): 
2)}%") 
-") 
percentage= (present / total_classes)* 100 if total classes > 0 else 0 
print(f" {name} - Present: {present}, Total Classes: {total_classes}, Attendance: [round (percentage, 
def check_low_attendance(): 
print("\nStudents Below 75% Attendance:") 
found = False 
for name, present in students.items(): 
percentage= (present / total_classes) *100 if total_classes > 0 else 0 if percentage < 75: 
- 
print (f" {name} {round (percentage, 2)}%") found = True 
if not found: 
print("No students below 75% attendance.") 
