def calculate_avg(marks):
    return sum(marks) / len(marks)

def student_performance(marks,attendance):
    
    if attendance < 75 or marks < 50:
        return("Low Attendance and Average Marks")
    else:
        return("Good Performance")

def student_report(name,marks,attendance):
    avg = calculate_avg(marks)
    status = student_performance(avg,attendance)
    print(f"Student Name: {name}")
    print(f"Average Marks: {avg}")
    print(f"Attendance: {attendance}%")
    print(f"Performance Status: {status}")