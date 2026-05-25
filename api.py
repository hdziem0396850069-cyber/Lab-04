from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__)
from cipher.playfair.playfair_cipher import PlayfairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher

transposition_cipher = TranspositionCipher(key=1)

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayfairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Thiếu dữ liệu JSON Body"}), 400
        
    key = data.get('key', '')
    cipher = PlayfairCipher()
    matrix = cipher.create_matrix(key)
    return jsonify({"matrix": matrix})

# 2. API Mã hóa Playfair
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Thiếu dữ liệu JSON Body"}), 400
        
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    
    cipher = PlayfairCipher()
    result = cipher.playfair_encrypt(plain_text, key)
    return jsonify({"cipher_text": result})

# 3. API Giải mã Playfair
@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Thiếu dữ liệu JSON Body"}), 400
        
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    
    cipher = PlayfairCipher()
    result = cipher.playfair_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": result})

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

raifence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    # Sử dụng get_json() để đọc chính xác dữ liệu từ Body -> raw -> JSON của Postman
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Không nhận được dữ liệu JSON"}), 400
        
    plain_text = data.get('plain_text', '')
    # Chuyển đổi key từ chuỗi sang số nguyên, ép mặc định là 3 nếu không truyền
    key = int(data.get('key', 3)) 
    
    # Gọi hàm từ class RailFenceCipher mà bạn đã sửa
    cipher = RailFenceCipher()
    result = cipher.rail_fence_encrypt(plain_text, key)
    
    return jsonify({"cipher_text": result})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Không nhận được dữ liệu JSON"}), 400
        
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 3))
    
    cipher = RailFenceCipher()
    result = cipher.rail_fence_decrypt(cipher_text, key)
    
    return jsonify({"decrypted_text": result})
# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)