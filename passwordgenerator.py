import string
import random
if __name__ == "__main__":
    string_container_1 = string.ascii_lowercase
    # print(string_container_1)
    string_container_2 = string.ascii_lowercase
    # print(string_container_2)
    string_container_3 = string.digits
    # print(string_container_3)
    string_container_4 = string.punctuation
    # print(string_container_4)
    password_length = int(input("Enter the length of the password:"))
    letter_container = list()
    letter_container.extend(list(string_container_1))
    letter_container.extend(list(string_container_2))
    letter_container.extend(list(string_container_3))
    letter_container.extend(list(string_container_4))
    random.shuffle(letter_container)
    password = (''.join(letter_container[:password_length]))
    print('Your Password is {}'.format(password))
