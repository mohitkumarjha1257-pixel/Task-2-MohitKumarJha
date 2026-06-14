# Phase 1: Initialization (Memory)
total = 0.0

# Phase 2: The Continuous Audit Loop
def tracker():
    global total
    while True:
        user_input = input("Enter expense amount: ")
        if user_input.lower() == 'quit':
            break
        
        try:
            expense = float(user_input)
            
            total += expense
            print("Added! Current running total: $", total)

        except ValueError:
            print("Invalid Data. Please enter a valid number.")
        
def menu():
    print("--- Expense Tracker ---")
    print("Type 'quit' to exit and see your final total.\n")
    print("Enter your expense amounts one by one.")
    tracker()
    
menu()
    
# Phase 3: Output Stream
print("\n" + "="*30)
print("FINAL TOTAL: $",total)
print("="*30)