employee = {
    "emp_name" : "ram",
    "emp_age" : 20,
    "emp_sal" : 30000
    
    }

text = input("enter a string:")

frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch]=frequency[ch]+1
    else:
        frequency[ch]=1
        
print("character frequency:")

for ch,count in frequency.items():
    print(ch,":",count)