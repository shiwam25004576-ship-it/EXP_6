employee = {
    "emp_name" : "ram",
    "emp_age" : 20,
    "emp_sal" : 30000
    
    }

employee["ID"] = "25BCAR0639"
print("after adding:",employee)

employee["emp_age"] = 20

print("after updating",employee)
del employee["emp_sal"]
print("after deleting",employee)
