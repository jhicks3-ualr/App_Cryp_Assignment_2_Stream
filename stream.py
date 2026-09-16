import textwrap


def answers():
    definitions = {
        "Security Parameter": "A way of measuring how hard it is for an adversary to break a Cryptographic Scheme.",
        "Polynomial Time": "A specific formula denoting how long it takes to solve an algortith in the format (O(n^k)) for a nonnegative integer k, and n is the complexity of the input.",
        "Negligible Function": "Function used to define the security of a system. A mathmatical function where the value drops toward zero faster than the inverse.",
        "Indistinguishability": "Making the difference between an encrypted message and a random string indistinguishable.",
    }

    scheme = "A Security Scheme is secure if the probability of a successful attack is negligable, meaning that the success chance is less than 1/p(n)."

    while True:
        print("Please select from the below menu: ")
        select_1 = input("1. View vocabulary definitions. \n" \
        "2. View Definition of Security Scheme.\n" \
        "3. Exit to the previous menu.\n" \
        "Input: ")

        match select_1:
            case '1':
                for key, value in definitions.items():
                    text = f"{key}: {value}"
                    wrapping_1 = textwrap.wrap(text, width=100)
                    for line in wrapping_1:
                        print(line)
                    print()
                input("Press any key to continue...")

            case '2':
                print("How can we prove that the security scheme is secure?")
                wrapping_2 = textwrap.wrap(scheme, width=100)
                for line in wrapping_2:
                    print(line)
                input("Press any key to continue...")

            case '3':
                return

            case _:
                print("Invalid input, please enter 1, 2, or 3.\n")

def rc4_init(key: bytes):
    s = list(range(256))
    j = 0
    key_length = len(key)

    for i in range(256):
        j = (j + s[i] + key[i % key_length]) % 256
        s[i], s[j] = s[j], s[i]

    return s

def rc4_prga(s: list, data_length: int):
    i = 0
    j = 0
    keystream = bytearray()

    for _ in range(data_length):
        i = (i + 1) % 256
        j = (j + s[i]) % 256

        s[i], s[j] = s[j], s[i]

        t = (s[i] + s[j]) % 256
        keystream.append(s[t])

    return keystream

def rc4_crypt(key: bytes, data: bytes) -> bytes:
    s = rc4_init(key)
    keystream = rc4_prga(s, len(data))
    return bytes(b1 ^ b2 for b1, b2 in zip(data, keystream))

def main():

    while True:
        print(" SELECTION MENU ".center(100,'-'))
        selection = input("Please select one of the following options:\n" \
        "1. See Vocabulary and Security Scheme Definitions.\n" \
        "2. Use an RC4 Psuedo Random Number Generator to encrypt and decrypt a message.\n" \
        "3. Exit the program.\n" \
        "Input: ")

        match selection:

            case '1':
                answers()
            case '2':
                print(" RC4 Encryption/Decryption ".center(100,'-'))

                message = input("Enter a message you would like to encrypt:\n")
                key = input("Please enter a secret key: \n")

                message_bytes = message.encode('utf-8')
                key_bytes = key.encode('utf-8')

                ciphertext = rc4_crypt(key_bytes, message_bytes)

                decrypted_bytes = rc4_crypt(key_bytes, ciphertext)

                print(f"Encrypted message in hex: {ciphertext.hex()}")
                print(f"Decrypted message: {decrypted_bytes.decode('utf-8')}")
                input("Press any key to continue...")

            case '3':
                print("Exiting Program...")
                quit()
            case _:
                print("Invalid input, please enter 1, 2, or 3.\n")


main()