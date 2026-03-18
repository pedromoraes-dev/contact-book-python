class Contatc:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f'Nome: {self.name} - Telefone: {self.phone} - email: {self.email}'