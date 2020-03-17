name = input ("What is your name? ")
student_id = input ("Registration number: ")
nt1 = int(input ("Grade of your first homework: ")) * 0.4
np1 = int(input ("First exame's grade: ")) * 0.6
nt2 = int(input ("Grade of your second homework: ")) * 0.4
np2 = int(input ("Second exame's grade: ")) * 0.6
nt3 = int(input ("Grade of your third homework: ")) * 0.4
np3 = int(input ("Third exame's grade: ")) * 0.6
nt4 = int(input ("Grade of your forth homework: ")) * 0.4
np4 = int(input ("Forth exame's grade: ")) * 0.6

n1b = nt1+np1
n2b = nt2+np2
n3b = nt3+np3
n4b = nt4+np4

grades = [n1b,n2b,n3b,n4b]
media = sum(grades) / len(grades)

if media >= 7:
    print (f"{name}, registration nº {student_id}, your grade was {media}, you are approved")
else:
    print (f"{name}, registration nº {student_id}, your grade was {media}, you are failed")    