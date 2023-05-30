from rest_framework.serializers import ValidationError


def password_validation(pass1: str, pass2: str):
    message = ""
    if pass1 != pass2:
        message = "passwords are not equal"
        return False, message
    
    if len(pass2) < 10:
        message = "passwords must have more than 10 characters"
        return False, message
    
    if pass2.lower() == pass2:
        message = "passwords must have at least one uppercase char"
        return False, message
    
    if pass2.upper() == pass2:
        message = "passwords must have at least one lowercase char"
        return False, message
    
    return True, ""
    
