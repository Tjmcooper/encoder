def encode():
    password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!\n")
    code = []
    for i in password:
        encoded = (int(i) + 3) % 10
        code.append(encoded)
    code = ''.join(str(j) for j in code)
    return

def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        selection = input("Please enter an option: ")
        if selection == '1':
            encode()
        elif selection == '2':
            decode()
        elif selection == '3':
            break
        else:
            continue
