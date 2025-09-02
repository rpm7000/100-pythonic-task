# Print Fibonacci sequence up to n terms

n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("❌ Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence: ")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
        count += 1
