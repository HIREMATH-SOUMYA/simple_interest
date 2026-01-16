def simple_interest(principal, rate, time):
    return principal * rate * time / 100 


if __name__ == "__main__":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate: "))
    time = float(input("Enter the time: "))

    print("Simple Interest:", simple_interest(principal, rate, time))
