
# # OOP + Type Hints

# # Modules & Packages

# # Exception Handling



def line():
    print("-------------------------")

# # 1. Input and Output

# #name = input("Enter the name : ")
# #print(name);

# #age = int(input("Enter the age : "))
# #print(age);

# #--------------------------------------------------------------------------------

# # 2. if / elif / else

# marks = 50;

# if marks == 35:
#     print("Passed")
    
# elif marks >=50:
#     print("RanK - D")

# else:
#     print("Failed")

# line()

# #--------------------------------------------------------------------------------

# # 3. for loop
# name = ["Rushi","Raju", "Ram"]
# age = [12,32,36]
# student = {"name":"John", "age":20}

# for i in range(5):
#     print(i);
# line();

# chooseAge = 36
# for index, value in enumerate(age):
#     if chooseAge == value:
#         print(f"Found at index {index}")
#         break
# else:
#     print("Not found")
# line();

# print("List print via index + value")
# for name in enumerate(name):
#     print(name);
# line();

# print("Dict print Only value");
# for value in student.values():
#     print(value)
# line();

# print("Dict print via index + value")
# for key, value in student.items():
#     print(key ,"-", value)
# line()
# #--------------------------------------------------------------------------------

# # 3.List 

# payment = ["Card","UPI","NetBanking","Wallet","Cash"];
# prices = [100, 200, 400, 700, 1000]

# # 1.print the list
# for rank, pay in enumerate(payment,start=1):
#     print(rank ,pay);
# line();

# # 2.Find thhe element

# choosePayment = "UPI";
# for pay in payment:
#     if choosePayment == pay:
#         print("UPI is present")
# line();

# #3. filter() → Above the some of data

# needPrice = 500
# result = list(filter(lambda price: price>needPrice,prices))
# print(result);
# line();

# #5.map() → Action on each data

# result1 = list(map( lambda price: price * 0.9,prices))
# print(result1)
# line()

# #6.next() → First Match
# result3 = next(
#     (
#         pay1
#         for pay1 in payment
#         if pay1.startswith("Ca")    
#     ),None
# )

# print(result3);
# line();

# # 7. List function (Most Used)

# exp = [price for price in prices if price>500]
# print(exp)
# line();


# #--------------------------------------------------------------------------------
# # 4. List[dict]

# employees = [
#     {"index" : 1,"name": "Ravi", "age": 28, "dept": "IT", "salary": 50000, "active": True},
#     {"index" : 2,"name": "Neha", "age": 32, "dept": "HR", "salary": 45000, "active": True},
#     {"index" : 3,"name": "Arjun", "age": 26, "dept": "IT", "salary": 60000, "active": True},
#     {"index" : 4,"name": "Priya", "age": 91, "dept": "Finance", "salary": 55000, "active": True},
#     {"index" : 5,"name": "Rahul", "age": 30,  "dept": "HR", "salary": 60000, "active": False},
# ]

# for emp in employees:
#     if emp["index"]==1:
#         print(f"Name : {emp['name']} and Salary : {emp['salary']}")

# res =  len(employees)
# print("\n",res)

# line();

# # 1.Sum of the salary 

# sum_sal = sum(emp["salary"] for emp in employees if emp["active"])
# print(sum_sal)
# line();

# # 2. print the active employes only 
# #act = [( index,emp["name"]) for index, emp in enumerate(employees, start=1) if emp["active"] ]
# act = [( index,emp["name"]) for index, emp in enumerate(employees, start=1) if not emp["active"] ]
# print("act",act)
# line();

# # 3. Count the active emp
# count = 0;

# active_count = sum( 
#         1 
#         for emp in employees
#         if  emp["active"]
#     )
# print("Active emp count : ",active_count)
# line();

# sal = [(emp["name"])for emp in employees if emp["dept"]=="IT"]
# print(sal)
# line();

# sal_ge = [(emp["name"],emp["salary"])for index,emp in enumerate(employees) if emp["salary"]>50000]
# print(sorted(sal_ge))
# line();
# emp_active = [
#             (emp["name"],emp["dept"])
#             for emp in employees 
#             if emp["active"] and emp["dept"]=="HR" ] 

# print(emp_active)
# line();

# age_ge = [(emp["name"], emp["age"])for index,emp in enumerate(employees) if emp["age"]>30]
# print(age_ge);
# line();


# salary1 = {
#     emp["name"]: emp["salary"]
#     for emp in employees
# }

# print(salary1)
# line();
# employee_index = {
#     emp["index"]: emp
#     for emp in employees
# }

# print(employee_index)
# line();



# --------------------------------------------------------------------------
#  Topic Name :  Function
# --------------------------------------------------------------------------

# 1. Multiple Return Values

# def data(name, age, salary):
#     return {
#         "Name": name,
#         "Age": age,
#         "Salary": salary
#     }

# result = data("Rushi", 26, 25)
# print(result["Name"], result["Age"], result["Salary"])
# line();

# # 2. Variable Arguments ==>In positional arguments, Python matches values by their position (order).

# def total(*num):
#     return sum(num)

# result = total(1,2,3,4,5,6)
# print(result)
# line();

# # 3. Keyword Arguments ==> Instead of sending values by order, we send them by name.

# def employee(**data):
#     for index,value in data.items():
#         print(index ,":" , value)
    
# employee(
#     name="Rushi",
#     age=26,
#     salary=25000,
#     city="Pune"
# ) 
# line();

# # Mix *args and **kwarg

# def info(*ipconfig,**data):
#     print("Numbers :", ipconfig) 
#     print("Details :", data)


# info(10,20,30,name="Rushi",age=26)
# line();


# # 4. High order function 

# num = 5
# nums =[1,2,3]
# employee2 = {
#     "Name" : "Rushi",
#     "Age" : 26
# }

# def square(num)-> int:
#     print(num*num);

# def cube(num):
#     return num * num * num

# def total_sum(num):
#     print(sum(num))

# def process(data,function_type):
    
#     print("Process is started");
#     print("proces is in progress")
    
#     if function_type == square:
#         print("Square function called")
#         function_type(data);

#     if function_type == cube:
#         print("cube function called")
#         for i in data:
#             result = function_type(i);
#             print(result)

#     if function_type == total_sum:
#         print("Sum function called")
#         function_type(data)
    
#     print("Process is compledt ")

# process(nums,total_sum)
# line();


# # 5 . Lamda function 

# names=["John","Amy","Christopher"]
# marks  = [2,3,5,8]
# students=[
# ("John",80),
# ("Amy",95),
# ("Mike",75)
# ]

# # 1. map()-> applies a function to every element in an iterable.
# ans = list(map(lambda x: x*2,marks))
# print(ans)
# line();

# # 2. Filter ()
# ans = list(filter(lambda x:x%2==0,marks));
# print(ans)
# line();

# # 3.Sorted()
# ans = sorted(names,key=len)
# print(ans)
# line()

# # 4. min() && max()
# ans = list(min(students, key=lambda x:x[1]))
# print("min(): ", ans)
# ans = list(max(students, key=lambda x:x[1]))
# print("max(): ", ans)
# line();

# # ----------;----------------------------------------------------------------
# #  Topic Name :  Decorators + Type Hints 
# # --------------------------------------------------------------------------


# def logo_dec(func):
#     def wrapper(num):
#         print("\nValue print : ",num)
#         return func(num);
#     return wrapper ;
    
# def decorator(func):
#     def wrapper(num):
#         if not num.isdigit():
#             print("Please enter the correct number")
#             return
#         return func(num)
#     return wrapper

# @logo_dec
# @decorator
# def func(num):
#     print(num)


# func("Rushi")
# func("123")
# line();

# # Exercise 2: Login Required

# is_logged_in = False  #True

# def login_required(func):
#     def wrapper(*args, **kwargs):
#         if not is_logged_in:
#             print("Login failed. Please login first.")
#             return
#         else:
#             print("Login sucessfully")
#             return func(*args, **kwargs)
#     return wrapper;

# @login_required
# def dashboard():
#     print("Welcome to dasboard page");

# dashboard();
# line();

# ----------;----------------------------------------------------------------
#  Topic Name :  Generators
# --------------------------------------------------------------------------

# def numbers():
#     print("Start")

#     yield 10

#     print("Middle")

#     yield 20

#     print("End")

#     yield 30


# gen = numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# line()

# def numbers():
#     for i in range(1,11):
#         yield i


# for num in numbers():
#     print(num)
    
# ----------;----------------------------------------------------------------
#  Topic Name :  String Handling
# --------------------------------------------------------------------------


# name = "rUsHIkEsH ramesh  bhondave"

# print(len(name))

# print(name.lower())

# print(name.upper())

# print("1st letter of every word uppercase " , name.title())

# print(name.capitalize())

# name1 = "    rushikehsh    "
# print(name1)
# print(name1.strip().title())


# ----------;----------------------------------------------------------------
#  Topic Name : Moudule  
# -------------------------------------------------------------------------
# from module_package import *  
# print(__name__)
# print(__package__)

# print(add(2,6))


# if __name__ == "__main__":
#     def mul(a,b):
#         return a - b;

# print(mul(2,6))

# age: int = 25
# name: str = "Rahul" 

# print(__annotations__)

x = 10


# ----------;----------------------------------------------------------------
#  Topic Name : OOPS + Type Hints
# --------------------------------------------------------------------------


# Typing hint 
# Magic methods
# SOLID principles
# Design patterns

# class Product1:
#     pass

#     @classmethod
#     def show(cls):
#         print("cls : ",cls)

# Product1.show()
# line();

########################################################################

# Encapsulation

# 1. @property


class Product:
    
    total_products = 0
    GST = 18
    
    def __init__(self,product_id,name,_price,stock): 
        self.product_id = product_id
        self.name = name
        self._price = _price
        self.stock = stock
        Product.total_products +=1

    @property
    def get_price(self):
        print(f"Prodcut Name = {self.name} and Price {self._price}")
        
    def display(self)->None:
        print("ID:",self.product_id)
        print("Product Name:",self.name)
        print("Product price:",self._price)
        print("Product stock:",self.stock)
        print("============================")

    def cart(self,name,qunatity)->None:
        if not qunatity > 0:
            print("quntity enterd is 0")
            print("============================")
        elif self.stock>=qunatity:
            self.stock-= qunatity
            print("Order is placed",name)
            print("============================")
        else:
            print("Insufficient Stock")
            print("============================")

    def add_Stock(self,name,stock_add):
        if stock_add < 0:
            print("Enter the correct quntity");
            print("============================")
        else:
            if self.name == name:
                self.stock+=stock_add;
                print(f"Stock qunitity is : {self.stock} and Stock name is {name}");
                print("============================")
            else:
                print("Item is not found")
                print("============================")

    @classmethod
    def show_product_count(cls):
        print(f"{Product.total_products} Product is list in the market")



# p1 = Product(1,"Laptop", 50000,20)
# p2 = Product(2,"Phone", 25000,20)
# p3 = Product(3,"Screen", 2000,30)

# p1.display()
# p2.display()
# p3.display()

# p1.get_price

# p1.cart("Laptop",10)
# p2.cart("Phone",5)
# p3.cart("Laptop",101)

# p1.add_Stock("Laptop",10)
# p2.add_Stock("Phone",20)
# p2.add_Stock("Toy",20)

# Product.show_product_count()
# print("============================")

########################################################################

# 3. Inheritance

class Employee:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_details(self):
        print("Name: ",self.name)
        print("Email:",self.email)


class FullTimeEmployee(Employee):
    
    def __init__(self, name, email,monthly_salary):
        super().__init__(name, email)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print("Emp Salary",self.monthly_salary)


class Freelancer(Employee):
    def __init__(self, name, email,hourly_rate, hours_worked):
        super().__init__(name, email)
        self.hourly_rate = hourly_rate
        self .hours_worked = hours_worked

    def calculate_salary(self):
        total_sal = self.hourly_rate*self.hours_worked
        print("Emp Salary",total_sal)



emp1 = FullTimeEmployee(
    "Riya",
    "riya@example.com",
    50000
)

emp2 = Freelancer(
    "Arjun",
    "arjun@example.com",
    500,
    80
)

emp1.show_details()
emp1.calculate_salary()  # 50000
print()
emp2.show_details()
emp2.calculate_salary() # 40000


########################################################################

