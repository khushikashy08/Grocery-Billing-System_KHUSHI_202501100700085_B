# Grocery Store Billing System

# Initialize total cost
total = 0

# Loop to accept input for 5 items
for i in range(1, 6):
    # Accept price of item
    price = float(input(f"Enter price of item {i}: "))
    
    # Accept quantity of item
    quantity = int(input(f"Enter quantity of item {i}: "))
    
    # Calculate cost for current item and add to total
    total += price * quantity

# Initialize discount
discount = 0

# Apply 10% discount if total exceeds Rs.100
if total > 100:
    discount = total * 0.10

# Calculate final amount
final_amount = total - discount

# Display results
print("\n----- BILL DETAILS -----")
print("Original Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)