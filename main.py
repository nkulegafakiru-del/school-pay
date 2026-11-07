
from student import Student,Undergraduate,Postgraduate
from course import Course,UndergraduateCourse,PostgraduateCourse
from feestructure import FeesStructure
from accountledger import AccountLedger
from payment import Payment,CashPayment,MobileMoneyPayment,BankPayment,CreditCardPayment
from feesitem import FeesItem

import json

with open ("tuition.json", "r") as file:
    tuition_data = json.load(file)

def getting_fees(name):
    if name in tuition_data:
        fees_dict = tuition_data[name]
        print()
        print("="*64)
        print(f"|    Fee Structure for {name} |")
        print("="*64)
        index : int = 0
        for fees_name, price in fees_dict.items():
            print(f"| {index:>2}.\t{fees_name.title():<42}{price:<13}|")
            index += 1
        total_fee = sum(fees_dict.values())
        
        
        print("=" * 64)
        print(f"|  TOTAL FEE \t\t\t\t\t {total_fee:,}     |")
        print("=" * 64)
        print ()
        

        return total_fee
        
    else:
        print(f"\n❌ Error: '{name}' was not found in the tuition data file.")
        return 0

def load_returning_student(search_id):
    """Dynamically loads a student profile from school.json with 100% dynamic attributes"""
    import os
    search_id = search_id.strip().upper()
    
    if not os.path.exists("school.json"):
        return None
        
    try:
        with open("school.json", "r") as file:
            saved_records = json.load(file)
    except json.JSONDecodeError:
        return None

    for record in saved_records:
        if isinstance(record, dict) and record.get("Student ID") == search_id:
            
            saved_course_id = record.get("Course ID")
            saved_course_name = record.get("Course")
            saved_course_fee = record.get("Course Fee", 0.0)

            class DynamicRecoveredCourse:
                def __init__(self, c_id, c_name, c_fee):
                    self.course_id = c_id
                    self.course_name = c_name
                    self.course_fee = c_fee
            
            dynamic_course_instance = DynamicRecoveredCourse(saved_course_id, saved_course_name, saved_course_fee)
            if record.get("Status") == "undergraduate":
                recovered_student = Undergraduate(
                    record.get("First name"),
                    record.get("Last name"),
                    record.get("Gender"),
                    dynamic_course_instance, 
                    record.get("Contact"),
                    record.get("Email"),
                    record.get("Academic level"),
                    record.get("Status"),
                    record.get("Year of study"),
                    record.get("Entry requirement")
                )
            else:
                recovered_student = Postgraduate(
                    record.get("First name"),
                    record.get("Last name"),
                    record.get("Gender"),
                    dynamic_course_instance,
                    record.get("Contact"),
                    record.get("Email"),
                    record.get("Academic level"),
                    record.get("Status"),
                    record.get("Research required"),
                    record.get("Qualification")
                )
                
            recovered_student.std_id = search_id
            return recovered_student

    return None


def get_fee_amount(name, category):
    if name in tuition_data:
        fees_dict = tuition_data[name]

        if category in fees_dict:
            return fees_dict[category]

        print("Fee category not found.")
        return None

    print("Course not found.")
    return None

def getting_course_data():
    index : int = 1
    for course in tuition_data:
        print(f"| {index}.\t{course:<52} |")
        index += 1
        
courses = {}

def verify_pin():
    user_name = "admin"
    pass_word = "1234"
    login_attempts = 0
    while login_attempts < 3:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username == user_name  and password == pass_word :
            print("\nLogin Successful! Welcome to the system.")
            return True
        else:
            login_attempts += 1
            print(f"Incorrect credentials. Attempts remaining: {3 - login_attempts}\n")
    print("\t\tToo many failed attempts.\n\t\tSystem locked for security.\n")
    exit()
    return False

print("\n\t\tSYSTEM LOGIN\n")
verify_pin()

while True:
    
    try:
        new_student = None  
        print('='*41)
        print("|\tMAIN STUDENTS PAY LIST\t\t|")
        print('='*41)
        print("| 1. COURSE\t\t\t\t|\n| 2. STUDENT\t\t\t\t|\n| 3. FEES STRUCTURE\t\t\t|\n| 4. FEES ITEM\t\t\t\t|\n| 5. PAYMENT\t\t\t\t|\n| 6. ACCOUNT LEDGER\t\t\t|")
        print('='*41)
        option = input ("\nEnter option: ")
        if option == "2":
                
            print("\n\tSTUDENT REGISTRATION SYSTEM\n")
            if not courses:
                print("❌ No course objects have been registered in the system yet.")
                print("Please choose Option 1 and register a course first.\n")
                continue

            student_fname = input("Enter student First Name: ").upper().strip()
            student_lname = input("Enter student Last Name: ").upper().strip()
            student_gender = input("Enter student Gender: ").upper().strip()

            print("\n\t\tREGISTERED SYSTEM COURSES\n")
            print("=" * 64)
            for course_name in courses:
                print(f" - {course_name}")
            print("=" * 64)

            student_course = input("\nEnter student Course [EXACTLY as listed above]: ").strip()

            if student_course not in courses:
                print("❌ Error: That course has not been registered as a Course object yet.")
                print("Please choose a course listed above or create it in Option 1.\n")
                continue

            
            selected_course = courses[student_course]

            student_contact = input("Enter student contact: ").strip()
            student_email = input("Enter student Email: ").strip()
            academic_level = input("Enter the Course level or Track [Diploma, Bachelor, Masters, PhD]: ").strip()

            std1 = None
            if academic_level in ["Diploma", "Bachelor", "Bachelors"]:
                status = "undergraduate"
                year_of_study = input("Enter Year of Study (eg. 1, 2, 3): ").strip()
                requirement = input("Enter Entry Requirements: ").strip()

                std1 = Undergraduate(
                    student_fname, student_lname, student_gender,
                    selected_course, student_contact, student_email,
                    academic_level, status, year_of_study, requirement
                )

            elif academic_level in ["Masters", "PhD"]:
                status = "postgraduate"
                research_required = input("Enter Research Required [TRUE or FALSE]: ").strip().upper()
                qualification_required = input("Enter Qualification Required: ").strip()

                std1 = Postgraduate(
                    student_fname, student_lname, student_gender,
                    selected_course, student_contact, student_email,
                    academic_level, status, research_required, qualification_required
                )

            else:
                print("❌ Wrong academic track level entered. Returning to menu.")
                continue

            
            print("\n--- STUDENT REGISTRATION SUCCESSFUL (WITH COMPOSITION) ---")
            print(std1.display_student_detail())
            print("\n--- COURSE DETAILS ACCESSED VIA COMPOSITION ---")
            print("Course ID:   ", std1.course.course_id)
            print("Course Name: ", std1.course.course_name)
            print("Base Fee:    shs", f"{std1.course.course_fee:,}")

            Payment.student_registry[std1.std_id] = std1

            if hasattr(std1, 'convert_to_dict'):
                new_student = std1.convert_to_dict()
            else:
                new_student = std1.user_inputs()


        elif option == "1":
            print("\n\tLOGGED TO COURSE DASHBOARD\n")
        
            print("=" * 62)
            getting_course_data()
            print("=" * 62)
            
            name = input("\nEnter Course Name [EXACTLY as given]: ").strip()
            
            if name not in tuition_data:
                print(f"❌ Error: '{name}' was not found in the tuition data file.")
                continue

            fee = getting_fees(name)
            code = input("Enter Course code [eg cs-101]: ").strip()
            duration = input("Enter Course duration: ").strip()
            faculty = input("Enter Course faculty: ").strip()
            level = input("Enter Course level (Bachelors / Masters / PhD / Diploma): ").strip()
            print()
            
            course1 = None
            if level in ["Bachelors", "Diploma"]:
                print("\nUNDERGRADUATE COURSE DETECTED")
                user_input = int(input("Enter the year of study (eg. 1, 2, 3): "))
                requirement = input("Enter the entry requirements: ")
                course1 = UndergraduateCourse(name, code, fee, duration, faculty, level, user_input, requirement)
                course1.register_course()
                print(course1.review_course_details())

            elif level in ["Masters", "PhD"]:
                print("\nPOSTGRADUATE COURSE DETECTED")
                user_input = input("Is research required? [TRUE or FALSE]: ")
                requirement = input("Enter the qualification required: ")
                course1 = PostgraduateCourse(name, code, fee, duration, faculty, level, user_input, requirement)
                course1.register_course()
                print(course1.review_course_details())
            else:
                print("❌ Invalid course level entered")
                continue

            # Save the registered course into our active memory array tracker
            courses[course1.course_name] = course1

            # Simple Course Verification Loop
            while True:
                answer = input("\nDo you want to change the course details? (yes or no): ").lower().strip()
                if answer == "yes":
                    print("-" * 62)
                    getting_course_data()
                    print("-" * 62)
                    
                    name = input("\nType the new course name [EXACTLY as given]: ").strip()
                    if name not in tuition_data:
                        print("❌ Course not found.")
                        continue
                        
                    fee = getting_fees(name)
                    code = input("Type new course code: ")
                    duration = input("Enter duration: ")
                    faculty = input("Type new faculty: ")
                    level = input("Enter level (Bachelors/Masters/PhD/Diploma): ").strip()
                    
                    if level in ["Bachelors", "Diploma"]:
                        user_input = input("Enter year of study: ")
                        requirement = input("Enter entry requirements: ")
                        course1 = UndergraduateCourse(name, code, fee, duration, faculty, level, user_input, requirement)
                    elif level in ["Masters", "PhD"]:
                        user_input = input("Is research required? [TRUE or FALSE]: ")
                        requirement = input("Enter qualification required: ")
                        course1 = PostgraduateCourse(name, code, fee, duration, faculty, level, user_input, requirement)
                    
                    # Update active collection registry
                    courses[course1.course_name] = course1
                    print("\nCourse changed successfully!")
                    print(course1.review_course_details())
                    break
                    
                elif answer == "no":
                    print("Keeping original course registration details.")
                    break
                else:
                    print("Invalid choice. Please enter yes or no.")
            
            # Convert to dictionary layout for saving
            new_student = course1.convert_to_dict()


        elif option == "3":
            print()
            getting_course_data()
            name = input("\nEnter Course Name [EXACTLY as its given]: ").strip()
            input_academic_year = input("Enter Academic Year [eg 2026/2027]: ")
            input_semester = input("Enter semester you are in: ")
            
            if name in tuition_data:
                # 1. Fetch the base amount for the course tuition from your file
                base_amount = getting_fees(name)
            else:
                print("❌ Course not found in records.")
                continue

            # 2. Create the base Tuition FeesItem object
            base_tuition_item = FeesItem("Core Tuition", "academic", base_amount)

            # 3. Initialize your structure assignment
            university_structure = FeesStructure(name, input_academic_year, input_semester, base_tuition_item)
            
            # 4. Ask the user if they want to append an additional item right now
            print("\n--- Optional: Add Additional Functional Fee Component ---")
            add_extra = input("Do you want to add an additional functional fee item right now? (yes/no): ").lower().strip()
            
            if add_extra == "yes":
                item_name = input("Enter the fees Item Name [e.g., Computer Lab, Library, Registration]: ").strip()
                item_category = input("Enter fees Category [academic/administrative/sports welfare/accomodation]: ").strip()
                try:
                    extra_amount = int(input("Enter item price amount (shs): ").strip())
                    university_structure.add_functional_fee(item_name, item_category, extra_amount)
                except ValueError:
                    print("❌ Invalid amount format. Skipping dynamic item addition.")
            else:
                print("Notice: No additional functional fee items appended. Setting item addition value to shs 0.")

            # 5. Display the statement breakdown report
            university_structure.display_statement()

            while True:       
                update_answer = input("Do you want to update the required base fee amount? (yes/no): ").lower().strip()
                try:
                    if update_answer == "yes":
                        changed_amount = int(input("Type the new updated total amount (shs): "))
                        base_tuition_item.update_amount(changed_amount)
                        university_structure.display_statement()
                        break
                    elif update_answer == "no":
                        print("\nNotice: Fees structure remains at its original value.")
                        break
                except ValueError:
                    print("Wrong user inputs entered. Must be valid integers.")
            
            new_student = university_structure.convert_fees_to_dict()



        elif option == "6":

            print("\n=== SCHOOL PAY SYSTEM ===")
            search_id = input("Enter Student ID to find records (e.g., SID-001): ").strip().upper()
            
            if search_id in Payment.student_registry:
                student_obj = Payment.student_registry[search_id]
                print(f"✅ Student Found in Active Memory: {student_obj.f_name} {student_obj.l_name}")
            else:

                student_obj = load_returning_student(search_id)
                
                if student_obj is not None:
                    
                    Payment.student_registry[search_id] = student_obj
                    print(f"\n✅ Returning Student Loaded from Storage File: {student_obj.f_name} {student_obj.l_name}")
                else:
                    print(f"❌ Error: Student ID '{search_id}' was not found in active session memory or system records.")
                    print("Please use Option 2 to register this student profile for the first time.\n")
                    continue

            print(f"Course Track: {student_obj.course.course_name}")
            print("-" * 45)
            name = student_obj.course.course_name
            total_billed = float(getting_fees(name))
            item_name = input("Enter the fees item name (e.g., Tuition): ").strip()
            alex_ledger = AccountLedger(student_obj, item_name, total_billed)

            def create_valid_transaction(s_id, category):
                while True:
                    try:
                        amount_paid = float(input("\nEnter Amount Paid: ").strip())
                    except ValueError:
                        print("❌ Error: Amount Paid must be a valid number. Please retry.")
                        continue

                    print("\nSelect Payment Method for this transaction:")
                    print("\t1. Cash\n\t2. Mobile Money\n\t3. Bank Slip\n\t4. Credit Card")
                    choice = input("Enter option choice (1-4): ").strip()

                    if choice == "1":
                        payment_method = "CASH"
                        receipt = input("Enter physical receipt slip number: ").strip()
                        transaction_obj = CashPayment(student_obj, category, amount_paid, payment_method, receipt)
                    
                    elif choice == "2":
                        print("\n\t--- MOBILE MONEY ---")
                        payment_method = "MOBILE MONEY"
                        phone = input("Enter sender's phone number: ").strip()
                        trx_id = input("Enter transaction ID: ").strip()
                        transaction_obj = MobileMoneyPayment(student_obj, category, amount_paid, payment_method, phone, trx_id)

                    elif choice == "3":
                        print("\n\t--- BANK TRANSFER ---")
                        payment_method = "BANK TRANSFER"
                        bank_name = input("Enter bank name: ").strip()
                        reference = input("Enter bank transfer reference number: ").strip()
                        transaction_obj = BankPayment(student_obj, category, amount_paid, payment_method, bank_name, reference)
        

                    elif choice == "4":
                        print("\n--- CREDIT CARD PAYMENT ---")
                        payment_method = "CREDIT CARD"
                        last_four = input("Enter the card's last four digits: ").strip()
                        authorization = input("Simulate authorization result (approved/declined): ").lower().strip()
                        transaction_obj = CreditCardPayment(student_obj, category, amount_paid, payment_method, last_four, authorization)
                        

                    else:
                        print("❌ Invalid payment method selection. Please try again.")
                        continue

                    if transaction_obj.initiate_payment() is True:
                        return transaction_obj 
                    else:
                        print("❌ Transaction verification rejected. Let's rebuild the transaction entry.")
                        print("🔄 Restarting payment initialization loop...")

            print("\n--- Processing First Payment ---")
            current_transaction = create_valid_transaction(student_obj, item_name)

        
            alex_ledger.compute_balance(current_transaction)
            alex_ledger.over_pay_allocation()
            alex_ledger.generate_ledger(current_transaction)

            new_student = alex_ledger.convert_ledger_to_dict(current_transaction)
            
            while True:
                sub_option = input("\nDo you want to process a Second Payment? (YES or NO): ").lower().strip()
                if sub_option == "yes":
                    print("\n--- Processing Second Payment ---")
                    next_transaction = create_valid_transaction(student_obj, item_name)
                    current_balance = alex_ledger.compute_balance(next_transaction)
                    print(f"\nFinal Balance Due Field: {current_balance} {Payment.currency}")
                    
                    alex_ledger.over_pay_allocation()
                    alex_ledger.generate_ledger(next_transaction)
                    new_student = alex_ledger.convert_ledger_to_dict(next_transaction)
                    break
                elif sub_option == "no":
                    print("Skipped second payment processing.")
                    break
                else:
                    print("❌ Invalid response choice. Please enter YES or NO.")

        elif option == "5":
            print("\n=== SCHOOL PAY SYSTEM ===")
            search_id = input("Enter Student ID to find records (e.g., SID-001): ").strip().upper()
            
            if search_id in Payment.student_registry:
                student_obj = Payment.student_registry[search_id]
                print(f"✅ Student Found in Active Memory: {student_obj.f_name} {student_obj.l_name}")
            else:

                student_obj = load_returning_student(search_id)
                
                if student_obj is not None:
                    
                    Payment.student_registry[search_id] = student_obj
                    print(f"\n✅ Returning Student Loaded from Storage File: {student_obj.f_name} {student_obj.l_name}")
                else:
                    print(f"❌ Error: Student ID '{search_id}' was not found in active session memory or system records.")
                    print("Please use Option 2 to register this student profile for the first time.\n")
                    continue

            print(f"Course Track: {student_obj.course.course_name}")
            print("-" * 45)
            
            category = input("Enter Payment Category (e.g., Tuition, Library): ").strip()
            
            try:
                amount_paid = float(input("Enter Amount Paid: ").strip())
            except ValueError:
                print("❌ Invalid entry: Amount Paid must be a valid number. Transaction aborted.")
                continue
            
            print("\nSelect Payment Method:")
            print("\t1. Cash\n\t2. Mobile Money\n\t3. Bank Slip\n\t4. Credit Card")
            choice = input("Enter option choice (1-4): ").strip()

            if choice == "1":
                payment_method = "CASH"
                receipt = input("Enter physical receipt slip number: ").strip()
                # Pass the dynamically recovered student object directly
                current_transaction = CashPayment(student_obj, category, amount_paid, payment_method, receipt)
                
            elif choice == "2":
                print("\n\t--- MOBILE MONEY ---")
                payment_method = "MOBILE MONEY"
                phone = input("Enter sender's phone number: ").strip()
                transaction = input("Enter transaction ID: ").strip()
                current_transaction = MobileMoneyPayment(student_obj, category, amount_paid, payment_method, phone, transaction)
            
            elif choice == "3":
                print("\n\t--- BANK TRANSFER ---")
                bank_name = input("Enter bank name: ").strip()
                reference = input("Enter bank transfer reference number: ").strip()
                payment_method = "BANK TRANSFER"
                current_transaction = BankPayment(student_obj, category, amount_paid, payment_method, bank_name, reference)
               
            elif choice == "4":
                print("\n--- CREDIT CARD PAYMENT ---")
                last_four = input("Enter the card's last four digits: ").strip()
                authorization = input("Simulate authorization result (approved/declined): ").lower().strip()
                payment_method = "CREDIT CARD"
                current_transaction = CreditCardPayment(student_obj, category, amount_paid, payment_method, last_four, authorization)
                
            else:
                print("❌ Invalid payment method option selected. Returning to dashboard.")
                continue
                
            if current_transaction.initiate_payment() is True:
                current_transaction.display_payment()
                new_student = current_transaction.generate_dict()
            else:
                print("❌ Transaction registration rejected. Returning to main menu panel...\n")
                continue


        elif option == "4":
            print()
            # 1. Print all available courses
            print("=" * 62)
            getting_course_data()
            print("=" * 62)
            
            name = input("\nEnter Course Name [EXACTLY as it's given]: ").strip()
            
            # 2. Safety Check: If course doesn't exist, stop immediately
            if name not in tuition_data:
                print(f"❌ Error: '{name}' was not found in the tuition data file.")
                continue  # Sends the user safely back to the main menu

            # 3. Fetch the fee amount safely (calls it only ONCE)
            amount = getting_fees(name)
            
            print()
            item_name = input("Enter the fees Item Name [Tuition/Functional/Registration/Examination]: ").strip()
            item_category = input("Enter fees Category [academic/administrative/sports welfare/accomodation]: ").strip()

            # 4. Create the standalone FeesItem object safely
            fees = FeesItem(item_name, item_category, amount)
            
            print("\n--- STANDALONE FEES ITEM CREATED ---")
            fees.view_fees()
            
            # 5. Convert to simple flat dict so it saves safely to school.json
            new_student = fees.fees_convert()
    except ValueError:
        print("❌ We have detected invalid user inputs")

    if new_student is not None:
        me = []
        with open ("school.json", "r") as doc:
            me = json.load(doc)


        with open ("school.json", "w") as doc:
            me.append(new_student)
            json.dump(me, doc ,indent = 4)
            
        print("\n\t\tRecords registered successfully\n\t\t\tTHANK YOU.....\n")
        
    while True:
        try:
            user_input = input("Do you still want to continue interacting with system [YES or NO]: ").lower()
            if user_input == "yes":
                break

            elif user_input == "no":
                print("\n\t\tYou have exited the System\n")
                exit()
            else:
                raise ValueError ("Wrong inputs entered") 

        except ValueError:
            print("\nWe have detected invalid user inputs MUST be YES or NO")


