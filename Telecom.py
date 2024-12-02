# Telecom Domain Project: Billing System

class Customer:
    def __init__(self, customer_id, name, plan):
        self.customer_id = customer_id
        self.name = name
        self.plan = plan
        self.usage_minutes = 0
        self.bill = 0

    def add_usage(self, minutes):
        self.usage_minutes += minutes

    def calculate_bill(self):
        if self.plan == "Basic":
            self.bill = 10 + 0.05 * self.usage_minutes
        elif self.plan == "Premium":
            self.bill = 20 + 0.02 * self.usage_minutes
        else:
            self.bill = 0  # Invalid plan

    def get_details(self):
        return f"ID: {self.customer_id}, Name: {self.name}, Plan: {self.plan}, Usage: {self.usage_minutes} mins, Bill: ${self.bill:.2f}"


# Sample Usage
if __name__ == "__main__":
    # Create customers
    customer1 = Customer(1, "Alice", "Basic")
    customer2 = Customer(2, "Bob", "Premium")

    # Simulate usage
    customer1.add_usage(200)
    customer2.add_usage(300)

    # Calculate bills
    customer1.calculate_bill()
    customer2.calculate_bill()

    # Print customer details
    print(customer1.get_details())
    print(customer2.get_details())
