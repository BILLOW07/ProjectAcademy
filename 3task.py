students = [
    ("Иван", "Петров", [4, 5, 5, 4], [3, 4, 5, 3], 0.9),
    ("Мария", "Иванова", [5, 5, 5, 5], [5, 5, 4, 5], 0.95),
    ("Алексей", "Сидоров", [3, 4, 3, 3], [4, 3, 4, 4], 0.7),
    ("Елена", "Козлова", [5, 4, 5, 5], [4, 5, 5, 5], 0.85),
    ("Дмитрий", "Смирнов", [2, 3, 2, 3], [3, 2, 2, 3], 0.5)
]
def low_attendance(students, threshold=0.75):
    return [f"{s[0]} {s[1]}" for s in students if s[4] < threshold]

def best_student(students):
    def calc_avg(student):
        return (sum(student[2])/len(student[2]) + sum(student[3])/len(student[3]))/2
    
    best = max(students, key=calc_avg)
    return f"{best[0]} {best[1]}", calc_avg(best)

def need_python_help(students):
    return [f"{s[0]} {s[1]}" for s in students 
            if sum(s[2])/len(s[2]) < sum(s[3])/len(s[3])]

print("Студенты с низкой посещаемостью:", *low_attendance(students), sep='\n')
name, avg = best_student(students)
print(f"\nЛучший студент: {name} (средний балл: {avg:.2f})")
print("\nНужно подтянуть Python:", *need_python_help(students), sep='\n')