from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        pass

    def caesar_encrypt_text(self, plain_text, key):
        result = ""
        # Duyệt qua từng ký tự trong chuỗi gốc
        for i in range(len(plain_text)):
            char = plain_text[i]
            
            # Mã hóa ký tự viết hoa
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            # Mã hóa ký tự viết thường
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            # Giữ nguyên khoảng trắng hoặc ký tự đặc biệt
            else:
                result += char
        return result

    def caesar_decrypt_text(self, cipher_text, key):
        # Giải mã Caesar bản chất là mã hóa ngược lại với số bước dịch chuyển là -key
        return self.caesar_encrypt_text(cipher_text, -key)