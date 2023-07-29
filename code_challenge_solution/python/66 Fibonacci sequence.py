# Function to generate Fibonacci sequence
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# User input
n = int(input("Enter the number of terms: "))

# Generate Fibonacci sequence
fib_sequence = fibonacci_sequence(n)

# Print the Fibonacci sequence
print("Fibonacci sequence:")
print(fib_sequence)