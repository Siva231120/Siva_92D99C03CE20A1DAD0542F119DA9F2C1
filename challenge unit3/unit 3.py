class Student:
  def _init_(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

# Create a list of student objects
students = [
  Student("Alice", "A101", 3.8),
  Student("Bob", "B102", 3.5),
  Student("Charlie", "C103", 3.9),
  Student("David", "D104", 3.7),
]

# Sort the students by CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"