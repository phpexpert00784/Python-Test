class FibFact:
    
    #do Factorial
    def factorial(self, n):
       
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    #do Fibobacci
    def fibonacci(self, n):
       
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    math_ops = FibFact()

    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")
    number = int(input("Enter a number: "))
    
    if choice == "1":
        ans = math_ops.factorial(number)

    elif choice == "2":
        ans = math_ops.fibonacci(number)

    else:
        ans = "Invalidhoice"

    print("\nFinal result:", ans)