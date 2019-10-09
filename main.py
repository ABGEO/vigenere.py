from viginere import Viginere as vC

if __name__ == '__main__':
    # Define keys.
    key_string = 'somekey'
    key_tuple = tuple(key_string)
    key_list = list(key_string)

    # Define text for encryption.
    text_string = 'Hello, World!'
    text_tuple = tuple(text_string)
    text_list = list(text_string)

    # Encrypt / Decrypt using strings.
    encrypted_string = vC.encrypt(text_string, key_string)
    decrypted_string = vC.decrypt(encrypted_string, key_string)

    # Encrypt / Decrypt using tuples.
    encrypted_tuple = vC.encrypt(text_tuple, key_tuple)
    decrypted_tuple = vC.decrypt(encrypted_tuple, key_tuple)

    # Encrypt / Decrypt using lists.
    encrypted_list = vC.encrypt(text_list, key_list)
    decrypted_list = vC.decrypt(encrypted_list, key_list)

    # Print results.
    print('Encrypted string: ', encrypted_string)
    print('Decrypted string: ', decrypted_string)

    print('Encrypted tuple: ', encrypted_tuple)
    print('Decrypted tuple: ', encrypted_tuple)

    print('Encrypted list: ', encrypted_list)
    print('Decrypted list: ', decrypted_list)
