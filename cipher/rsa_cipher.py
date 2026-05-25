class RSACipher:
    def __init__(self):
        pass

    def rsa_encrypt(self, plain_text, e, n):
        # Thuật toán RSA cơ bản xử lý trên số nguyên
        m = int(plain_text)
        c = pow(m, e, n)
        return c

    def rsa_decrypt(self, cipher_text, d, n):
        c = int(cipher_text)
        m = pow(c, d, n)
        return m