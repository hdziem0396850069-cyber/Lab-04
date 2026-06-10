# sha-3.py
from Crypto.Hash import SHA3_256

def sha3(message):
    # Create SHA3-256 hash object
    sha3_hash = SHA3_256.new()
    # Update with the message (already in bytes)
    sha3_hash.update(message)
    # Return the raw digest
    return sha3_hash.digest()

def main():
    # Ask user for input and encode to bytes
    text = input('Nhập chuỗi văn bản: ').encode('utf-8')
    # Compute SHA3 hash
    hashed_text = sha3(text)

    # Print results
    print('Chuỗi văn bản đã nhập:', text.decode('utf-8'))
    print('SHA-3 Hash:', hashed_text.hex())

if __name__ == '__main__':
    main()
