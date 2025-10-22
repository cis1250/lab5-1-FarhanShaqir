def get_number():
    while True:
        num = input("Enter how many terms of the Fibonacci sequence you want: ")
        if num.isdigit() and int(num) > 0:
            return int(num)
        else:
            print("Please enter a positive integer.")

def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_fibonacci(sequence):
    print("Fibonacci Sequence:")
    print(", ".join([str(x) for x in sequence]))

def main():
    num_terms = get_number()
    sequence = generate_fibonacci(num_terms)
    print_fibonacci(sequence)

main()
