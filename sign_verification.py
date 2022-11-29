from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.x509.oid import NameOID
import datetime
import cryptography.hazmat.primitives.serialization as serialization

class SignVerification:
    def __init__(self):
        pass
    
    def generate_private_key(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        return private_key
    
    def generate_public_key(self, private_key):
        public_key = private_key.public_key()
        return public_key
    
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

    def generate_certificate(self, private_key):
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"mysite.com"),
        ])
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
        # Write our certificate out to disk.
        with open("database/certificates/certificate.pem", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
            
    # method that will save the message with the signature at the end in a new file input_signed.txt
    def sign_message(self, private_key, input_file):
        # first we copy the message from input_file into a new file input_signed.txt
        with open(input_file, 'r') as file:
            data = file.read()
        # convert to bytes-like object
        bdata = data.encode('utf-8')
        with open('input_signed.txt', 'wb') as file:
            file.write(bdata)
        # now we create the signature from the message and the private key
        signature = self.create_signature(bdata, private_key)
        # decode the signature to string
        # s = bytearray(signature)
        # s.extend(bytes(serialized, 'utf-8'))
        # decoded_signature = signature.decode('utf-8')
        # then we add the signature at the end of the file
        with open('input_signed.txt', 'ab') as file:
            file.write(signature)
    
    def verify_signature(self, public_key, input_file):
        # first we read the message from input_file
        with open(input_file, 'rb') as file:
            data = file.read()
        # then we read the signature from the end of the file
        signature = data[-256:]
        # finally we verify the signature
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
            print("The signature is valid.")
        except:
            print("The signature is not valid.")
        
s = SignVerification()
private_key = s.generate_private_key()
s.generate_certificate(private_key)
s.sign_message(private_key, 'input.txt')
public_key = s.generate_public_key(private_key)
s.verify_signature(public_key, 'input_signed.txt')