# print prime number and count the prime number accurance present in that range
def prime_number(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    if count == 2:
        print("Number is prime")
    else:
        print("Number is not a prime")


number = int(input("Give your number to check the number : "))
prime_number(number)
