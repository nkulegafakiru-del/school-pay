from  abc import ABC,abstractmethod

class Student(ABC):
    student_counter : int = 0
    def __init__(self,f_name, l_name, gender, course, contact, email, academic_level):
    
        self.std_id = Student.generate_id()
        self.f_name= f_name
        self.l_name = l_name
        self.gender = gender 
        self.course = course
        self.contact = contact
        self.email = email
        self.academic_level = academic_level
        
    
    def __str__(self):
        return f"{self.std_id}\n{self.f_name}\n{self.l_name}\n{self.contact}"
     
    @classmethod
    def generate_id(cls):
        cls.student_counter += 1
        return f"SID-{cls.student_counter:03d}"
    
    @abstractmethod
    def display_student_detail(self):
        pass
    @abstractmethod
    def user_inputs(self):
        pass

class Undergraduate(Student):
    def __init__(self, f_name, l_name, gender,course, contact, email,academic_level,status,year_of_study,requirement):
        super().__init__(f_name, l_name, gender,course, contact, email,academic_level)
        self.status = status
        self.year_of_study = year_of_study
        self.requirement = requirement
        
    def register_student(self):
        pass
    
    def display_student_detail(self):
        print ("\n\t\tSTUDENT DETAILS")
        print("="*50)
        return f"Student ID:\t{self.std_id}\nStudent First Name:\t{self.f_name}\nStudent Last Name:\t{self.l_name}\nGender:\t{self.gender}\nCourse:\t{self.course.course_name}\nContact:\t{self.contact}\nAcademic level:\t{self.academic_level}\nStatus:\t \t{self.status}\nYear of study:\t{self.year_of_study}"
        print("="*50)

    def user_inputs(self):
        return{
    "Student ID" : self.std_id,
    "First name" : self.f_name,
    "Last name" : self.l_name,
    "Gender" : self.gender,
    "Course ID" : self.course.course_id,
    "Course" : self.course.course_name,
    "Contact" : self.contact,
    "Email" : self.email,
    "Academic level" : self.academic_level,
    "Status" : self.status,
    "Year of study" : self.year_of_study,
    "Entry requirement" : self.requirement
        }




class Postgraduate(Student):
    def __init__(self, f_name, l_name, gender,course, contact, email,academic_level,status,research_required,qualification):
        super().__init__(f_name, l_name, gender,course, contact, email, academic_level)
        self.status = status
        self.research_required = research_required
        self.qualification = qualification

    def register_student(self):
        pass

    def display_student_detail(self):
        print ("\n\t\tSTUDENT DETAILS")
        print("="*50)
        return f"Student ID:\t{self.std_id}\nStudent First Name:\t{self.f_name}\nStudent Last Name:\t{self.l_name}\nGender:\t{self.gender}\nCourse:\t{self.course.course_name}\nContact:\t{self.contact}\nacademic_level:\t{self.academic_level}\nStatus:\t \t{self.status}\nResearch required:\t{self.research_required}\nQualificaton:\t\t{self.qualification}"
        print("="*50)


    def user_inputs(self):
        return{
    "Student ID" : self.std_id,
    "First name" : self.f_name,
    "Last name" : self.l_name,
    "Gender" : self.gender,
    "Course ID" : self.course.course_id,
    "Course" : self.course.course_name,
    "Contact" : self.contact,
    "Email" : self.email,
    "academic_level" : self.academic_level,
    "Status" : self.status,
    "Research required" : self.research_required,
    "Qualification" : self.qualification

        }

