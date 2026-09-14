

definitions = {
    "Security Parameter": "A way of measuring how hard it is for an adversary to break a Cryptographic Scheme.",
    "Polynomial Time": "A specific formula denoting how long it takes to solve an algortith in the format (O(n^k)) for a nonnegative integer k, and n is the complexity of the input.",
    "Negligible Function": "Function used to define the security of a system. A mathmatical function where the value drops toward zero faster than the inverse.",
    "Indistinguishability": "Making the difference between an encrypted message and a random string indistinguishable.",
}

scheme = print("A Security Scheme is secure if the probability of a successful attack is negligable, meaning that the success chance is less than 1/p(n).")

def stream(S, text_length):
    i - 0
    j = 0
    keystream = []

    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 256
        keystream.append(S[t])

    return keystream