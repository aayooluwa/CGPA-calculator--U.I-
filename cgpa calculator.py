def cgpa_display():
    total1=0
    total_units=0
    #accepts input that determines the arithmethic to use for grading
    pointsystem=input("\n What is the grade point system, 4.0 or 7.0?:")
    

    
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
    ps=int(float(pointsystem))
    
    #collects details of the student. Should be reprogrammed to get the details from an input file
    name=input("\n Enter the student name:\t")
    dept=input(" Enter the department:\t")
    year=input(" Enter the year of student:\t")
    sem=input(" Enter the semester of the student:\t")
    n=int(input(" Enter the number of courses:\t"))
    
    
    
    
    
    print("\n Enter the grades in (A-F) arrear")
    marks=[]
    
    
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
                    