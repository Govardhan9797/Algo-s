# Luhn Algorithm Validator

This repository contains a Python implementation of the **Luhn Algorithm**, a checksum formula used to validate various identification numbers such as credit card numbers. The program checks if a given number is valid according to the Luhn algorithm.

---

## Features
- Validates numeric input based on the Luhn algorithm.
- Detects whether a credit card number or similar identifier is valid.
- Simple, efficient, and easy to use.

---

## How the Luhn Algorithm Works
1. Start from the rightmost digit (check digit).
2. Double every second digit from the right.
3. If the doubled value is greater than 9, subtract 9 from it.
4. Sum all the digits.
5. If the total is divisible by 10, the number is valid.

---

## Requirements
- Python 3.6 or later.

---

## Usage

### Input
The program prompts the user to enter a number for validation.

### Output
- Prints whether the input number is valid or invalid based on the Luhn algorithm.

---

## Example
### Input:
```
Enter the card number to validate: 4539148803436467
```

### Output:
```
4539148803436467 is valid according to the Luhn algorithm.
```

---

## Code
Here is the Python implementation of the Luhn algorithm:

```python
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
```

---

## Running the Program
1. Clone or download this repository.
2. Run the Python file in your terminal or IDE.
3. Enter a number when prompted.

---

## Contributing
Feel free to contribute by submitting issues or pull requests. All contributions are welcome!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- The Luhn algorithm was created by **Hans Peter Luhn**.
- This implementation is inspired by the simplicity of checksum validation systems.



## Author - Govardhan Reddy D
