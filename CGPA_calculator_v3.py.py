class Student:

    def __init__(self,r,n,d,y):
        self.r_number = r
        self.name = n
        self.dept = d
        self.year = y

    def academic_report(self,cgpa,result):
        print("\nACADEMIC REPORT")
        print("="*40)

        print("Register Number :", self.r_number)
        print("Name            :", self.name)
        print("Department      :", self.dept)
        print("Year            :", self.year)
        print("CGPA            :", round(cgpa,2))
        print("Classification  :", result)
        print("="*40)

    def student_details(self):
        print("Register number: ",self.r_number)
        print("Name: ",self.name)
        print("Department: ",self.dept)
        print("Year: ",self.year)

r = input("Enter register number: ")
while True:
        n = input("Enter name: ")
        if len(n.strip())==0:
            print("Enter a correct name.")
        else:
            try:
                float(n)
                print("Invalid name")
            except ValueError:
                break
while True:
    d = input("Enter department: ")
    if len(d.strip()) == 0:
        print("Enter a Valid department")
    else:
        try:
            float(d)
            print("Invalid department name")
        except ValueError:
            break
while True:
    try:
        y = int(input("Enter the year of studying: "))
        if y > 0 and y <= 4:
            break
        else:
            print("Enter a Valid year")
    except ValueError:
        print("Invalid year")

stu = Student(r,n,d,y)


class CGPACalculator:
    grade_points = {'O':10,'A+':9,'A':8,'B+':7,'B':6,'C':5,'U':0}

    def g_points(self,grades):
        return self.grade_points[grades]

    def gpa_calc(self):
        subject_data = []
        while True:
            try:
                n = int(input("Enter total number of subjects for semester: "))
                if n > 0:
                    break
                else:
                    print("Enter subject number greater than 0")
            except ValueError:
                    print("Enter a Valid subject number")
        total_grade_points = 0
        total_credit = 0
        for i in range(1,n+1):
            while True:
                subject_name = input("Enter subject names: ")
                if len(subject_name.strip()) == 0:
                    print("Enter a Valid subject name")
                else:
                    try:
                        float(subject_name)
                        print("Invalid subject name")
                    except ValueError:
                        break
            while True:
                try:
                    credit = int(input("Enter number of credits: "))
                    if credit > 0 and credit <= 10:
                        break
                    else:
                        print("Enter a credit between 1 and 10")
                except ValueError:
                    print("Please enter a number")
            while True:
                grades = input("Enter grade").upper()
                if grades in self.grade_points:
                    break
                else:
                    print("Enter valid grade")
            points = self.g_points(grades)
            subject_data.append({'Subject_Name':subject_name,'Credit':credit,'Grades':grades})
            t_grades = points*credit
            total_grade_points+=t_grades
            total_credit+=credit
        GPA = total_grade_points/total_credit
        print("\nSubject Report")
        print("-"*40)
        for subject in subject_data:
            print("Subject :", subject['Subject_Name'])
            print("Credit  :", subject['Credit'])
            print("Grade   :", subject['Grades'])
            print("-"*20)
        return GPA

    def CGPA_calc(self):
        CGPA_list = []
        while True:
            try:
                semester = int(input("Enter total semester studied: "))
                if semester > 0 and semester <= 4:
                    break
                else:
                    print("Enter Valid semester number")
            except ValueError:
                print("Invalid semester number")
        for j in range(semester):
            print(f"\nSemester {j+1}")
            gpa = self.gpa_calc()
            print("Semester GPA:", round(gpa, 2))
            CGPA_list.append(gpa)
        CGPA = sum(CGPA_list)/len(CGPA_list)
        if CGPA >= 9:
            result = "Outstanding"
        elif CGPA >= 8:
            result = "First Class with Distinction"
        elif CGPA >= 7:
            result = "First Class"
        elif CGPA >= 6:
            result = "Second Class"
        else:
            result = "Pass"
        print("CGPA:", round(CGPA, 2))
        print("Result:", result)
        return CGPA,result

cgpa = CGPACalculator()
CGPA,result = cgpa.CGPA_calc()
stu.academic_report(CGPA,result)

        

        
        



        
        
