employee = {
    "emp_name" : "ram",
    "emp_age" : 20,
    "emp_sal" : 30000
    
    }

print("keys:")
print(employee.keys())

print("values:")
print(employee.values())

print("items:")
print(employee.items())

print("name:",employee.get("emp_name"))
print("age:",employee.get("emp_age"))
print("sal:",employee.get("emp_sal"))

employee.update({"age":20,"sal":30000})

print("after updating")
print(employee)
