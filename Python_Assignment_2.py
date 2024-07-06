'''Create a Python program to manage a list of employees in a company. The program should allow the
addition, removal, and display of employees, as well as the ability to give raises and promotions based
on certain conditions.'''

class Employee:

    def __init__(self,name,age,position,salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def give_raise(self,amount):
        self.salary = self.salary + amount

    def promote(self, new_position, raise_amount):
        self.position = new_position
        self.give_raise(raise_amount)

class Management_System():

    def __init__(self):
        self.employees_list = []
    def add_employee(self, emp):
        self.employees_list.extend(emp)  # Gives an error - TypeError: 'Employee' object is not iterable

    def remove_employee(self, name):
        self.employees_list.remove(name) #here employees list holds object so how do we specify the name for which object?

    def annual_review(self):
        for e in self.employees_list:
            if e.age > 40:
                calc_raise = e.salary * 0.05
                self.give_raise(calc_raise)
            elif e.position.upper() == "JUNIOR DEVELOPER" :
                calc_raise = e.salary * 0.1
                self.promote("Senior Developer",calc_raise)

   # def find_employee(self,name):
   #     return employees(name)
         #here employees list holds object so how do we specify the name for which object?


e1 = Employee("Akshay",34,"Junior Developer",40000)
e2 = Employee("Meitheli",42,"Manager",80000)

m1 = Management_System()
m1.add_employee(e1)
m1.add_employee(e2)











