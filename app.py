from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.rsa_cipher import RSACipher

# Định nghĩa đối tượng Flask trước khi cấu hình các Route
app = Flask(__name__)

# ==================== TRANG CHỦ & CAESAR CIPHER ====================

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    Caesar = CaesarCipher()
    encrypted_text = Caesar.caesar_encrypt_text(text, key)
    
    return render_template('caesar.html', 
                           encrypted_text=encrypted_text, 
                           text_encrypt=text, 
                           key_encrypt=key)

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    Caesar = CaesarCipher()
    decrypted_text = Caesar.caesar_decrypt_text(text, key)
    
    return render_template('caesar.html', 
                           decrypted_text=decrypted_text, 
                           text_decrypt=text, 
                           key_decrypt=key)


# ==================== RSA CIPHER ====================

# 1. Điều hướng khi nhấn vào link "RSA Cipher" từ trang chủ index.html
@app.route("/rsa")
def rsa_page():
    return render_template('rsa.html')

# 2. Xử lý nút bấm Encrypt của RSA
@app.route("/rsa/encrypt", methods=['POST'])
def rsa_encrypt():
    text = request.form['inputPlainText']
    pub_key_str = request.form['publicKey']
    
    # Tách chuỗi "7, 187" thành cặp số e và n
    e, n = map(int, pub_key_str.split(','))
    
    rsa = RSACipher()
    encrypted_text = rsa.rsa_encrypt(text, e, n)
    
    return render_template('rsa.html', 
                           encrypted_text=encrypted_text, 
                           text_encrypt=text, 
                           pub_key=pub_key_str)

# 3. Xử lý nút bấm Decrypt của RSA
@app.route("/rsa/decrypt", methods=['POST'])
def rsa_decrypt():
    text = request.form['inputCipherText']
    priv_key_str = request.form['privateKey']
    
    # Tách chuỗi "23, 187" thành cặp số d và n
    d, n = map(int, priv_key_str.split(','))
    
    rsa = RSACipher()
    decrypted_text = rsa.rsa_decrypt(text, d, n)
    
    return render_template('rsa.html', 
                           decrypted_text=decrypted_text, 
                           text_decrypt=text, 
                           priv_key=priv_key_str)


# Khởi chạy ứng dụng tại Port 5050 chuẩn theo tài liệu
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)