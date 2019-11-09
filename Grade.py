import numpy as np
import matplotlib.pyplot as plt



#This funtion takes an int and returns a letter grade
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    else:   # grade must be B, C, D or F
        if score >= 80:
            letter = 'B'
        else:   # grade must be C, D or F
            if score >= 70:
                letter = 'C'
            else:   # grade must D or F
                if score >= 60:
                    letter = 'D'
                else:
                    letter 'F'
    return letter
    
    
    studentScore = input()
print("The student's grade is: " + letterGrade(studentScore))
