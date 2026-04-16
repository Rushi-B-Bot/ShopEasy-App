"""
- Week 1: Python Fundamentals (for FastAPI only)

  - Syntax differences Lists, dicts, sets

  - Functions + Async basics + type hints

  - OOP in Python

  - Error handling

"""

# --------------------------------------------------------------------------
#  Topic Name :- if/else , for , and/or/not,Ternary
# -------------------------------------------------------------------------
def line():
    print("\n------------------------\n")

employees = [
    {"name": "Ravi", "age": 28, "dept": "IT", "salary": 50000, "active": True},
    {"name": "Neha", "age": 32, "dept": "HR", "salary": 45000, "active": True},
    {"name": "Arjun", "age": 26, "dept": "IT", "salary": 60000, "active": True},
    {"name": "Priya", "age": 29, "dept": "Finance", "salary": 55000, "active": True},
    {"name": "Rah", "age": 30,  "dept": "Finance", "salary": 60000, "active": False},

]

# 1) any() --> exist or not
dept = "IT";
if any(emp["dept"]==dept for emp in employees):
    print("dept is exit in the dict");
    line();

# 2) len() --> Length find

print(len(employees))
line();

# 3) all() --> Need to match all (Not compare with any one )

if all(emp["active"] for emp in employees):
    print("All employees are active");
else:
    print("Some employees are active")
line();

if all(emp["age"]>25 for emp in employees):
    print("Y")
else:
    print("N");
line();


# 4) next() --> Find one record at like --> Java -> findFirst()
# 1st found 1st serve  if multiple records present with same detailes 

emp = next((emp for emp in employees if emp["dept"]=="Finance"),None)
print(emp)
line();

# 5) Ternary Operator --> value_if_true if condition else value_if_false 

for emp in employees:
    result = "Active" if emp["active"] else "Inactive"
    print(result)
line();

# 6) f-string (Formatted String)  --> print(f"{emp['']} ")
    # (f"{emp['name']}")
for emp in employees:
    print(f"{emp['name']} and {emp['salary']} is a salary then get bonus is {emp['salary']+5000}")
line();

# ) Practice

for emp in employees:
    if emp["active"]:
        print(emp["name"], "is present in the company")
        if emp["salary"]> 50000:
            print(emp["name"], "Salary is higher than 50k")
line();

# --------------------------------------------------------------------------
#  Topic Name :- Lists, Dicts, Sets
# --------------------------------------------------------------------------

# List :
# --------------------------------------------------------------------------
# Key Rules
# -  Ordered 
# -  Mutable (can change) 
# -  Allows duplicates 
# -  Can store multiple data types 

cart = [1,'a',"Hello",3.5,True,0];

# Print the List 
print(cart[0]);
print("-1 =",cart[-1]);
print(cart[-2]);
print(cart[-3]);
print(cart[1]);
print(cart[2]);
print()

# Adding the element at the end
cart.append("Laptop");
print(cart)
line()

# Adding the element at the index position
cart.insert(1,"Rushi");
print(cart)
line()

# extend() → add multiple items at end
cart.extend(["abc","KIWI"])


# Remove the element by name 
cart.remove("Hello")  
print(cart)
line()

# Remove by the index wise
removed = cart.pop(1)   
print("Removed:", removed)
print("\nUpdated cart:", cart)
line()

# clear() → remove all items
#cart.clear()
#print("clear()",cart)
#line()


# Updating Elements
cart[0] = "Ram"
print(cart)
line()


# Length
# len = len(cart);
# print("Length: ",len);
# line()

users = [
    {"name": "A", "verified": True},
    {"name": "B", "verified": False}
]

# verified = [u for u in users if u["verified"]]  # Only return the true value

verified = [ users for users in users if users["verified"]]
print(verified)
line()


# --------------------------------------------------------------------------
# Dicts :
# --------------------------------------------------------------------------
print("---------- Dicts --------------")
line()
# Key Rules
# - Uses curly braces {}
# - Format → key: value
# - Keys must be: key : value(duplicate ok)
# - Unique
# - Immutable (string, number, tuple)
# - Values can be anything

student = {
    "Name": "Rushi",
    "Age": 25,
    "Company Name": "Edegevere",
    "CTC": "3.6 LPA",
    "Joining Date": "12-03-2025",
    "course": "course"
}

print(student)
line()  

# Accessing Values
print(student.get("Age"))
line()

# Adding / Updating Items
student["grade"] = "A"
student["Age"] = 21
print(student)
line()

# Removing Items
student.pop("course", None)
print(student)
line()

# Looping Through Dictionary
for key in student:
    print(key, student[key])
line()

for key, value in student.items():
    print(key, value)
line()

# Important Methods
print(student.keys())
print(student.values())
print(student.items())
line()

# Checking Keys
if "Name" in student:
    print("Exists")
line()

# Copying Dictionary
new_student = student.copy()
print(new_student)



# --------------------------------------------------------------------------
#  Topic Name :-Functions + async :
# --------------------------------------------------------------------------
print("\n ---------- Functions + async --------------\n")
line()

def home():
    return "Hello Home" 
    
print(home());
line();

def add(a,b):
    return a + b;

ans=add(7,5);
print(ans)
line();

def create_user1(name,age = 25,role="user"):
    return {
        "Name":name,
        "Age" :age,
        "Role":role
    }
    
# result = create_user1("Rushi",role="Admin");  output :- {'Name': 'Rushi', 'Age': Admin, 'Role': 'user'}
result = create_user1("Rushi",role="Admin");
print(result)
line();

def total(*num):
    return sum(num);

print(total(1,2,2))
line();

# Even numbers only prinnt (* args)
def even(*args):
    total = [] ;
    sum = 0;
    for i in args:
        if i % 2 == 0:
            total.append(i); 
        else:
            sum +=i;
    return { "Totals":total, "Sum":sum};

print(even(1,2,4,5,6,9,10,22));
line();


def create_user(**detailes):
    user = {};
    for key , i in detailes.items():
        user[key] = i;
    return user 


user1 = create_user(name="Rushi", age=21, role="Admin")
user2 = create_user(name="Sneha", email="amit@gmail.com", role="User")

print(user1)

print("\n",user2) 
line();


def log_event(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

log_event(error="File not found", code=404)
line();

data = {
    "name": "Rushi",
    "age": 21
}

def show(name, age):
    print(name, age)

show(**data)
line();

# Function with Return Value with Type hints

from typing import TypedDict, List, Tuple, Dict

def totalamt(amount,rate) -> float:
    return amount - rate;

print(totalamt(1.2,2.1))  
line();

def log_data(data: str) -> None:
    print(data)

log_data("Data")
line();

class Student(TypedDict):
    Name: str
    Age: int
    RollNo: int
    Std: str
    Joining_Date: str
    Result: str  # "Pass" | "Fail"


Students: List[Student] = [
    {
        "Name": "Rushi",
        "Age": 25,
        "RollNo": 1,
        "Std": "11th",
        "Joining_Date": "12-01-2018",
        "Result": "Pass"
    },
    {
        "Name": "Amit",
        "Age": 24,
        "RollNo": 2,
        "Std": "12th",
        "Joining_Date": "15-06-2019",
        "Result": "Fail"
    }
]


# 1. Print the all Records 

def get_all_records()->list[Student]:
    return Students;

print(get_all_records());
line();

# 2. Print the all Records as Tuple 
# 👉 The list becomes immutable,
# 👉 BUT the dictionaries inside are STILL mutable 

def get_all_records_as_Tuple() -> Tuple[dict, ...]:
    return tuple(Students)

print(get_all_records_as_Tuple());
line();

# 3. Get record by roll number

def get_record_rollNo(RollNo:int)->list[dict]:
    stu = [ stu for stu in Students if stu["RollNo"]==RollNo];
    return stu


print(get_record_rollNo(1));
line();

# 4. Print aligned data (formatted output)

def print_students_table() -> None:
    print(f"{'Name':<8} {'RollNo':<8} {'Result':<6}")
    for s in Students:
        print(f"{s['Name']:<10} {s['RollNo']:<7} {s['Result']:<6}")
        
print(print_students_table())
line();

# 5. Check record exists

def check_record(data:int | str)->list[dict | str | int] | None: 
    if any(stu["RollNo"]==data for stu in Students):
        print("THe  Record is present")
        
print(check_record(1));
line();

# 6. Multiple roll numbers input

def get_multiple_records(rollNo:list[int])->list[dict | Student]:
    return [stu for stu in Students if stu["RollNo"] in rollNo]

print(get_multiple_records([1,2]));
line();
# 7. Get only names

def get_name_only(name:str)-> tuple:
    return tuple(stu for stu in Students if stu["Name"]==name);

def get_name_only1(name:str | list[str] )-> tuple:
    return tuple(stu for stu in Students if stu["Name"] in name);
print(get_name_only("Rushi"))
line();

print(get_name_only1(["Rushi","Amit"]))
line();

def count_students():
    return len(Students);

print(count_students());
line();

# --------------------------------------------------------------------------
#  Topic Name :  OOP in Python + Error handling
# --------------------------------------------------------------------------

# 1. Class & Object

class User:
    
    def __init__(self,Name,SurName):
        self.Name = Name             # Public variable
        self.SurName = SurName       # Public variable

    def display(self):
        return f"{self.Name} and {self.SurName}";

my_User = User("Rushi","Bhondave")
print(my_User.Name);
print(my_User.SurName);
print(my_User.display());


# 2. Encapsulation (Data Protection)

class BankAccount:
    def __init__(self, name):
        self.name = name              # public
        self._pin = 5046              # protected
        self.__balance = 1000         # private

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"

        if amount > self.__balance:
            return "Insufficient balance"

        self.__balance -= amount
        return f"{amount} withdrawn. Remaining balance: {self.__balance}"

account = BankAccount("Rushi")
print(account.withdraw(500))
print(account._BankAccount__balance) # Python allows to acces the private variable but DON’T DO THIS ❌


#3. Inheritance / Polymorphism

class Payement:

    def __init__(self,amount):
        self._amount = amount

    def pay(self):
        raise NotImplementedError("Subclasses must implement this")

class UPIPayment(Payement):

    def pay(self):
        print("Payment done by UPIPayment")

class CardPayment(Payement):

    def pay(self):
        print("Payment done by CardPayment")

class walletPayment(Payement):

    def pay(self):
        print("Payment done by walletPayment ")


#payment_Type = int(input("Enter the payment menthod 1.UPIPayment 2.CardPayment 3.walletPayment :- "))

#if payment_Type == 1:
payment = UPIPayment(1000);
print(payment.pay());
    
#if payment_Type == 2:
payment = CardPayment(1000);
print(payment.pay());
    
#if payment_Type == 3:
payment = walletPayment(1000);
print(payment.pay());


# Super Keyword

class BaseUser:
    def __init__(self,name):
        self.name = name

class User(BaseUser):
    def __init__(self, name,email):
        super().__init__(name)
        self.email = email
    
    def display(self):
        return f" My name is {self.name} and Mail id:{self.email}"


user = User("Rushi","Rushi@gmail.com");
print(user.display());


# --------------------------------------------------------------------------
#  Topic Name :  Error handling
# --------------------------------------------------------------------------

try:
    x = int("abc");
except ValueError:
    print("Value error")
except TypeError:
    print("Type error")
finally:
    print("Closing the res")





# ----------------------------------------------------------------------------------------------
#  Small project : Student Markshit + Addendance Report
#  Topic's Name :-Functions + Type hints + async + List + Tuple + Dict + *args + *Kwargs
# ----------------------------------------------------------------------------------------------

# Print the all student List 
# Print the specific data
# 2 List comapre and print (Reocrd + Marks)
# Attdeance List Print
# Default attendace findout

Students_Record = [
    {
        "Name": "Rushi",
        "Age": 25,
        "RollNo": 1,
        "Std": "11th",
        "Joining_Date": "12-01-2018"
    },
    {
        "Name": "Amit",
        "Age": 24,
        "RollNo": 2,
        "Std": "12th",
        "Joining_Date": "15-06-2019"
    },
    {
        "Name": "Sneha",
        "Age": 23,
        "RollNo": 3,
        "Std": "10th",
        "Joining_Date": "10-03-2020"
    },
    {
        "Name": "Priya",
        "Age": 22,
        "RollNo": 4,
        "Std": "11th",
        "Joining_Date": "22-07-2021"
    },
    {
        "Name": "Raj",
        "Age": 24,
        "RollNo": 5,
        "Std": "9th",
        "Joining_Date": "22-07-2021"
    }
]

student_Marks_Attdeance = [
    {
        "RollNo": 1,
        "Marks": 
                {
                    "Maths": 45,
                    "English": 65,
                    "Java": 85,
                    "Python": 25,
                    "Marathi": 35,
                    "Science": 100
                },
        "Attdeance" :
                {
                    "Jan" :
                    {
                        "Monday" :  "Present",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Present",
                        "Thursday" :  "Absent",
                        "Friday" :  "Present",
                        "Saturdy" :  "Absent",
                    },
                    "Feb" :
                    {
                        "Monday" :   "Present",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Absent",
                        "Thursday" : "Absent",
                        "Friday" :   "Present",
                        "Saturdy" :  "Absent",
                    },
                    "Mar" :
                    {
                        "Monday" :   "Present",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Absent",
                        "Thursday" : "Absent",
                        "Friday" :   "Present",
                        "Saturdy" :  "Present",
                    },
                }
    },
    
    {
        "RollNo" : 2,
        "Marks" :
            {
                "Maths": 65,
                "English": 95,
                "Java": 85,
                "Python": 65,
                "Marathi": 69,
                "Science": 99.5
            },
        "Attdeance" :
            {
                "Jan" :
                    {
                        "Monday" :  "Present",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Present",
                        "Thursday" :  "Absent",
                        "Friday" :  "Present",
                        "Saturdy" :  "Absent",
                    },
                "Feb" :
                    {
                        "Monday" :   "Absent",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Present",
                        "Thursday" : "Absent",
                        "Friday" :   "Present",
                        "Saturdy" :  "Absent",
                    },
                    "Mar" :
                    {
                        "Monday" :   "Present",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Present",
                        "Thursday" : "Absent",
                        "Friday" :   "Present",
                        "Saturdy" :  "Absent",
                    },
            }
    },
    {
        "RollNo" : 3,
        "Marks" :
            {
                "Maths": 15,
                "English": 75,
                "Java": 50,
                "Python": 65,
                "Marathi": 95,
                "Science": 34
            },
        "Attdeance" :
            {
                "Jan" :
                    {
                        "Monday" :  "Present",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Present",
                        "Thursday" :  "Absent",
                        "Friday" :  "Present",
                        "Saturdy" :  "Absent",
                    },
                "Feb" :
                    {
                        "Monday" :   "Absent",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Present",
                        "Thursday" : "Absent",
                        "Friday" :   "Present",
                        "Saturdy" :  "Absent",
                    },
                    "Mar" :
                    {
                        "Monday" :   "Present",
                        "Tuesday" :  "Absent",
                        "Wensday" :  "Present",
                        "Thursday" : "Absent",
                        "Friday" :   "Present",
                        "Saturdy" :  "Absent",
                    },
            }
    },
]











