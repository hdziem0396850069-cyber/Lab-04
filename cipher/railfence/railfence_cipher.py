class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text
            
        # Khởi tạo các hàng (rails) dưới dạng danh sách
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: đi xuống, -1: đi lên
        
        # Xếp từng ký tự vào các hàng theo hình zigzag
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            
            # SỬA LỖI 1: Đưa lệnh này ra ngoài các khối if/elif nhưng vẫn TRONG vòng lặp for
            rail_index += direction  
            
        # SỬA LỖI 2: Đưa khối gộp chuỗi ra NGOÀI hoàn toàn vòng lặp for
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text

        # Bước 1: Tính toán số lượng ký tự nằm ở mỗi hàng (rail)
        rail_lengths = [0] * num_rails
        rail_index = 0 
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Bước 2: Cắt chuỗi cipher_text và phân bổ vào các hàng
        rails = []
        start = 0
        for length in rail_lengths:
            # Chuyển đổi chuỗi thành list để dễ dàng bóc tách ký tự
            rails.append(list(cipher_text[start:start + length]))
            start += length
            
        # Bước 3: Đọc lại các ký tự theo hình zigzag để khôi phục plain_text
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            if rails[rail_index]:  # Nếu hàng vẫn còn ký tự
                plain_text += rails[rail_index].pop(0)  # Lấy ký tự đầu tiên ra
            
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text