# Write a Python dictionary that stores full name and CGPA informations of 10 final year students. Then
# do the following :
# (a) Print the names as initials with surname, say Arindam Biswas becomes A. Biswas.
# (b) Display details of the student with highest CGPA.
# (c) Display names of students with CGPA below 3.0 out of 10.0, if any.

students = {
    "Arindam Biswas": 8.2,
    "Sneha Roy": 7.5,
    "Rahul Dutta": 9.1,
    "Priya Sen": 6.8,
    "Riya Naskar": 7.9,
    "Ananya Roy": 8.5,
    "Sumantra Das": 5.6,
    "Taniya Mukherjee": 9.3,
    "Ritwik Banerjee": 4.8,
    "Neha Chatterjee": 2.9
}

# (a) Print the names as initials with surname
print("Names as initials with surname: ")
for name in students.keys():
    parts = name.split()
    initials = '. '.join(p[0] for p in parts[:-1])+ '. ' + parts[-1]
    print(initials)


# (b) Display details of the student with highest CGPA.
highest_cgpa = max(students, key=students.get)
print("\nStudent with highest cgpa:")
print(f"{highest_cgpa} : {students[highest_cgpa]}")


# (c) Display names of students with CGPA below 3.0 out of 10.0, if any.

print("\nCGPA below 3.0: ")
for name, cgpa in students.items():
    if(cgpa < 3.0):
        print(f"{name}: {cgpa}") 

