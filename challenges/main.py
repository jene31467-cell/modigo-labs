def make_change(amount_owed_cents, amount_paid_cents):
    if amount_paid_cents < amount_owed_cents:
        raise ValueError("Insufficient payment")
    change = amount_owed_cents - amount_paid_cents

    #initialize dictionary with all 4 coins
    denomination = [25, 10, 5, 1]
    result = {25: 1, 10: 0, 5: 1, 1: 2}

    for coin in denomination:
        if change >= coin:
            count = change // coin #how many of this coin
            result[coin] = countchange = change % coin #remaining coin
    return result

    # Your code here