import math

# --- Class Definitions ---

class MortgageCalculator:
    """Encapsulates the financial logic for bank loans."""
    @staticmethod
    def get_monthly_payment(principal, rate, years):
        if principal <= 0: return 0
        r = rate / 12 / 100
        n = years * 12
        # Amortization Formula
        return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

class Property:
    """Base class demonstrating Encapsulation and Abstraction."""
    def __init__(self, address, price):
        self.address = address
        self.__price = price # Private attribute

    @property
    def price(self):
        return self.__price

    def calculate_stamp_duty(self):
        """Logic for HK Ad Valorem Stamp Duty (Scale 2)."""
        p = self.__price
        if p <= 3000000: return 100
        elif p <= 4500000: return p * 0.015
        elif p <= 6000000: return p * 0.0225
        elif p <= 9000000: return p * 0.03
        else: return p * 0.0375

    def get_max_loan_ratio(self):
        """Polymorphism: To be overridden by subclasses."""
        return 0.5 

class PrivateHousing(Property):
    """Inheritance: Specific rules for Private Flats."""
    def get_max_loan_ratio(self):
        # 90% loan for properties up to 10M
        return 0.9 if self.price <= 10000000 else 0.7

class Buyer:
    """Encapsulates Buyer's financial data and decision logic."""
    def __init__(self, name, monthly_income, cash_savings):
        self.name = name
        self.__income = monthly_income # Private
        self.__cash = cash_savings     # Private

    def evaluate_purchase(self, property_obj):
        # 1. Upfront Costs calculation
        loan_ratio = property_obj.get_max_loan_ratio()
        downpayment = property_obj.price * (1 - loan_ratio)
        stamp_duty = property_obj.calculate_stamp_duty()
        total_upfront = downpayment + stamp_duty + 10000 # 10k Legal fees
        
        # 2. Monthly Debt calculation
        loan_amt = property_obj.price * loan_ratio
        monthly_pay = MortgageCalculator.get_monthly_payment(loan_amt, 4.125, 30)
        dsr = (monthly_pay / self.__income) * 100

        # Output Report
        print(f"\n" + "="*45)
        print(f" BUYER: {self.name} | PROPERTY: {property_obj.address}")
        print(f"="*45)
        print(f"Property Price:   ${property_obj.price:,.0f}")
        print(f"Stamp Duty:       ${stamp_duty:,.0f}")
        print(f"Downpayment:      ${downpayment:,.0f} ({int((1-loan_ratio)*100)}%)")
        print(f"Total Cash Req:   ${total_upfront:,.0f}")
        print(f"---")
        print(f"Monthly Payment:  ${monthly_pay:,.0f}")
        print(f"DSR (Income %):   {dsr:.1f}%")

        # Decision Logic
        has_cash = self.__cash >= total_upfront
        is_affordable = dsr <= 50

        if has_cash and is_affordable:
            print(f"RESULT: ✅ CONGRATULATIONS! Purchase Approved.")
        else:
            reason = []
            if not has_cash: reason.append("Insufficient Cash")
            if not is_affordable: reason.append("Failed Income Stress Test")
            print(f"RESULT: ❌ DECLINED - {', '.join(reason)}")

# --- Demo Execution ---

# 1. Create a Target Property
dream_home = PrivateHousing("Quarry Bay - Taikoo Shing", 9500000)

# 2. Create Different Buyer Profiles
buyers = [
    Buyer("Mr. Rich (Cash Heavy)", monthly_income=30000, cash_savings=3000000),
    Buyer("Ms. High-Earner (Cash Low)", monthly_income=100000, cash_savings=500000),
    Buyer("The Perfect Match", monthly_income=75000, cash_savings=1500000)
]

# 3. Run the Evaluation
for person in buyers:
    person.evaluate_purchase(dream_home)
