from feesitem import FeesItem

class FeesStructure:
    fees_counter: int = 0

    def __init__(self, course_name, academic_year, semester, main_tuition_item: FeesItem):
        self.feestructure_id = FeesStructure.generate_id()
        self.course_name = course_name 
        self.academic_year = academic_year
        self.semester = semester
        self.main_tuition = main_tuition_item
        
        self.fees_components = []

    @classmethod
    def generate_id(cls):
        cls.fees_counter += 1
        return f"Fs{cls.fees_counter:03d}"

    def add_functional_fee(self, fees_item_name, category, amount):
        new_item = FeesItem(fees_item_name, category, amount)
        self.fees_components.append(new_item)
        print(f"Added: {fees_item_name} (shs {amount:,})")


    def display_statement(self):
        added_items_total = sum(item.amount for item in self.fees_components)
        total_overall = self.main_tuition.amount + added_items_total

        print("\n==============================================")
        print("          OFFICIAL FEES STRUCTURE             ")
        print("==============================================")
        print(f"Course/Program:  {self.course_name}")
        print(f"Academic Year:   {self.academic_year}")
        print(f"Semester:        {self.semester}")
        print(f"Structure ID:    {self.feestructure_id}")
        print("----------------------------------------------")
        print(f"1. Core Tuition Fee:         shs {self.main_tuition.amount:,}")
        
        if self.fees_components:
            print("\n2. Additional/Functional Items:")
            for item in self.fees_components:
                print(f"   - {item.fees_item_name:<22} : shs {item.amount:,}")
        
        print("----------------------------------------------")
        print(f"TOTAL FEES REQUIRED:         shs {total_overall:,}")
        print("==============================================\n")


    def convert_fees_to_dict(self):
        added_items_total = 0
        for item in self.fees_components:
            added_items_total = added_items_total + item.amount

        total_overall = self.main_tuition.amount + added_items_total

        
        fees_data_block = {
            "Academic Year": self.academic_year,
            "Semester": self.semester,
            "FeesStructure ID": self.feestructure_id,
            "Course Name": self.course_name,
            "Base Tuition Fee": self.main_tuition.amount,
            "Additional Components Amount": added_items_total,
            "Total Amount Required": total_overall
        }
        
        return fees_data_block
