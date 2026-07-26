"""
- Week 2: Backend-Specific Python + SQL

-  Models(Pydantic) +  Decorater

- JSON handling

- SQL basics

- SQLAlchemy ORM (FastAPI standard)

- Environment variables (.env)

- Logging

-----------------------------------------------------------------

Today +  Tommarrow

✅  BaseModel
✅  Field
✅  field_validator
✅  model_validator
✅  typing (List, Optional, etc.) + Optional Fields
✅  Response Models (FastAPI)
✅  EmailStr / HttpUrl / types
✅  parse_obj / model_validate
✅  Serialization (model_dump)
✅  Config / model_config +ORM Mode (DB integration)
✅  Schema generation
✅  Settings (BaseSettings) ⚠️ VERY IMPORTANT
✅  Higher-order functions

-----------------------------------------------------------------

"""


# --------------------------------------------------------------------------
#  Topic Name :-  Models + __name__  + pydantic
# -------------------------------------------------------------------------

# Models :
import random
from demo_module import *

result = add();
result1= sub();

print(result);
print(result1);

print(random.randint(1, 10))  
line();

# 1. BaseModel (CORE) --> Validate API input/output

from pydantic import BaseModel , Field , ValidationError,field_validator,model_validator

class User(BaseModel):
    age: int
    name: str

    def get_data(self):
        return f"{self.name} and {self.age}"

user = User(name="Rushi", age="569");

print("pydantic module : ", user.get_data()) 
line();

# 2. feild(); ---> is used to add rules, constraints, and metadata to a model field.
# 3. field_validator() --> It runs automatically when you create the object  (No need to call and print)
# 4. model_validator() ---> checks the whole model (all fields together)
#                        mode="Before" --> Called when the cls & dict build before all custom valiadtion
#                        mode="after"  --> Runs after object is created
#                         | Feature        | before      | after    |
#                         | -------------- | ----------- | -------- |
#                         | Input type     | dict        | object   |
#                         | Access fields  | data["age"] | self.age |
#                         | Object exists? | ❌ No       | ✅ Yes   |

discount = 50

class Students1(BaseModel):
    name: str = Field(min_length=3, max_length=12)
    age: int = Field(gt=18, lt=60)
    amount: float = Field(gt=0)

    
    @field_validator("amount")
    def check_amt(cls,v):
        if v>10000:
            raise ValueError("Amount is greater than 10k")
        return v;
    
    @model_validator(mode="after")
    def check_discount(self):
    
        if self.amount < discount:
            raise ValueError("Discount cannot be greater than price")
        return self

    def get_Discount(self):
        
        if self.age < 25:
            total_price_pay = self.amount - discount;    

        elif self.age > 25:
            total_price_pay = self.amount - discount;
        
        return f"You have paid {total_price_pay} and {discount} Rs. discount got on this subscrition"
try:
    stu = Students1(name="Rushi", age=150, amount=100)
    print(stu)
    line();
    print(stu.get_Discount())
    line();

except ValidationError as e:
    print("❌ Invalid input!")
    
    for error in e.errors():
        field = error["loc"][0]
        message = error["msg"]
        value = error["input"]
        print("\n----------------")
        print(f"👉  Field: {field}")
        print(f"👉 Problem: {message}")
        print(f"👉 Given value: {value}")

line();

# 5. typing ---> typing is used to define the type/shape of data
#👉 Built-in types (str, int, float) are enough for simple fields
#👉 typing is needed for:
# Key Points :
# - complex data
# - flexible structures
# - optional/multiple values

from typing import List, Dict, Tuple

items: List[str] = ["apple", "banana"]
user: Dict[str, str] = {"name": "Aman"}
coords: Tuple[float, float] = (18.52, 73.85)

print(items)
line();


# --------------------------------------------------------------------------
#  Topic Name :-   Decorater 
# -------------------------------------------------------------------------

def check_name_age(func):
    def wrap(name,age):
        if not isinstance(name,str) or name.strip== " " or not isinstance(age,int):  #strip = remove spaces
            return "Please Check the input values"
        return func(name,age);
    return wrap

@check_name_age
def get_name(name: str, age: int):
    return f"My name is {name} and my age is {age}"


#print(get_name("Rushi", 55))
#line();



# --------------------------------------------------------------------------
#  Topic Name :-  Literal 
# -------------------------------------------------------------------------

# 1. Literal ----> Restrict values to fixed options

from typing import Literal

method = Literal["UPI","Card","wallet"];
print(method);
line();