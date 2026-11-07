class FeesItem:
    fees_counter : int = 0
    def __init__(self, fees_item_name,category,amount):
        self.fees_id = FeesItem.generate_id()
        self.fees_item_name = fees_item_name
        self.category = category
        self.amount = amount


    def update_amount(self,new_amount:int):
        self.amount = new_amount

    @classmethod
    def generate_id(cls):
        cls.fees_counter += 1
        return f"F{cls.fees_counter:03d}"

    def view_fees(self):
        print("Fees Id:", self.fees_id)
        print("Fees Name:", self.fees_item_name)
        print("Category", self.category)
        print("Total Fees:", self.amount)


    def fees_convert(self):
        return {
            "Item ID" : self.fees_id,
            "Item name" : self.fees_item_name,
            "item category" : self.category,
            "Item amount" : self.amount
            }
