
# Armstrong Number - 153 --> 1^3 + 5^3 + 3^3 = 153

n = int(input("Enter the number: "))

original = n

number_of_digits = len(str(n))

sum = 0

while n>0:
    digit = n % 10
    sum = sum + digit**number_of_digits
    n = n // 10

if original == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number.")



# Output:

# Enter the number: 153
# Armstrong number

