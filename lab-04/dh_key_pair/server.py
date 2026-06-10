from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate DH parameters
def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

# Generate server key pair
def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # Step 1: Generate parameters
    parameters = generate_dh_parameters()

    # Step 2: Generate server key pair
    private_key, public_key = generate_server_key_pair(parameters)

    # Step 3: Save server public key to PEM file
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("Server public key saved to server_public_key.pem")

if __name__ == "__main__":
    main()
