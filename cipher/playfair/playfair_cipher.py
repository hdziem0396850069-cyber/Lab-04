class PlayfairCipher:
    def __init__(self):
        pass

    def create_matrix(self, key):
        # Chuẩn hóa key: viết hoa, đổi J thành I, bỏ ký tự không phải chữ cái
        key = key.upper().replace('J', 'I')
        cleaned_key = ""
        for char in key:
            if char.isalpha() and char not in cleaned_key:
                cleaned_key += char
                
        # Định nghĩa bảng chữ cái (bỏ J)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        
        # Tạo danh sách các ký tự trong ma trận 5x5
        matrix_chars = list(cleaned_key)
        for char in alphabet:
            if char not in matrix_chars:
                matrix_chars.append(char)
                
        # Chia thành ma trận 5 hàng, mỗi hàng 5 ký tự
        matrix = [matrix_chars[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def _find_position(self, matrix, char):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char:
                    return r, c
        return None

    def _prepare_text(self, text):
        # Chuẩn hóa văn bản đầu vào
        text = text.upper().replace('J', 'I')
        cleaned_text = [char for char in text if char.isalpha()]
        
        prepared_text = ""
        i = 0
        while i < len(cleaned_text):
            char1 = cleaned_text[i]
            prepared_text += char1
            
            # Nếu là ký tự cuối cùng của chuỗi lẻ
            if i + 1 == len(cleaned_text):
                prepared_text += 'X'
                break
                
            char2 = cleaned_text[i+1]
            # Nếu 2 ký tự trùng nhau trong một cặp, chèn 'X' vào giữa
            if char1 == char2:
                prepared_text += 'X'
                i += 1
            else:
                prepared_text += char2
                i += 2
        return prepared_text

    def playfair_encrypt(self, plain_text, key):
        matrix = self.create_matrix(key)
        prepared_text = self._prepare_text(plain_text)
        cipher_text = ""
        
        for i in range(0, len(prepared_text), 2):
            char1, char2 = prepared_text[i], prepared_text[i+1]
            r1, c1 = self._find_position(matrix, char1)
            r2, c2 = self._find_position(matrix, char2)
            
            if r1 == r2:  # Cùng hàng: dịch sang phải (vòng lại đầu hàng nếu chạm biên)
                cipher_text += matrix[r1][(c1 + 1) % 5]
                cipher_text += matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:  # Cùng cột: dịch xuống dưới (vòng lại đầu cột nếu chạm biên)
                cipher_text += matrix[(r1 + 1) % 5][c1]
                cipher_text += matrix[(r2 + 1) % 5][c2]
            else:  # Khác hàng khác cột: tạo hình chữ nhật, đổi cột cho nhau
                cipher_text += matrix[r1][c2]
                cipher_text += matrix[r2][c1]
                
        return cipher_text

    def playfair_decrypt(self, cipher_text, key):
        matrix = self.create_matrix(key)
        cipher_text = cipher_text.upper().replace('J', 'I')
        plain_text = ""
        
        for i in range(0, len(cipher_text), 2):
            char1, char2 = cipher_text[i], cipher_text[i+1]
            r1, c1 = self._find_position(matrix, char1)
            r2, c2 = self._find_position(matrix, char2)
            
            if r1 == r2:  # Cùng hàng: dịch sang trái
                plain_text += matrix[r1][(c1 - 1) % 5]
                plain_text += matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:  # Cùng cột: dịch lên trên
                plain_text += matrix[(r1 - 1) % 5][c1]
                plain_text += matrix[(r2 - 1) % 5][c2]
            else:  # Khác hàng khác cột
                plain_text += matrix[r1][c2]
                plain_text += matrix[r2][c1]
                
        return plain_text