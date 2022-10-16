import random
from elements import letters, numbers, symbols

total_number = int(input("Enter number of characters: "))
string_number = int(input("Enter number of strings: "))
symbol_number = int(input("Enter number of symbols: "))
num_number = int(input("Enter number of numbers: "))

password = []
final = ""
if (string_number+symbol_number+num_number) == total_number:
    for i in range(0, string_number+1):
        password.append(random.choice(letters))
    for i in range(0, symbol_number+1):
        password.append(random.choice(symbols))
    for i in range(0, num_number+1):
        password.append(random.choice(numbers))
    for i in range(0, total_number+1):
        final += password[i]
    print(f'{final}')
else:
    print("The number ratio is wrong")
