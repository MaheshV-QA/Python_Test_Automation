# loop_control_demo.py

# =========================================
# Demonstrating `break`
# =========================================
print("########## break ##########")

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    else:
        print(i)

# =========================================
# Demonstrating `continue`
# =========================================
print("\n########## continue ##########")

for i in range(10):
    if i == 5:
        continue  # Skip this iteration when i is 5
    else:
        print(i)

# =========================================
# Demonstrating `pass`
# =========================================
print("\n########## pass ##########")

for i in range(10):
    if i == 5:
        pass  # Does nothing; just a placeholder
        print(i)  # Still prints 5
    else:
        print(i)
