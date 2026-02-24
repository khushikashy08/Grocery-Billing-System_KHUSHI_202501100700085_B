
Name: Khushi
Roll No: 202501100700085
Branch: ECE
Section: B

Problem Statement:

A grocery store wants to calculate the total cost of 5 different items purchased by a customer. Each item can be bought in multiple quantities. If the total exceeds Rs. 100, a 10% discount is applied. The program should display the original total, discount, and final payable amount.

# Grocery Billing System

total = 0

for i in range(1, 6):
    price = float(input(f"Enter price of item {i}: "))
    quantity = int(input(f"Enter quantity of item {i}: "))
    total += price * quantity

discount = 0
if total > 100:
    discount = total * 0.10

final_amount = total - discount

print("\n----- BILL DETAILS -----")
print("Original Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
