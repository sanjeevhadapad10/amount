initial_balance = float(input("Enter Initial Balance: ₹"))
deposit_amount = float(input("Enter Deposit Amount: ₹"))

new_balance = initial_balance + deposit_amount

print(f"Initial Balance: ₹{initial_balance}")
print(f"Deposit: ₹{deposit_amount}")
print(f"New Balance after deposit: ₹{new_balance}")
withdraw_amount = float(input("Enter Withdraw Amount: ₹"))

final_balance = balance_after_deposit - withdraw_amount

# Display final result
print(f"Withdraw: ₹{withdraw_amount}")
print(f"Final Balance: ₹{final_balance}")