age = int(input("Age: "))

# .strip().lower() ensures "Yes", "YES", or "yes " all work correctly
has_id_input = input("Do you have an ID (yes/no)? ")

# This makes has_id True only if they typed "yes"
has_id = (has_id_input == "yes")

if age >= 18 and has_id:
    print("access")
else:
    print("not")