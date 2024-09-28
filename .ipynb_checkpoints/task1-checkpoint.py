#This script will prompt the user to input 3 integers; then, it will sort them and output sorted values

#prompting the user to enter integers
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: ")) 

if a > b:
    a, b = b, a #swapping values
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if b > c:
    b, c = c, b

print()
print(f'Your integers sorted: {a},{b},{c}')
print()
print("Smile please:) today is a great day")
print()