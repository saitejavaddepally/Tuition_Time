
from passlib.hash import pbkdf2_sha256

# from utils.errors import send_password_fault_error

def password_checker(password1, enc_password):
    if(pbkdf2_sha256.verify(password1,enc_password)):
        return True
    else:
        return False

