# client.py
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate client key pair
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Derive shared secret using client private key and server public key
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Load server public key from PEM file
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Generate DH parameters (must match server’s parameters)
    parameters = dh.generate_parameters(generator=2, key_size=2048)

    # Generate client key pair
    private_key, public_key = generate_client_key_pair(parameters)

    # Derive shared secret
    shared_secret = derive_shared_secret(private_key, server_public_key)

    # Print shared secret in hex format
    print("Shared secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
