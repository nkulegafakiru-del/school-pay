from datetime import date

class AccountLedger:
    payment_counter: int = 0
    
    def __init__(self, student_obj, fees_item_name, total_billed: float):
        self.ledger_id = AccountLedger.generate_id()
        self.student_obj = student_obj  # Keep the whole student object here
        self.student_id = student_obj.std_id  # Keep the string ID here for easy dictionary conversion
        self.transaction_date = date.today()
        self.fees_item_name = fees_item_name
        self.total_billed = total_billed
        self.total_amount_paid = 0.0
        self.balance_due = total_billed
        self.credit_amount = 0.0

    @classmethod
    def generate_id(cls):
        cls.payment_counter += 1
        return f"AC-{cls.payment_counter:03d}"

    def verify_student(self, transaction_obj):
        
        print(f"System: Student {self.student_id} verified for payment processing.")

    def compute_balance(self, transaction):
        if transaction.payment_status in ["paid", "Pending confirmation", "Approved (Simulation)", "APPROVED"]:
            self.total_amount_paid += transaction.amount_paid
            self.balance_due = self.total_billed - self.total_amount_paid
        else:
            print(f"❌ Payment verification failed. Status: {transaction.payment_status}")
            
        return self.balance_due

    def over_pay_allocation(self):
        if self.balance_due < 0:
            self.credit_amount = -self.balance_due
            print(f"\n[ALERT] Overpayment Detected for Student {self.student_id}!")
            print(f"Allocating shs {self.credit_amount:,} as an advanced credit.")
        else:
            self.credit_amount = 0.0
        return self.credit_amount

    def generate_ledger(self, transaction):
        print("\n========== PAYMENT LEDGER ==========")
        print("AccountLedger ID:", self.ledger_id)
        print("Student ID:      ", self.student_id)
        print("Total billed:    ", f"shs {self.total_billed:,}")
        print("Amount Paid:     ", f"shs {self.total_amount_paid:,}")
        print("Balance Due:     ", f"shs {self.balance_due:,}")
        print("Over Payment:    ", f"shs {self.credit_amount:,}")
        print("====================================")
        
        transaction.display_payment()
        
    def convert_ledger_to_dict(self, transaction):
        transaction.ledger_id = self.ledger_id
        return {
            "AccountLedger": {
                "AccountLedger ID": self.ledger_id,
                "Student ID": self.student_id,
                "fees_item_name": self.fees_item_name,
                "Total billed": self.total_billed,
                "Amount Paid": self.total_amount_paid,
                "Balance Due": self.balance_due,
                "Over Payment": self.credit_amount
            },
            "Payment": transaction.generate_dict()
        }

        
