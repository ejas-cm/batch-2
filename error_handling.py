# try
#  ↓
# Run risky code
#  ↓
# Error?
#  ↙️       ↘️
# YES       NO
#  ↓         ↓
# except    else
#  ↓         ↓
# Handle    Success
#     ↘️    ↙️
#    finally
#       ↓
# Always runs

#list handling index error
# numbers = [10, 20, 30]

# try:
#     print(numbers[5])

# except IndexError:
#     print("That position doesn't exist.")

# try:
#     age = int(input("Enter your age: "))
#     print("Your age is:", age)

# except ValueError:
#     print("Please enter numbers only.")

