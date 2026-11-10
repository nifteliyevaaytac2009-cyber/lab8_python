def make_student(name, score, group=""):
    """Tələbə məlumatlarından dictionary yaradır"""
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student

print(make_student("Kamran", 61, "CE-101"))

students = []
while True:
    name = input("Name (quit to stop): ")
    if name.lower() == "quit":
        break
    score = int(input("Score: "))
    group = input("Group (optional): ")
    stud = make_student(name, score, group)
    students.append(stud)

for s in students:
    print(s["name"] + ": " + str(s["score"]))