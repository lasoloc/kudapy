from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import base64


def rsa_encrypt(message, public_key):
    message = str.encode(message)
    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    encrypted_text = base64.b64encode(encrypted_text)
    return encrypted_text

def rsa_decrypt(encrypted_text, private_key):
    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)
    return decrypted_text






# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import binascii
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import hashes

# import base64


# def rsa_encrypt(message, public_key):
#     """
#     encrypt message with RSA public key
#     """
#     ciphertext = public_key.encrypt(
#         message,
#         padding.OAEP(
#         mgf = padding.MGF1(algorithm = hashes.SHA256()),
#         algorithm = hashes.SHA256(),
#         label = None
#         )
#     )
#     return base64.b64encode(ciphertext).decode('utf-8')
#     #return ciphertext

# def rsa_decrypt(ciphertext, private_key):
#     """
#     decrypt encrypted message with RSA private key
#     """
#     plaintext = private_key.decrypt(
#             ciphertext,
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#     return plaintext
