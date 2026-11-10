def average(*numbers):
    """İxtiyari sayda ədədin ortalamasını tapır"""
    if not numbers:  
        return 0
    return sum(numbers) / len(numbers)

def make_course(code, **details):
    """Kurs kodu və əlavə məlumatlardan dictionary düzəldir"""
    course = {"code": code}
    for key, value in details.items():
        course[key] = value
    return course

print(average(70, 80, 90)) 
print(average(100))          
print(average())             
print(make_course("CE101", title="Fundamentals of Programming", credits=6))
