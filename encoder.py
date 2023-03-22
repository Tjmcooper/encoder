def encode():
    password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!\n")
    code = []
    for i in password:
        encoded = (int(i) + 3) % 10
        code.append(encoded)
    code = ''.join(str(j) for j in code)
    return code

def decode(code):
    new_password = ''
    for i in code:
        i = int(i)
        i -= 3
        i = str(i)
        new_password += i
    return new_password




def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        selection = input("Please enter an option: ")
        if selection == '1':
            code = encode()
        elif selection == '2':
            new_password = decode(code)
            print(f"The encoded password is {code}, and the original password is {new_password}\n")

        elif selection == '3':
            break
        else:
            continue

main()

