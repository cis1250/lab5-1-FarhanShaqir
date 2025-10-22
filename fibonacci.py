def get_number():
    """Prompt the user for a positive integer and validate input."""
    while True:
        try:
            num = int(input("Enter how many terms of the Fibonacci sequence you want: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_fibonacci(n):
    """Generate the Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_fibonacci(sequence):
    """Print the Fibonacci sequence in a readable format."""
    print("Fibonacci Sequence:")
    print(", ".join(str(num) for num in sequence))

def main():
    num_terms = get_number()
    sequence = generate_fibonacci(num_terms)
    print_fibonacci(sequence)

if __name__ == "__main__":
    main()#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
