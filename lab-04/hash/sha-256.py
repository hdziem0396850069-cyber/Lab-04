# sha-256.py
import hashlib

def calculate_sha256_hash(data):
    # Create SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Convert string to bytes and update the hash
    sha256_hash.update(data.encode('utf-8'))
    # Return the hexadecimal digest
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    # Ask user for input
    data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
    # Calculate SHA-256 hash
    hash_value = calculate_sha256_hash(data_to_hash)
    # Print result
    print("Giá trị hash SHA-256:", hash_value)
