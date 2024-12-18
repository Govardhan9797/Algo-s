def luhn_algorithm(card_number):
    # Convert the card number into a list of integers
    digits = [int(d) for d in str(card_number)]
    
    # Reverse the digits for easier manipulation
    digits.reverse()
    
    # Apply the Luhn algorithm
    for i in range(1, len(digits), 2):  # Double every second digit (starting from index 1)
        digits[i] *= 2
        if digits[i] > 9:  # If doubling produces a number > 9, subtract 9
            digits[i] -= 9
    
    # Calculate the total sum
    total_sum = sum(digits)
    
    # The card is valid if the total sum is divisible by 10
    return total_sum % 10 == 0

# Example usage
card_number = input("Enter the card number to validate: ")
if luhn_algorithm(card_number):
    print(f"{card_number} is valid according to the Luhn algorithm.")
else:
    print(f"{card_number} is invalid according to the Luhn algorithm.")
