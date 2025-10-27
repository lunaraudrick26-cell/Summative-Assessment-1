# Exercise 10: Is it even? - OPTIMIZED

def check_even_odd(num):
    return f"The number {num} is {'even' if num % 2 == 0 else 'odd'}."

def main():
    try:
        num = int(input("Enter a number: "))
        print(check_even_odd(num))
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()