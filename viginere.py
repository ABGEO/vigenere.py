"""
Module viginere.py
"""


class Viginere:
    """
    Class for text encryption and decryption
    with viginere Cipher.
    """

    __author__ = "Temuri Takalandze <me@abgeo.dev>"
    __copyright__ = "Copyright 2019, abgeo.dev"
    __license__ = "MIT"
    __version__ = "0.9"
    __maintainer__ = "Temrui Takalandze"
    __email__ = "me@abgeo.dev"
    __status__ = "Development"

    @classmethod
    def encrypt(cls, text, key):
        """
        Encrypt given string
        :param text Text for encryption.
        :param key  Encryption key.
        :return: Encrypted string
        """

        encrypted = ''
        steps = 0
        for char in text:
            key_index = steps % len(key)
            steps += 1
            shift = 97 if char.islower() else 65

            if ord(char) in [i for i in range(65, 91)] + [i for i in range(97, 123)]:
                new_char_code = (ord(char) + key_index - shift) % 26 + shift
            else:
                new_char_code = ord(char)

            encrypted += chr(new_char_code)

        if type(text) is tuple:
            return tuple(encrypted)
        elif type(text) is list:
            return list(encrypted)

        return encrypted

    @classmethod
    def decrypt(cls, text, key):
        """
        Decrypt given string
        :param text Text for decryption.
        :param key  Decryption key.
        :return: Decrypted string
        """

        decrypted = ''
        steps = 0
        for char in text:
            key_index = steps % len(key)
            steps += 1
            shift = 97 if char.islower() else 65

            if ord(char) in [i for i in range(65, 91)] + [i for i in range(97, 123)]:
                new_char_code = (ord(char) - key_index - shift) % 26 + shift
            else:
                new_char_code = ord(char)

            decrypted += chr(new_char_code)

        if type(text) is tuple:
            return tuple(decrypted)
        elif type(text) is list:
            return list(decrypted)

        return decrypted
