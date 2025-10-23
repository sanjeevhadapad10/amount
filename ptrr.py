
P = float(input("Enter Principal Amount (₹): "))
R = float(input("Enter Rate of Interest (%): "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100

print("Simple Interest: ₹", SI)
CI = P * ((1 + R / 100) ** T) - P
print("Compound Interest: ₹", round(CI, 2))