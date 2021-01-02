def cgpa_display():
    total1=0
    total_units=0
    #accepts input that determines the arithmethic to use for grading
    pointsystem=input("\n What is the point grade system, 4.0 or 7.0?:")

    
   #assigns points to each grade for both grading systems: ''dictionaries'
    if pointsystem =="4.0" or "4":
        grades={"A":"4","B":"3","C":"2","D":"1","F":"0"}
    if pointsystem == "7.0" or "7":
        grades={"A":"7","B":"6","C":"5","D":"4","d":"3","E":"2","e":"1","F":"0"}
    else:
        still_active = True
        while still_active:   
            pointsystem = input("The point system you entered is not available. Try again.")
            if pointsystem =="4.0" or "4":
                grades={"A":"4","B":"3","C":"2","D":"1","F":"0"}
                still_active = False
            if pointsystem == "7.0" or "7":
                grades={"A":"7","B":"6","C":"5","D":"4","d":"3","E":"2","e":"1","F":"0"}
                still_active = False
            else:
                still_active = True
                
                
    #converts float pointsystem to an integer for arithmetic
    ps = int(float(pointsystem))
    
    #collects details of the student. Should be reprogrammed to get the details from an input file
    name=input("\n Enter the student name:\t")
    dept=input(" Enter the department:\t")
    year=input(" Enter the year of student:\t")
    sem=input(" Enter the semester of the student:\t")
    n=int(input(" Enter the number of courses:\t"))
    
    
    grade_style_choice = input("A: Enter grades using score over 100 \nB: Enter grades using (A-F) arrear\n")        
    
    marks=[]

    if grade_style_choice == "A":
        
        
        if ps == 4:
            
            grades={"A":"4","B":"3","C":"2","D":"1","F":"0"}
           
            for entry in range(n):  
                subject_code=input("\n Enter the subject code:\t")
                units=float(input(" How many units is the course? \t"))
                y=int(input(" Enter the grade using score obtained over 100:\t\n"))
                
                if  70 <= y:
                    grade= "A"
                if  60 <= y < 70:
                    grade= "B"
                if  50 <= y < 60:
                    grade= "C"
                if  45 <= y < 50:
                    grade= "D"
                if  y < 45 :
                    grade= "F"
            
                elif  100 < y or y < 0:
                    still_active = True
                    
                    while still_active:     
                        x =input("You have entered an invalid score.Try again")
                        if  70 <= y:
                            grade= "A"
                            still_active = False
                        if  60 <= y < 70:
                            grade= "B"
                            still_active = False
                        if  50 <= y < 60:
                            grade= "C"
                            still_active = False   
                        if  45 <= y < 50:
                            grade= "D"
                            still_active = False
                        if  y < 45 :
                            grade= "F"
                            still_active = False
                        else:
                            still_active = True
                
                if grade in grades:    
                    points=float(grades[grade])
                    entry=(subject_code,units,points,grade)
                    marks.append(entry)
        
        if ps == 7:
            grades={"A":"7","B":"6","C":"5","D":"4","d":"3","E":"2","e":"1","F":"0"}
            
            for entry in range(n):
                
                subject_code=input("\n Enter the subject code:\t")
                units=float(input(" How many units is the course? \t"))
                x=int(input(" Enter the grade using score obtained over 100:\t\n"))
        
                if  70 <= x:
                    grade = "A"
                if  65 <= x < 70:
                    grade = "B"
                if  60 <= x < 65:
                    grade = "C"
                if  55 <= x < 60:
                    grade = "D"
                if  50 <= x < 55 :
                    grade = "d"
                if  45 <= x < 50:
                    grade = "E"
                if  40 <= x <45:
                    grade = "e"
                if  x < 40:
                    grade = "F"
                elif  100 < x or x < 0:
                    still_active = True
                    
                    while still_active:     
                        x =input("You have entered an invalid score.Try again")
                        if  70 <= x:
                            grade = "A"
                            still_active = False
                        if  65 <= x < 70:
                            grade = "B"
                            still_active = False
                        if  60 <= x < 65:
                            grade = "C"
                            still_active = False
                        if  55 <= x < 60:
                            grade = "D"
                            still_active = False
                        if  50 <= x < 55 :
                            grade = "d"
                            still_active = False
                        if  45 <= x < 50:
                            grade = "E"
                            still_active = False
                        if  40 <= x <45:
                            grade = "e"
                            still_active = False
                        if  x < 40:
                            grade = "F"
                            still_active = False
                        else:
                            still_active = True
                    
                if grade in grades:
                    points=float(grades[grade])
                    entry=(subject_code,units,points,grade)
                    marks.append(entry)
        
        
        
    if grade_style_choice == "B":
        
        for entry in range(n):
        
            subject_code=input("\n Enter the subject code:\t")
            units=float(input(" How many units is the course? \t"))
            grade=input(" Enter the grade in (A-F):\t\n")
            
            if grade in grades:
                points=float(grades[grade])
                entry=(subject_code,units,points,grade)
                marks.append(entry)
            
            else:
                still_active = True
    
                while still_active:   
                    grade=input("You have entered an invalid grade.Try again.")
                    
                    if grade in grades:
                        points=float(grades[grade])
                        entry=(subject_code,units,points,grade)
                        marks.append(entry)
                        still_active = False
                    
                    else:
                        still_active = True  
           
        
    print("\n\tNAME:",name,"\t\tDEPARTMENT:",dept)
    print("\n\tYEAR:",year,"\t\tSEMESTER:",sem)
    print("\n\tSubject code" +"\t\tGrade" + "\t\tUnits" + "\t\tPoints")
    
    for entry in marks:
        subject_code,units,points,grade=entry
        print("    \n\t",subject_code,"    \t\t",grade,"  \t\t",units,"  \t\t",points)
        total1= total1 + points * units
        total_units=total_units + units*ps
        cgpa=(total1*ps/total_units)
                
    print(total1)
    print(total_units)
    print("\n\nCGPA=",cgpa)
cgpa_display() 
input("\n Press enter key to exit....")        
                    