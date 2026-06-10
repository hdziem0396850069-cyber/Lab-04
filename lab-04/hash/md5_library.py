# md5_library.py
import hashlib

def calculate_md5(input_string):
    # Create MD5 hash object
    md5_hash = hashlib.md5()
    # Update with the input string (encoded to bytes)
    md5_hash.update(input_string.encode('utf-8'))
    # Return the hexadecimal digest
    return md5_hash.hexdigest()

if __name__ == "__main__":
    # Ask user for input
    input_string = input("Nhập chuỗi cần băm: ")
    # Calculate MD5 hash
    md5_hash = calculate_md5(input_string)
    # Print result
    print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
