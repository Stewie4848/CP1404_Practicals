FILE = "name.txt"

name = input("Enter name")
out_file = open(FILE, 'w')
print(name, file=out_file)
out_file.close()

in_file = open(FILE, 'r')
name = in_file.read().strip()
in_file.close()
print("Your name is ", name)

numbers_file = open("numbers.txt", 'r')
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
numbers_file.close()
print(number1 + number2)

total = 0
numbers_file = open("numbers.txt", 'r')
for line in numbers_file:
    number = int(line)
    total += number
print(total)
