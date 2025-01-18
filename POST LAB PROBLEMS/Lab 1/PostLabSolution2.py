
filename = input("Enter the filename: ")

with open(filename, "w") as file:
    print("Enter text to continue writing to the file. Otherwise enter 'exit'")

    while True:
        user_input = input()

        if user_input == 'exit':
            break

        file.write(user_input + "\n")

num = -1
while num != 0:
    num = int(input("Enter the number of the line you want to print:  "))


    with open(filename, "r+") as file:
        content = file.readlines()

        if num ==0:
            break
        elif 1<=num<=len(content):
            print("Line %d is: " %(num), end=" ")
            print(content[num-1])
        else:
            print("Invalid line number.")

print("Program terminated.")