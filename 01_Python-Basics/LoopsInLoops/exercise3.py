number = input()
non_prime_sum = 0
prime_sum = 0

while number != "stop":
    number = int(number)
    if number < 0:
        print("Number is negative.")
    else:
        for i in range (2, number):
            if number % i == 0:
                non_prime_sum += number
                break
        else:
            prime_sum += number
    number = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
