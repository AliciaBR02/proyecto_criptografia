from cryptography.hazmat.primitives.asymmetric import rsa
import cryptography.hazmat.primitives.serialization as serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
import datetime

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Various details about who we are. For a self-signed certificate the
# subject and issuer are always the same.
# 
# CREACIÓN DEL CERTIFICADO
# tiene la clave pública

# Write our key to disk for safe keeping
with open("database/certificate.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),
    ))
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
with open("path/to/certificate.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

# from cryptography.hazmat.primitives import serialization

# with open("path/to/key.pem", "rb") as key_file:
#     private_key = serialization.load_pem_private_key(
#         key_file.read(),
#         password=None,
#     )


# se escriben los datos cifrados con correo y contraseña del profesor en la base de datos
# si el profesor quiere que el estudiante vea sus notas, se le envía el archivo con el texto decriptado y firmado con la clave privada del profesor -> ARCHIVO CON NOTAS -> el estudiante lo descifra con la clave pública del profesor
# en la base de datos, todo va a estar cifrado, pero SOLO SI EL PROFESOR QUIERE, creará un archivo con las notas del estudiante sin cifrar nada y lo firmará con su clave privada para que el estudiante pueda acceder a él


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
message = b"A message I want to sign"
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

message = b"encrypted data"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)




# FUNSIONAMIENTO DE LA VAINA BAKANA
# el alumno va a tener siempre un archivo con sus notas -> ese archivo será el último archivo subido/firmado por el profesor
# el profesor irá modificando el archivo de notas firmandolas y todo el show
# pero el profesor puede decidir si quiere que el alumno vea sus notas o no
    # si el profesor quiere que el alumno vea sus notas, el profesor le enviará el archivo de notas firmado con su clave privada
# cada vez que el hash del archivo del profesor sin subir sea diferente al archivo que posee el alumno, el hash será distinto y por tanto el alumno aún no podrá acceder a ver sus notas
# es decir, hasta que el profesor no decida subir los cambios y firmarlos, el alumno no podrá hacer nada.

# importante: hay que comparar el hash del archivo que no ha firmado aún el profesor con el hash del archivo que está subido