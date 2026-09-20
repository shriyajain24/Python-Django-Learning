def calculate_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return avg

def student_grade(marks):
    avg = calculate_avg(marks)
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "Average"

def student_attendance(attendance,marks):
    if attendance < 75:
        return "Low attendance"
    else:
        return "safe"