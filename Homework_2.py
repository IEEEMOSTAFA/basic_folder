 
# def find_largest(num1, num2, num3):
#     largest = num1
#     if num2 > largest:
#         largest = num2
#     if num3 > largest:
#         largest = num3
#     return largest

# def main():
#     num1 = float(input("Enter the first number:"))
#     num2 = float(input("Enter the second number:"))
#     num3 = float(input("Enter the Third number:"))
#     largest = find_largest(num1, num2, num3)
#     print(f"The largest number is {largest}.")

# if __name__ == "__main__":
#     main()


# find largest three number
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the Third number:"))

if(num1 > num2) and (num1 > num3):
   largest = num1
elif(num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
print('The largest number is',largest)   