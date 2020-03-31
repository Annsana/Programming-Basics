last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
#new semester subjects and marks
subjects=["physics", "calculus", "poetry", "history"]
grades=[98, 97, 85, 88]

#Your grade for Computer Science class just came in! You got a perfect score, 100!
subjects.append("computer science")
grades.append(100)
gradebook=list(zip(subjects,grades))

#Your grade for visual arts just came in! You got a 93!
gradebook.append(("visual arts",93))
print(list(gradebook))

#full gardebook is the sum of last semester and new semester gradebook
full_gradebook=last_semester_gradebook+gradebook
print(full_gradebook)
