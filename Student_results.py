# Given result list
result = [["m1", 42, 23, 17], ["m2", 43, 23, 21], ["m3", 45, 20, 12], ["m4", 46, 23, 24], ["a5", 32, 21, 14]]

# Add a sum column to each sublist
for i in result:
    s = sum(i[1:])  # Calculate the sum of the elements starting from index 1
    i.append(s)  # Append the sum to the sublist

# Print the updated result list
print(result)

# Initialize variables to calculate theory, practical/viva totals, and count
th = 0
vp = 0
c = 0

# Iterate through the updated result list to calculate totals
for sm in result:
    th += sm[1]  # Sum of theory marks
    vp += sm[2] + sm[3]  # Sum of practical and viva marks
    c += 1  # Count of students

# Print the number of students
print(c)

# Calculate the average theory marks
pr = th / c
print(pr)

# Determine pass/fail status in theory
if pr >= 33:
    print("pass in theory")
else:
    print("fail in theory")

# Calculate the average practical and viva marks
prt = vp / c
print(prt)

# Determine pass/fail status in practical and viva
if prt >= 33:
    print("pass in practical and viva")
else:
    print("fail in practical and viva")

# Calculate the total average marks
total = (th + vp) / c
print(total)

# Determine overall pass/fail status
if total >= 50.0:
    print("pass in o level")
else:
    print("you are fail")
