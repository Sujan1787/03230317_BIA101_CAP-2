class Person:
    def _init_(self, name, income):
        self.name = name
        self._income = income  # Protected attribute

    def get_income(self):
        return self._income


class Employee(Person):
    def _init_(self, name, income, position, organization):
        super()._init_(name, income)
        self.position = position
        self.organization = organization

    def get_taxable_income(self):
        taxable_income = self.get_income()

        # Deduct PF and GIS contributions for regular employees
        if self.position == "Regular":
            taxable_income -= 0.10 * taxable_income  # PF contribution
            taxable_income -= 0.50 * taxable_income  # GIS contribution

        # Apply general deductions
        general_deductions = min(0.05 * taxable_income, 350000)
        taxable_income -= general_deductions

        return taxable_income


class TaxCalculator:
    def _init_(self, employee):
        self.employee = employee

    def calculate_tax_amount(self):
        taxable_income = self.employee.get_taxable_income()

        # Define tax slabs and rates
        tax_slabs = [
            (300000, 0.00),
            (400000, 0.10),
            (650000, 0.15),
            (1000000, 0.20),
            (1500000, 0.25)
        ]

        # Initialize tax amount
        tax_amount = 0

        # Calculate tax amount based on tax slabs
        for slab in tax_slabs:
            if taxable_income <= slab[0]:
                tax_amount += taxable_income * slab[1]
                break
            else:
                tax_amount += (slab[0] * slab[1])
                taxable_income -= slab[0]

        return tax_amount


# Example usage
try:
    emp1 = Employee("Sonam", 80000, "Regular", "Private")
    calculator = TaxCalculator(emp1)
    tax_amount = calculator.calculate_tax_amount()
    print(f"Tax amount for {emp1.name}: Nu. {tax_amount:.2f}")

except Exception as e:
    print("An error occurred:",str(e))
