
# Count No. of digit

n = int(input("Enter the number: "))

count = 0

while n>0:
    digit = n%10
    count = count + 1
    n= n//10
print(count)

# Output:

# Enter the number: 123
# 3

