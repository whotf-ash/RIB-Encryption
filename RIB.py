def text_to_binary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    binary_values = binary.split(' ')
    text = ''.join(chr(int(char, 2)) for char in binary_values)
    return text

def rail_fence_encrypt(text, rails=3):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in text:
        fence[rail].append(char)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    encrypted_text = ''.join(''.join(rail) for rail in fence)
    return encrypted_text

def rail_fence_decrypt(encrypted_text, rails=3):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in encrypted_text:
        fence[rail].append(None)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    index = 0
    for i in range(rails):
        for j in range(len(fence[i])):
            fence[i][j] = encrypted_text[index]
            index += 1
            rail += direction
            
            if rail == rails - 1 or rail == 0:
                direction *= -1
    
    decrypted_text = ''
    rail = 0
    direction = 1
    for _ in range(len(encrypted_text)):
        decrypted_text += fence[rail].pop(0)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction *= -1
    
    return decrypted_text




def add_a_every_2_letters(data):
    result = ''
    for _ in range(2):
        for i in range(0, len(data), 2):
            result += data[i:i+2] + 'a'
        data = result
        result = ''
    return data


def add_z_every_3_letters(data2):
    result = ''
    for _ in range(2):
        for i in range(0, len(data2), 3):
            result += data2[i:i+3] + 'z'
        data2 = result
        result = ''
    return data2


def add_o_every_4_letters(data3):
    result = ''
    for _ in range(2):
        for i in range(0, len(data3), 4):
            result += data3[i:i+4] + 'o'
        data3 = result
        result = ''
    return data3


def remove_z_every_3_letters(data):
    result = ''
    for _ in range(2):
        for i in range(0, len(data), 4):
            result += data[i:i+3]
        data = result
        result = ''
    return data


def remove_o_every_4_letters(data):
    result = ''
    for _ in range(2):
        for i in range(0, len(data), 5):
            result += data[i:i+4]
        data = result
        result = ''
    return data


def remove_a_every_2_letters(data):
    result = ''
    for _ in range(2):
        for i in range(0, len(data), 3):
            result += data[i:i+2]
        data = result
        result = ''
    return data


def decrypt_result3(data):
    decrypted_data = remove_o_every_4_letters(data)
    decrypted_data = remove_z_every_3_letters(decrypted_data)
    decrypted_data = remove_a_every_2_letters(decrypted_data)
    return decrypted_data


def main():
    data = input("Please enter some data: ")

    data1 = data.replace(' ', '!')
    
    print("You entered:", data)
    
    print("Select an option:")
    print("1. Encrypt Data")
    print("2. Decrypt Data")
    option = input("Enter your choice (1 or 2): ")
    
    if option == '1':
        result = add_a_every_2_letters(data1)
        result1 = add_z_every_3_letters(result)
        result2 = add_o_every_4_letters(result1)
        encrypted_text = rail_fence_encrypt(result2, rails=3)
        binary = text_to_binary(encrypted_text)
        print("Encrypted Data:", binary)
    elif option == '2':
        text = binary_to_text(data)
        decrypted_text = rail_fence_decrypt(text, rails=3)
        result = decrypted_text.replace('!', ' ')
        decrypted_data = decrypt_result3(result)
        decrypted_data = decrypted_data
        print("Decrypted Data:", decrypted_data)
    else:
        print("Invalid option!")


if __name__ == "__main__":
    main()
