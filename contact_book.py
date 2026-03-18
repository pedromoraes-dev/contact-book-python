from contact import Contatc

class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, name, phone, email):
        contact = Contatc(name, phone, email)
        self.contacts.append(contact)
        print('\nContato adicionado com sucesso!')
    
    def list_contact(self):
        if not self.contacts:
            print('Nenhum contato cadastrado!')
            return
        self.contacts.sort(key=lambda contact: contact.name)
        for contact in self.contacts:
            print(contact)
            
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print('\n',contact)
                return
        print('Contato não encontrado!')
    
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print('\nContato removido com sucesso!')
                return
        print('Contato não encontrado ou cadastrado!')