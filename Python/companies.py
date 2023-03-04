class employee:
    def __init__(self, name, company, role):
        self.name = name
        self.company = company
        self.role = role
    
    def __str__(self):
        return self.name, self.company, self.role

class company:

    def __init__(self, name, sales, products, employees):
        self.name = name
        self.sales = sales
        self.products = products
        self.employees = employees
    
    def add_product(self, name, price):
        self.products.update({name:price})
    
    def add_employee(self, name, role = 1):
        self.employees.append(employee(name, self.name, role))

    def get_employees(self):
        for employee in self.employees:
            print(employee.__str__())
    
    def get_products(self):
        print(self.products)
    
    def sell(self, product):
        if product in self.products:
            self.sales.append(product)
    
    def get_sales(self):
        print(self.sales)

apple = company("CrimTech", [], {"Comp":10}, [])
apple.add_employee("Naomi", 10)
apple.add_employee("Naomi", 10)
apple.add_employee("Comper")
apple.add_product("Slides", 5)
apple.sell("Slides")
apple.sell("blah")

apple.get_employees()
apple.get_products()
apple.get_sales()