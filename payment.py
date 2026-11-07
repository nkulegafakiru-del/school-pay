from datetime import date

class Payment:
    payment_counter: int = 0
    currency = "UGX"
    student_registry = {}

    def __init__(self, student_obj, category, amount_paid, payment_method):
        self.payment_id = Payment.generate_id()
        self.payment_date = date.today()
        self.student_obj = student_obj
        self.category = category
        self.amount_paid = amount_paid
        self.payment_method = payment_method
        self.payment_status = "pending"
        self.ledger_id = None
        self.currency = Payment.currency 
        
    @classmethod
    def generate_id(cls):
        cls.payment_counter += 1
        return f"PID-{cls.payment_counter:03d}"

    @classmethod
    def register_student_to_payment(cls, student_object):
        cls.student_registry[student_object.std_id] = student_object
        print(f"System: Student {student_object.std_id} linked to the payment details.")


    def initiate_payment(self):
        pass

    def generate_dict(self):
        pass


class CashPayment(Payment):
    def __init__(self, student_obj, category, amount_paid, payment_method, receipt_number):
        super().__init__(student_obj, category, amount_paid, payment_method)
        self.receipt_number = receipt_number

    def initiate_payment(self):
        if self.amount_paid > 5000 and self.receipt_number:
            self.payment_status = "paid"
            print(f"\n[SUCCESS] Cash amount: {self.amount_paid:,} {self.currency} received and recorded successfully!")
            print(f"Physical Receipt #{self.receipt_number} verified and filed.")
            return True
        else:
            print(f"\n[ALERT] Amount paid of {self.amount_paid:,} was not recorded because Cash payment requires an amount greater than 5000 and a valid receipt number.please try again")
            self.amount_paid = 0
            self.payment_status = "pending confirmation"
            return False

    def display_payment(self):
        print("\n========== PAYMENT TRANSACTION==========")
        print("Payment ID:", self.payment_id)
        print("Date:", self.payment_date)
        print("Student ID:", self.student_obj.std_id)
        print("Student Name:", self.student_obj.f_name, self.student_obj.l_name)
        print("Category:", self.category)
        print("Payment method:", self.payment_method)
        print("Payment status:", self.payment_status)
        print("Amount Paid:", self.amount_paid)
        print("====================================\n") 
    
    def generate_dict(self):
        return {
            "Payment ID": self.payment_id,
            "Student ID": self.student_obj.std_id,
            "Student Name": f"{self.student_obj.f_name} {self.student_obj.l_name}",
            "Category": self.category,
            "Amount Paid": self.amount_paid,
            "Payment Method": self.payment_method,
            "Status": self.payment_status,
            "Ledger ID": self.ledger_id,
            "Receipt No": self.receipt_number
        }


class MobileMoneyPayment(Payment):
    def __init__(self, student_obj, category, amount_paid, payment_method, phone_number, transaction_id):
        super().__init__(student_obj, category, amount_paid, payment_method)
        self.phone_number = phone_number
        self.transaction_id = transaction_id

    def initiate_payment(self):
        if self.phone_number and self.transaction_id and self.amount_paid > 5000:
            self.payment_status = "Pending confirmation"
            print("\nMobile Money details recorded.")
            print("Transaction ID:", self.transaction_id)
            print("Awaiting payment confirmation.\n")
            return True
        else:
            self.payment_status = "Invalid"
            print("❌ Verification Failed: Phone number, transaction ID, and amount greater than 5000 are required.")
            return False

    def display_payment(self):
        print("\n========== PAYMENT TRANSACTION==========")
        print("Payment ID:", self.payment_id)
        print("Date:", self.payment_date)
        print("Student ID:", self.student_obj.std_id)
        print("Student Name:", self.student_obj.f_name, self.student_obj.l_name)
        print("Category:", self.category)
        print("Payment method:", self.payment_method)
        print("Payment status:", self.payment_status)
        print("Amount Paid:", self.amount_paid)
        print("Phone Number:", self.phone_number)
        print("====================================")

    def generate_dict(self):
        return {
            "Payment ID": self.payment_id,
            "Student ID": self.student_obj.std_id,
            "Student Name": f"{self.student_obj.f_name} {self.student_obj.l_name}",
            "Category": self.category,
            "Amount Paid": self.amount_paid,
            "Payment Method": self.payment_method,
            "Status": self.payment_status,
            "Ledger ID": self.ledger_id,
            "Phone Number": self.phone_number
        }


class BankPayment(Payment):
    def __init__(self, student_obj, category, amount_paid, payment_method, bank_name, reference):
        super().__init__(student_obj, category, amount_paid, payment_method)
        self.bank_name = bank_name
        self.reference = reference
        
    def initiate_payment(self):
        if not self.bank_name or not self.reference:
            print("\nBank name and reference are required.")
            self.payment_status = "Invalid"
            return False
            
        if self.amount_paid <= 5000:
            print("\n❌ Verification Failed: Bank transfer requires an amount greater than 5000.")
            self.payment_status = "Invalid"
            return False

        self.payment_status = "Pending confirmation"
        print(f"\nTransfer reference recorded for {self.bank_name}.")
        print("Awaiting bank confirmation.")
        return True

    def display_payment(self):
        print("\n========== PAYMENT TRANSACTION==========")
        print("Payment ID:", self.payment_id)
        print("Date:", self.payment_date)
        print("Student ID:", self.student_obj.std_id)
        print("Student Name:", self.student_obj.f_name, self.student_obj.l_name)
        print("Category:", self.category)
        print("Payment method:", self.payment_method)
        print("Payment status:", self.payment_status)
        print("Amount Paid:", self.amount_paid)
        print("Bank name:", self.bank_name)
        print("Bank reference no:", self.reference)
        print("====================================")

    def generate_dict(self):
        return {
            "Payment ID": self.payment_id,
            "Student ID": self.student_obj.std_id,
            "Student Name": f"{self.student_obj.f_name} {self.student_obj.l_name}",
            "Category": self.category,
            "Amount Paid": self.amount_paid,
            "Payment Method": self.payment_method,
            "Status": self.payment_status,
            "Ledger ID": self.ledger_id,
            "Bank name": self.bank_name,
            "Bank reference no": self.reference
        }


class CreditCardPayment(Payment):
    def __init__(self, student_obj, category, amount_paid, payment_method, last_four, authorization):
        super().__init__(student_obj, category, amount_paid, payment_method)
        self.last_four = last_four
        self.authorization = authorization

    def initiate_payment(self):
        if self.last_four.isdigit() and len(self.last_four) == 4:
            if self.authorization == "approved" and self.amount_paid > 5000:
                self.payment_status = "Approved (Simulation)"
                print("\nCard authorization simulated successfully.")
                return True  # 👈 CHANGED TO TRUE
            elif self.authorization == "declined":
                self.payment_status = "Declined"
                print("\nCard transaction declined.")
                return False  # 👈 CHANGED TO FALSE
            else:
                self.payment_status = "Pending"
                return False  # 👈 CHANGED TO FALSE
        else:
            self.payment_status = "Invalid"
            print("\nInvalid card digits.")
            return False  # 👈 CHANGED TO FALSE


    def display_payment(self):
        print("\n========== PAYMENT TRANSACTION==========")
        print("Payment ID:", self.payment_id)
        print("Date:", self.payment_date)
        print("Student ID:", self.student_obj.std_id)
        print("Student Name:", self.student_obj.f_name, self.student_obj.l_name)
        print("Category:", self.category)
        print("Payment method:", self.payment_method)
        print("Payment status:", self.payment_status)
        print("Amount Paid:", self.amount_paid)
        print("Last 4 card No:", self.last_four)
        print("Authorization:", self.authorization)
        print("====================================")

    def generate_dict(self):
        return {
            "Payment ID": self.payment_id,
            "Student ID": self.student_obj.std_id,
            "Student Name": f"{self.student_obj.f_name} {self.student_obj.l_name}",
            "Category": self.category,
            "Amount Paid": self.amount_paid,
            "Payment Method": self.payment_method,
            "Status": self.payment_status,
            "Ledger ID": self.ledger_id,
            "Last 4 card No": self.last_four,
            "Authorization": self.authorization
        }
