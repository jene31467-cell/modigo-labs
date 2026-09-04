def fizzbuzz_counts(n):
    counts = {
        "fizz": 0, 
        "buzz": 0, 
        "fizzbuzz": 0
        }
    
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            counts["fizzbuzz"] += 1
        elif number % 3 == 0:
            counts["fizz"] += 1
        elif number % 5 == 0:
            counts["buzz"] += 1
        # TODO: check divisibility by 3 and 5, and increment the correct key in `counts`
    return counts
print(fizzbuzz_counts(15))