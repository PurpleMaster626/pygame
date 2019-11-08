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
#These variables are used in our while Loop


GradeList = []


#Loops through the
print("When you are done entering grades, enter to continue.")
while(true):


    studentScore = input("What is the students grade: ")
    
    
    if(not studentScore):
        break
        
    studentScoreInt = int(studentScore)
    GradeList.append(studentScoreInt)
    
    StudentGrade = letterGrade(StudentScoreInt)
    
    
    print("The students grade is: " + StudentGrade)
    
    
values = GradeList
#this also overwrites the var(values) which makes what we enter meaning less
#unless we comnent out the line below
#Example funtion to print a normal class bell curve
#Last # is num of students (data points)
#values = np.random.normal(50, 25, 67)



input("Press enter to generate graph")
plt.hist(values, 10)
plt.show()
