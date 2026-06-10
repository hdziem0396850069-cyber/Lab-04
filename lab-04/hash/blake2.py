# blake2.py
import hashlib

def blake2(message):
    # Create Blake2b hash object with 64-byte digest
    blake2_hash = hashlib.blake2b(digest_size=64)
    # Update with the message (already in bytes)
    blake2_hash.update(message)
    # Return raw digest
    return blake2_hash.digest()

def main():
    # Ask user for input and encode to bytes
    text = input('Nhập chuỗi văn bản: ').encode('utf-8')
    # Compute Blake2 hash
    hashed_text = blake2(text)

    # Print results
    print('Chuỗi văn bản đã nhập:', text.decode('utf-8'))
    print('BLAKE2 Hash:', hashed_text.hex())

if __name__ == '__main__':
    main()
