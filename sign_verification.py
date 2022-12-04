from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.x509.oid import NameOID
import datetime
import cryptography.hazmat.primitives.serialization as serialization
import json_manager
import json

class SignVerification:
    def __init__(self):
        pass
    
    def generate_private_key(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        return private_key

    def encrypt_private_key(self, private_key, password):
        # Encrypt the private key
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
        )
        return pem
    
    def decrypt_private_key(self, private_key, password):
        # Decrypt the private key
        private_key = serialization.load_pem_private_key(
            private_key,
            password=password.encode(),
        )
        return private_key
    
    def deserialize_public_key(self, public_key):
        return serialization.load_pem_public_key(public_key)

    def generate_public_key(self, private_key):
        public_key = private_key.public_key()
        return public_key

    def encrypt_public_key(self, public_key):
        # Encrypt the public key
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem    
    def create_signature(self, message, private_key):
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def generate_certificate(self, private_key, mail:str):
        subject = issuer = x509.Name([ x509.NameAttribute(NameOID.COMMON_NAME, mail) ])
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.utcnow()
        ).not_valid_after(
            # Our certificate will be valid for 10 days
            datetime.datetime.utcnow() + datetime.timedelta(days=10)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
            critical=False,
        # Sign our certificate with our private key
        ).sign(private_key, hashes.SHA256())
        with open("database/certificates/certificate_"+mail+".pem", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
    
    def encrypt_message(self, message, public_key):
        return public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    
    def decrypt_message(self, private_key, message):
        return private_key.decrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    
    def sign_message(self, private_key, input_file):
        # first we copy the message from input_file into a new file input_signed.txt
        with open(input_file, 'r') as file:
            data = file.read()
            file.close()
        bdata = data.encode('utf-8')
        # now we create the signature from the message and the private key
        signature = self.create_signature(bdata, private_key)
        # database = json_manager.JsonManager(input_file)
        return str(signature)
        
        
    
    def verify_signature(self, public_key, input_file):
        # first we read the message from input_file
        try:
            with open(input_file, 'r') as file:
                data = file.read()
                file.close()

        except: # no file found
            return "No marks were uploaded"
        # then we read the signature from the end of the file
        signature = data[-256:]
        try:
            public_key.verify(
                signature,
                data[:-256],
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return "The signature is valid."
        except:
            return "The signature is not valid."
