# simple_interest.py
# Program to calculate Simple Interest

# Initialize values directly (no user input)
principal = 10000   # Principal amount
rate = 5            # Rate of interest in percent
time = 3            # Time in years

simple_interest = (principal * rate * time) / 100

print("----- Simple Interest Calculator -----")
print(f"Principal Amount: ₹{principal}")
print(f"Rate of Interest: {rate}%")
print(f"Time Period: {time} years")
print(f"Calculated Simple Interest: ₹{simple_interest}")