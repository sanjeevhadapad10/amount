# Bank Account Balance Program

# Ask user for initial balance and deposit amount
initial_balance = float(input("Enter Initial Balance: ₹"))
deposit_amount = float(input("Enter Deposit Amount: ₹"))

# Calculate new balance after deposit
new_balance = initial_balance + deposit_amount

# Display results
print(f"Initial Balance: ₹{initial_balance}")
print(f"Deposit: ₹{deposit_amount}")
print(f"New Balance after deposit: ₹{new_balance}")
withdraw_amount = float(input("Enter Withdraw Amount: ₹"))

# Calculate final balance
final_balance = balance_after_deposit - withdraw_amount