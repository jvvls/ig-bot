import random
import string
from br_nome_gen import pessoa_random

class Usuario:
    def __init__(self):
        self.pessoa = pessoa_random()

    def fullname(self):
        name = self.pessoa.nome.split()[0]
        lastname = self.pessoa.nome.split()[-1]
        return f"{name} {lastname}"

    def user(self):
        name = self.pessoa.nome.split()[0]
        sobrenome = self.pessoa.nome.split()[-1]
        numero_aleatorio1 = random.randint(1, 5000)
        numero_aleatorio2 = random.randint(1, 50)
        return f"{numero_aleatorio2}{name.lower()}_{sobrenome.lower()}{numero_aleatorio1}"
    
    def email(self):
        return 'vou fazer ainda'

    def password(self, length=12):
        if length < 4:
            raise ValueError("Length must be at least 4 to include all character types.")

        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
        
        random_string = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice("!@#$%^&*")
        ]
        
        random_string += random.choices(characters, k=length - 4)
        
        random.shuffle(random_string)
        
        return ''.join(random_string)

usuario = Usuario()
print(usuario.fullname())  
print(usuario.user())  
print(usuario.email())
print(usuario.password()) 
