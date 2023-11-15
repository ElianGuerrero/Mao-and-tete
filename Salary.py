#Tete salary
https://replit.com/join/mnsbnckrwx-elianguerrero1

employees = input("Is there more than 1 employee?")
if employees == "yes":
  print("How many employees are there?")
  employees = int(input())
  for x in range(employees):
    print("What is the employee's name?")
    name = input()
    print("What is the employee's base wage?")
    wage = float(input())
    print("What are the total sales by the employee?")
    sales = float(input())
    
    if sales > 7000:
      total = wage + (sales * .15)
    elif 3500 <= sales <= 7000:
      total = wage + (sales * .10)
    elif sales < 3500:
      total = wage + (sales * .07)
    print(name, "earned", total)
elif employees == "no":
  print("What is the employee's name?")
  name = input()
  print("What is the employee's base wage?")
  wage = float(input())
  print("What are the total sales by the employee?")
  sales = float(input())
  
  if sales > 7000:
    total = wage + (sales * .15)
  elif 3500 <= sales <= 7000:
    total = wage + (sales * .10)
  elif sales < 3500:
    total = wage + (sales * .07)
  print(name, "earned", total)
