# No starter code provided — write the full function yourself.
# Function name: split_bill
# Parameters: bill_amount, tip_percent, people
# Must return: each person's share, rounded to 2 decimal places

def split_bill(bill_amount, tip_percent, people):
    tip_amount = bill_amount * (tip_percent/100)
    grand_total = bill_amount + tip_amount
    persons_share = grand_total/people
    return round(persons_share, 2)
print(split_bill(100, 10, 2))