monthly_expenses = [2200, 2350, 2600, 2130, 2190]
monthly_expenses
# 1. In Feb, how many dollars you spent extra compare to January?

feb_extra = monthly_expenses[1] - monthly_expenses[0]
feb_extra
# 2. Find out your total expense in first quarter (first three months) of the year.

first_quarter = sum(monthly_expenses[0:2])
first_quarter

# 3. Find out if you spent exactly 2000 dollars in any month

# for i in monthly_expenses:
#     if i == 2000:
#         print("Yes I did spend more than 2000")
#     else:
#         print("No I did not")

2000 in monthly_expenses

# False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

monthly_expenses.append(1980)

print(monthly_expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expenses[3] = monthly_expenses[3] - 200

print(monthly_expenses)
