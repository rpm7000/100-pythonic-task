
print("Chooes + - *  /")
choose = input("What Will You Choose: ")

if choose not in["+", "-", "*", "/"]:
    print("Invalid operator!")
    exit()
   
try: 
    user_input_a = float(input("Enter: "))
    print(choose)
    user_input_b = float(input("Enter: "))
except ValueError:
    print("Please enter valid numbers only.")

if choose == "+":
    print(f"= {user_input_a + user_input_b}")
elif choose == "-":
    print(f"= {user_input_a - user_input_b}")
elif choose == "*":
    print(f"= {user_input_a * user_input_b}")
elif choose == "/":
    print(f"= {user_input_a / user_input_b}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















    
    
    