from abc import ABC,abstractmethod

class Course (ABC):
    course_counter : int = 0
    def __init__(self,course_name,course_code,course_fee,course_duration,course_faculty,course_level):
        
        self.course_id = Course.generate_id()
        self.course_name = course_name
        self.course_code = course_code
        self.course_fee = course_fee
        self.course_duration = course_duration
        self.course_faculty = course_faculty
        self.course_level = course_level

    @classmethod
    def generate_id(cls):
        cls.course_counter += 1
        return f"CID{cls.course_counter:03d}"

    @abstractmethod
    def review_course_details(self):
        pass
    
    @abstractmethod
    def  change_course(self,new_course_name,new_course_code,new_faculty,new_course_level):
        pass
    @abstractmethod
    def convert_to_dict(self):
        pass

class UndergraduateCourse(Course):
    def __init__(self,course_name, course_code, course_fee,course_duration, course_faculty,course_level,year_of_study,entry_requirements):
        super().__init__(course_name, course_code,course_fee,course_duration,course_faculty,course_level)
        self.year_of_study = year_of_study
        self.entry_requirements = entry_requirements

    def register_course(self):
        return ("COURSE SUCCESSSFULLY REGISTERED") 

    def review_course_details(self):
        return f"\n\t\tREVIEWING COURSE RECORD\nCourse ID: {self.course_id}\nCourse Name: {self.course_name}\nCourse Code: {self.course_code}\nCourse Tuition: {self.course_fee}\nCourse Duration: {self.course_duration}\nFaculty: {self.course_faculty}\nCourse level: {self.course_level}\nYear of study: {self.year_of_study}\nEntry Requirement: {self.entry_requirements}"

    def  change_course(self,new_course_name,new_course_code,new_fee,new_duration,new_faculty,new_level,new_inputs,new_requirement):
        self.course_id = self.course_id
        self.course_name = new_course_name
        self.course_code = new_course_code
        self.course_fee = new_fee
        self.course_duration = new_duration
        self.course_faculty = new_faculty
        self.course_level = new_level
        self.year_of_study = new_inputs
        self.entry_requirement = new_requirement        
        return f"success identity shifted. Course is {self.course_id}\nID: {self.course_id}\nCourse code: {self.course_code}"


    def convert_to_dict(self):
        return{    
            "COURSE ID" : self.course_id,
            "Course name" : self.course_name,
            "Course code" : self.course_code,
            "Total fees" : self.course_fee,
            "Course Duration" : self.course_duration,
            "Faculty" : self.course_faculty,
            "Course level" : self.course_level,
            "Year_of_study" : self.year_of_study,
            "Entry_requirements" : self.entry_requirements
            }


class PostgraduateCourse(Course):
    def __init__(self, course_name, course_code, course_fee, course_duration,course_faculty,course_level,research_required,previous_qualification):
        super().__init__(course_name, course_code,course_fee, course_duration,course_faculty, course_level)
        self.research_required = research_required
        self.previous_qualification = previous_qualification

    def register_course(self):
        return ("COURSE SUCCESSSFULLY REGISTERED") 

    def review_course_details(self):
        return f"\n\t\tREVIEWING COURSE RECORD\nCourse ID: {self.course_id}\nCourse Name: {self.course_name}\nCourse Code: {self.course_code}\nCourse Tuition: {self.course_fee}\nCourse Duration: {self.course_duration}\nFaculty: {self.course_faculty}\nnCourse level: {self.course_level}\nResearch required: {self.research_required}\nPrevious Qualification: {self.previous_qualification}"

    def  change_course(self,new_course_name,new_course_code,new_fee,new_duration,new_faculty,new_level,new_research_required,new_qualification):
        self.course_id = self.course_id 
        self.course_name = new_course_name
        self.course_code = new_course_code
        self.course_fee = new_fee
        self.course_duration = new_duration
        self.course_faculty = new_faculty
        self.course_level = new_level
        self.research_required = new_research_required
        self.previous_qualification = new_qualification
        return f"success identity shifted. Course is {self.course_id}\nID: {self.course_id}\nCourse code: {self.course_code}"


    def convert_to_dict(self):
        return{    
            "COURSE ID" : self.course_id,
            "Course name" : self.course_name,
            "Course code" : self.course_code,
            "Total fees" : self.course_fee,
            "Course Duration" : self.course_duration,
            "Faculty" : self.course_faculty,
            "Course level" : self.course_level,
            "Research_required" : self.research_required,
            "Previous_qualification" : self.previous_qualification

            }


