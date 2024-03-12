import string
import random

class PasswordGenerator:
    def __init__(self):
        pass
        
    def generate_password(self, length=8, include_uppercase=False, include_special_chars=False):
        characters = string.ascii_letters + string.digits
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_special_chars:
            characters += string.punctuation
            
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def check_strength(self, password):
        
        if len(password) < 8:
            return "Débil"
        elif len(password) < 12:
            return "Media"
        else:
            return "Fuerte"